import numpy as np
#import pandas as pd
#import scipy.io as sio
#from os.path import dirname, join as pjoin

path='C:/Users/ptsch/Box/AP3_Open_Access_Model/Course_Project/Model_Components'

# read in emissions
areaSources = np.genfromtxt(path + '/Emissions/area_sources_2008.csv', 
delimiter=',')
lowStacks = np.genfromtxt(path + '/Emissions/low_2008.csv', 
delimiter=',')
medStacks = np.genfromtxt(path + '/Emissions/medium_2008.csv', 
delimiter=',')
tallStacks = np.genfromtxt(path + '/Emissions/tall_2008.csv', 
delimiter=',')
tall2Stacks = np.genfromtxt(path + '/Emissions/tall2_2008.csv', 
delimiter=',')

# read in demographic data (population and mortality)
population = np.genfromtxt(path + '/Population_Mortality/pop_2008.csv', 
delimiter=',')
mortality = np.genfromtxt(path + '/Population_Mortality/mort_2008.csv', 
delimiter=',')

# read in source/receptor matrices
## Area
areaSoReNOx = np.genfromtxt(path + '/SR_Matrices/Area_NOx.csv', 
delimiter=',')
areaSoRePMVOC = np.genfromtxt(path + '/SR_Matrices/Area_PM_VOC.csv', 
delimiter=',')
areaSoReSO2 = np.genfromtxt(path + '/SR_Matrices/Area_SO2.csv', 
delimiter=',')
areaSoReNH3 = np.genfromtxt(path + '/SR_Matrices/Area_NH3.csv', 
delimiter=',')

## Low
lowSoReNOx = np.genfromtxt(path + '/SR_Matrices/Low_NOx.csv', 
delimiter=',')
lowSoRePMVOC = np.genfromtxt(path + '/SR_Matrices/Low_PM_VOC.csv', 
delimiter=',')
lowSoReSO2 = np.genfromtxt(path + '/SR_Matrices/Low_SO2.csv', 
delimiter=',')
lowSoReNH3 = np.genfromtxt(path + '/SR_Matrices/Low_NH3.csv', 
delimiter=',')

## Medium
medSoReNOx = np.genfromtxt(path + '/SR_Matrices/Med_NOx.csv', 
delimiter=',')
medSoRePMVOC = np.genfromtxt(path + '/SR_Matrices/Med_PM_VOC.csv', 
delimiter=',')
medSoReSO2 = np.genfromtxt(path + '/SR_Matrices/Med_SO2.csv', 
delimiter=',')
medSoReNH3 = np.genfromtxt(path + '/SR_Matrices/Med_NH3.csv', 
delimiter=',')

## Tall
tallSoReNOx = np.genfromtxt(path + '/SR_Matrices/Tall_NOx.csv', 
delimiter=',')
tallSoRePMVOC = np.genfromtxt(path + '/SR_Matrices/Tall_PM_VOC.csv', 
delimiter=',')
tallSoReSO2 = np.genfromtxt(path + '/SR_Matrices/Tall_SO2.csv', 
delimiter=',')
tallSoReNH3 = np.genfromtxt(path + '/SR_Matrices/Tall_NH3.csv', 
delimiter=',')

## Tall2
tall2SoReNOx = np.genfromtxt(path + '/SR_Matrices/Tall2_NOx.csv', 
delimiter=',')
tall2SoRePMVOC = np.genfromtxt(path + '/SR_Matrices/Tall2_PM_VOC.csv', 
delimiter=',')
tall2SoReSO2 = np.genfromtxt(path + '/SR_Matrices/Tall2_SO2.csv', 
delimiter=',')
tall2SoReNH3 = np.genfromtxt(path + '/SR_Matrices/Tall2_NH3.csv', 
delimiter=',')

deaths = population * mortality
print(sum(sum(deaths))

# below here is model code from Matlab copied over