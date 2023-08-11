# Metadata exploration:
## Requirements:
  - due to problems with `pylegendmeta`, I needed to use a personal cloned repository containing the metadata.
    - Follow this [example](https://legend-exp.atlassian.net/wiki/spaces/LEGEND/pages/645234763/Getting+started+with+the+Dataloader+and+LegendMetadata) for more questions; the problem seems common on NERSC.
  - Need to make sure `L200_SMM.xlsx` is included. It contains HV Flanges information. It is a reformatted L200 master channelmap shared by Brady.

---
For simplicity, I kept all forms of the slow control analysis in a single notebook, due to the need to make a channelmap in memory using the cloned repository, everytime the notebook is run.
Observed systems:
- Channels & Rawchannels (unique IDs, and can be substituted by the names of the detectors)
- HV Filters
- Strings
- CC4s
- HV Flanges
---
All systems, except HV Flanges, can be generalized with the same general approaches.
1. Create channel map
2. Extract relevant information for each system
3. Create a minimap of the unique hardware in question, e.g. P03 R003 - 81 channels and 16 CC4s.
4. Count the top 10 outliers for each one. Looking at the top 10 outliers for each label was enough for P03 R003, as most categories only had a handful of outliers

Due to HV Flange information not being included in pylegendmeta, this has to be done manually, and through a slightly different approach.
Look at the different options available for each function if you need plots, top counts, or other details regarding each category.

any questions please [Email me](mailto:Mabschott@outlook.com)
