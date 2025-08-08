# **Precision Paths**
## An Aggregated, Curated, & Itemized Collection of Open and Available Precision Functional Mapping (PFM) from Resting State fMRI Data
Contributors: Jonathan Ahern, Elizabeth Li, Sujin Park


Project Output [(presentation slides)](https://docs.google.com/presentation/d/1HJ0MWlfA3SRCS6izPqH9STxzEKUupiQYGsJzuQueHgU/edit?slide=id.g373766c5e58_0_0#slide=id.g373766c5e58_0_0): 
1. [Literature Review Spreadsheet](https://docs.google.com/spreadsheets/d/1GAycMBfSNfVKg72nL3qlH0fvf_AokEXm1qFT6KMysBk/edit?usp=sharing): Collection of PFM studies with accessible datasets
2. [PFM Data Explorer](https://precision-paths-gptlrvaefbfjz2bcowz4yb.streamlit.app/): Web-app version of interactive figures of PFM study subjects


## Goals: 
- Summary and Graphical Figure of released PFM datasets
- Provide easy access to the original articles/datasets using PFM approach
- Summarize Preprocessing Steps and key parameters for each dataset (to facilitate cross-dataset comparisons)
- Future Plan: Periodic updates as more data become available and gaps in the literature are filled

## What is PFM?
We borrow our primary definition from previous work.
> "PFM is the precise characterization of individual brain function, currently made possible by the collection of hours of non-invasive fMRI data from an individual, typically collected over multiple visits. PFM relies on large amounts of resting state or task fMRI data in order to extract highly reliable, individualized estimates of brain function and functional connectivity (FC), which allow for the creation of high-resolution, high-fidelity individual-specific maps of functional brain networks or activation." [(Demeter & Greene, 2025)](https://doi.org/10.1038/s41386-024-01941-z)[^1]

### How do we parameterize PFM for this dataset?
**We consider a dataset eligible for use in PFM if there is _over_ 90 minutes of single-echo or 40 minutes of multi-echo whole-brain resting-state data**

Please note that there is no "one-size-fits-all" definition since every study has different methodololgical details (e.g., single echo vs. multi-echo; 3T vs. 7T tesla; collection sites; type of scanners; task paradigms; target population) and goals (e.g., ROI-based vs. whole-brain analysis, cortex requires 45 min of data to achieve high reliability while the cerebellum and subcortex require more [(Gordon et al., 2017)](https://www.cell.com/neuron/fulltext/S089662731730613X)[^2], [(Greene et al., 2020)](https://www.cell.com/neuron/fulltext/S0896-6273(19)30975-4?dgcid=raven_jbs_etoc_email)[^3], [(Lynch et al., 2020)](https://www.sciencedirect.com/science/article/pii/S2352154620301996#bib0270)[^4]. Our decision was mainly built upon the definition from [(Gratton et al, 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7203002/)[^5]. You can check if the dataset is openly available or not in the [*spreadsheet*](https://docs.google.com/spreadsheets/d/1ZMnbptWr2mAtJtoK5vAUa3AvqwJfOTWLE0lrchhi25w/edit?usp=sharing).

## Ongoing Data Aggregation
Building a GitHub Repository for Precision (Functional Mapping) Datasets: [Literature Review Spreadsheet](https://docs.google.com/spreadsheets/d/1GAycMBfSNfVKg72nL3qlH0fvf_AokEXm1qFT6KMysBk/edit?usp=sharing)

In the spreadsheet, there are 3 sub-sheets. 
1. The first sheet (1. PFM papers with available data) is a list of papers with accessible data (publicly available or available upon request) that we could find for literature review.
2. The second sheet (2. Subject-level information) has more detailed information in a subject-level across these datasets. You can make a copy of the sheet and filter the subjects as you need. Descriptions are in the comments of the first row of a column. Papers with yellow highlight are papers that are not listed in Table 1 from [(Gratton et al, 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7203002/)[^5]. For visualization, we also provide an interacitve app version of this table, check out [PFM Data Explorer](https://precision-paths-gptlrvaefbfjz2bcowz4yb.streamlit.app/)!
3. In the third sheet (3. Scan parameters), we summarized scan parameters of study that meets the following criteria: 1) 'TRUE' for 'Mostly resting state/ Enough Resting State' column in the 2nd spreadsheet, AND  2) 'Open' or 'Available upon request' for 'Open?' column in the 2nd spreadsheet. 

## Other useful resources
- Lit Review Spreadsheet is an updated version of [(Gratton et al, 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7203002/)[^5]
- Github Repository for other brain-imaging modality datasets: [here](https://link.springer.com/article/10.1007/s11682-022-00724-8)

## Note
This repository is a project for Neurohackademy 2025.  

## Works Cited
[^1]: Demeter, D.V., Greene, D.J. The promise of precision functional mapping for neuroimaging in psychiatry. Neuropsychopharmacol. 50, 16–28 (2025). https://doi.org/10.1038/s41386-024-01941-z
[^2]: Gordon, E. M., Laumann, T. O., Gilmore, A. W., Newbold, D. J., Greene, D. J., Berg, J. J., ... & Dosenbach, N. U. (2017). Precision functional mapping of individual human brains. Neuron, 95(4), 791-807.
[^3]: Greene, D. J., Marek, S., Gordon, E. M., Siegel, J. S., Gratton, C., Laumann, T. O., ... & Dosenbach, N. U. (2020). Integrative and network-specific connectivity of the basal ganglia and thalamus defined in individuals. Neuron, 105(4), 742-758.
[^4]: Lynch, C. J., Power, J. D., Scult, M. A., Dubin, M., Gunning, F. M., & Liston, C. (2020). Rapid precision functional mapping of individuals using multi-echo fMRI. Cell reports, 33(12).
[^5]: Gratton, C., Kraus, B. T., Greene, D. J., Gordon, E. M., Laumann, T. O., Nelson, S. M., Dosenbach, N. U. F., & Petersen, S. E. (2020). Defining Individual-Specific Functional Neuroanatomy for Precision Psychiatry. Biological psychiatry, 88(1), 28–39. https://doi.org/10.1016/j.biopsych.2019.10.026

