# MRLC Data Analysis Readme

This repository contains data scraped from the Multi-Resolution Land Characteristics (MRLC) consortium website (https://www.mrlc.gov/eva/). The MRLC consortium provides consistent and relevant land cover information at the national scale for various environmental, land management, and modeling applications. The data scraped includes information on land cover types and their distribution across states, counties, and years.

## Data Collection Process

The data was collected by scraping the MRLC website using a web scraping tool. Specifically, the data was collected from the "Land Cover Area and Change Distribution" table displayed after hitting the "Get Started" button on the MRLC website.

## Variables and Their Significance

The following variables were fetched from the website, along with their descriptions and significance:

- **HID** - High Intensity Developed: Areas characterized by high levels of urban or built-up development, providing insights into urbanization trends and environmental impacts.
  
- **MID** - Medium Intensity Developed: Areas with moderate levels of development, useful for understanding suburban sprawl and population growth patterns.
  
- **LID** - Low Intensity Developed: Areas with sparse development, valuable for assessing rural development and land conservation efforts.
  
- **OSD** - Open Space Developed: Areas developed for human use while maintaining natural characteristics, important for land management decisions and conservation efforts.
  
- **CRP** - Cropland/Pasture: Areas used for agricultural purposes, reflecting shifts in agricultural practices and land use policies.
  
- **PAS** - Pasture: Lands specifically used for grazing livestock, providing insights into livestock management practices and land sustainability.
  
- **GRS** - Grassland/Shrubland: Natural or semi-natural vegetation dominated by grasses or shrubs, important for biodiversity conservation and habitat management.
  
- **DFO** - Deciduous Forest: Forests dominated by deciduous tree species, useful for assessing forest health and biodiversity conservation efforts.
  
- **EFO** - Evergreen Forest: Forests characterized by evergreen tree species, important for understanding forest dynamics and ecosystem services.
  
- **MFO** - Mixed Forest: Forests with a mix of deciduous and evergreen tree species, providing insights into forest composition shifts and habitat resilience.
  
- **SHB** - Shrubland: Lands dominated by shrubby vegetation, relevant for assessing ecosystem dynamics and land degradation processes.
  
- **WDW** - Woody Wetland: Wetland ecosystems characterized by woody vegetation, critical for wetland conservation and water quality management.
  
- **EHW** - Emergent Herbaceous Wetland: Wetlands dominated by herbaceous vegetation, providing insights into wetland biodiversity and resilience to climate change.
  
- **BRN** - Barren Land: Lands devoid of vegetation cover, important for assessing land degradation and desertification processes.
  
- **WTR** - Water: Surface water bodies such as lakes, rivers, and ponds, critical for water resource management and aquatic ecosystem health.

- **PIS** - Presumably another land cover category, but missing from the provided data.

## Future Work

- The missing land cover category (**PIS**) needs to be identified and included in the analysis.
  
- Further analysis can be conducted on the collected data to identify trends, patterns, and changes in land cover over time.
  
- Visualization techniques can be employed to present the data in a more understandable and insightful manner.

  
Please feel free to contribute to this repository by adding more analysis, improving the scraping process, or suggesting enhancements to the readme file. Your contributions are highly appreciated!