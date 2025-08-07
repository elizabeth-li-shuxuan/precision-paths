#8/7/2025 Elizabeth Li @ Neurohackademy
# app to deploy on steamlit

import streamlit as st
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from pathlib import Path

# ————————————————————— App Title —————————————————————
st.title("PFM Data Explorer")



# ————————————————————— LOAD AND CACHE DATA —————————————————————
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    # parse Age_num
    def parse_age(age):
        if isinstance(age, str):
            s = age.strip().replace('–','-').replace('—','-').replace(' to ','-')
            nums = re.findall(r'\d+\.?\d*', s)
            if len(nums) >= 2:
                low, high = map(float, nums[:2])
                return (low + high) / 2
            if len(nums) == 1:
                return float(nums[0])
        try:
            return float(age)
        except:
            return np.nan
    df['Age_num'] = df['Age'].apply(parse_age)
    # parse Study Year to a 4-digit int
    def parse_year(y):
        m = re.search(r'\b(\d{4})\b', str(y))
        return int(m.group(1)) if m else np.nan
    df['StudyYear_num'] = df['Study Year'].apply(parse_year)
    return df

data_path = "data/data.csv" #top?
df = load_data(data_path)



# ————————————————————— SIDEBAR —————————————————————
st.sidebar.header("Demographics")

# 1. age range and bin size
age_min  = int(df['Age_num'].min(skipna=True))
age_max  = int(df['Age_num'].max(skipna=True))
age_range = age_max - age_min

bin_size = st.sidebar.number_input(
    "Age bin size",
    min_value=1,
    max_value=age_range,      
    step=1,
    value=5,
    help="Width of each age bin in years"
)
age_range = st.sidebar.slider(
    "Age range",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max),
    step=1,
    help="Minimum and maximum are constrainted by the minimum and maximum ages available"
)

# 2 and 3. sex and handedness checkboxes ("pills")
def multi_pill_filter(label, options, help_text=None):
    """Render a multi-select pill widget and return the list of selected options"""
    return st.sidebar.pills(
        label,
        options=options,
        selection_mode='multi',
        default=options,
        help=help_text or f"Filter by {label.lower()}"
    )

sex_options=["Male", "Female", "Other", "Unknown"]
handedness_options=["Left", "Right", "Ambidextrous", "Unknown"]

sex_filters = multi_pill_filter("Sex", sex_options)
handedness_filters = multi_pill_filter("Handedness", handedness_options)


# 4. study year
year_min = int(df['StudyYear_num'].min(skipna=True))
year_max = int(df['StudyYear_num'].max(skipna=True))

study_year_range = st.sidebar.slider(
    "Study year range",
    min_value=year_min,
    max_value=year_max,
    value=(year_min, year_max),
    step=1,
    help="Minimum and maximum are constrainted by the minimum and maximum ages available"
)




# ————————————————————— APPLY FILTERS —————————————————————
filtered = df.copy()

#1. age 
filtered = filtered[
    (filtered['Age_num'] >= age_range[0]) &
    (filtered['Age_num'] <= age_range[1])
]

#2. sex
if sex_filters:
    filtered = filtered[filtered['Sex'].isin(sex_filters)]

#3. handedness
if handedness_filters:
    filtered = filtered[filtered['Handedness'].isin(handedness_filters)]

#4. study year
filtered = filtered[
    (filtered['StudyYear_num'] >= study_year_range[0]) &
    (filtered['Age_StudyYear_numnum'] <= study_year_range[1])
]






# ————————————————————— BINNING —————————————————————
bins = np.arange(age_range[0], age_range[1]+bin_size, bin_size)
# say bin size = 5, produce labels on the x-axis like "0-5", "5-10", ..., "75-80"
labels = [f"{b}–{b+bin_size}" for b in bins[:-1]]
filtered['age_bin'] = pd.cut(
    filtered['Age_num'],
    bins=bins,
    right=False,
    labels=labels,
    include_lowest=True
)
counts = filtered['age_bin'].value_counts().reindex(labels, fill_value=0)



# ————— Display —————
st.subheader("Counts per Age Bin")
st.bar_chart(counts)

st.subheader("Bar Plot (Matplotlib)")
fig, ax = plt.subplots(figsize=(8, 4))
counts.plot(kind='bar', ax=ax, color='steelblue')
ax.set_title("Participant Count by Age", fontsize=14)
ax.set_xlabel("Age Bin", fontsize=12)
ax.set_ylabel("Count", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# ————— Show Filtered Data —————
st.subheader("Filtered Data Preview")
st.dataframe(filtered.reset_index(drop=True))




