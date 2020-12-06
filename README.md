# AP3-Python-OpenSource

~~ model still under development ~~


## Model Overview
The AP3 model is a model that estimates marginal damages from pollutant emissions that contribute to the formation of fine particulate matter in the contiguous United States. This type of model is called “integrated assessment model” because it combines several steps that are required to derive monetary damages for location-specific pollutant emissions:
1. Emissions need to be fed into the model based on their location and type of emission (ground level such as transit is dealt with differently than emissions through smokestacks of power plants) and sorted by pollutant (we deal with five major precursors to particulate matter)
2. The next step is a very simplified air quality model to estimate PM2.5 concentrations in all these counties
3. The model is then iteratively run with a perturbation of emissions for each location, emission type and precursor pollutant and the differential concentrations from the emission perturbations across all counties are recorded
4. Lastly, we compare concentrations after emission perturbation with the baseline in step 2 to compute concentration differentials, store them and then assess the number of people exposed to quantify health impacts

##
Inputs
The inputs for the model are also computed by us, but this step is not part of the model I’m creating for this project.
Emissions: 
* Area Sources: 3,109 counties x 5 pollutants
* Low Stacks: 3,109 counties x 5 pollutants
* Med Stacks: 3,109 counties x 5 pollutants
* Tall Stacks: 565 facilities x 5 pollutants
* New Tall Stacks: 91 facilities x 5 pollutants
Population files are also preprocessed elsewhere and the data stems from post-censal and intercensal estimates. Mortality data is taken from the Centers for Disease Control and Prevention (CDC).
* Population: 3,109 counties x 19 age groups
* Baseline Mortality: 3,109 counties x 19 age groups

### Source/Receptor Matrices
These matrices are the core of the model as they describe the transport of pollutant mass from source counties to receptor counties.
* Area: 3,109 counties x 3,109 counties (4 different matrices)
* Low 3,109 counties x 3,109 counties (4 different matrices)
* Med 3,109 counties x 3,109 counties (4 different matrices)
* Tall Stacks: 565 facilities x 3,109 counties (4 different matrices)
* More Tall Stacks: 91 facilities x 3,109 counties (4 different matrices)
S/R matrices undergo a change depending on the year in a secondary calibration step.

## Parameters to change
Emissions, Population and Mortality depending on year (2008, 2011, 2014 and 2017 so far)
A number of other parameters are required for the model to run: a dose-response function (or damage function) describes the relationship between exposure to particulate matter and increase in mortality risk — we have two of them: one for infants and one for people aged 30+; age groups 2-29 are assumed to be impervious to adverse health effects from PM exposure. Further, a value of reduced mortality risk (VRMR) monetizes the increased mortality risk.

## Outputs
Potential intermediate results: 
estimated air pollution deaths by the model in baseline configuration
Average estimated concentration 
Marginal Damages: 
* Area Sources: 3,109 counties x 5 pollutants
* Low Stacks: 3,109 counties x 5 pollutants
* Med Stacks: 3,109 counties x 5 pollutants
* Tall Stacks: 565 facilities x 5 pollutants
* New Tall Stacks: 91 facilities x 5 pollutants
