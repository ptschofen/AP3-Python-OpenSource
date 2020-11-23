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

deaths = population * mortality
print(sum(sum(deaths))


### below here is model code from Matlab copied over

'''
% (* ::Package:: *)

% Baseline Concentrations
% 28761.72 converts tons per year to milligrams per second to micrograms
% per cubic meter for annual emissions

% Run Secondary Calibration developed by Sergi et al. 2019
run PM_secondary_calibration_2017

% Area Sources
NH3 (:,1)   =         1.06.*(28761.72.*(Area_Source {4,1}(:,1)')*((NH4_Cal.*Area_Source {5,1})))';
NOx (:,1) =           1.35.*(28761.72.*(Area_Source {4,1}(:,2)')*((NOx_Cal.*Area_Source {1,1})))';
PM_25_Primary (:,1) =       (28761.72.*(Area_Source {4,1}(:,4)')*((PM25_Cal.*Area_Source {2,1})))';
SO2 (:,1)   =         1.50.*(28761.72.*(Area_Source {4,1}(:,5)')*((SO2_Cal.*Area_Source {3,1})))';

A_VOC (:,1) =               (28761.72.*(Area_Source {4,1}(:,6)')*((VOC_Cal.*Area_Source {2,1})))';
B_VOC (:,1) =               (28761.72.*(Area_Source {4,1}(:,7)')*(B_VOC_Cal.*(Area_Source {2,1})))';


# Low Stacks
NH3 (:,2) =           1.06.*(28761.72.*(Low_Stack {4,1}(:,1)')*((NH4_Cal.*Low_Stack {5,1})))';
NOx (:,2) =           1.35.*(28761.72.*(Low_Stack {4,1}(:,2)')*((NOx_Cal.*Low_Stack {1,1})))';
PM_25_Primary (:,2) =       (28761.72.*(Low_Stack {4,1}(:,4)')*((PM25_Cal.*Low_Stack {2,1})))';
SO2 (:,2) =           1.50.*(28761.72.*(Low_Stack {4,1}(:,5)')*((SO2_Cal.*Low_Stack {3,1})))';

A_VOC (:,2) =               (28761.72.*(Low_Stack {4,1}(:,6)')*(VOC_Cal.*Low_Stack {2,1}))';

clear CB_COI CB Visibility Data PM_Emission

% Medium Stacks

NH3 (:,3) =           1.06.*(28761.72.*(Med_Stack {4,1}(:,1)')*((NH4_Cal.*Med_Stack {5,1})))';
NOx (:,3) =           1.35.*(28761.72.*(Med_Stack {4,1}(:,2)')*((NOx_Cal.*Med_Stack {1,1})))';
PM_25_Primary (:,3) =       (28761.72.*(Med_Stack {4,1}(:,4)')*((PM25_Cal.*Med_Stack {2,1})))';
SO2 (:,3) =           1.50.*(28761.72.*(Med_Stack {4,1}(:,5)')*((SO2_Cal.*Med_Stack {3,1})))';

A_VOC (:,3) =               (28761.72.*(Med_Stack {4,1}(:,6)')*(VOC_Cal.*Med_Stack {2,1}))';

% Tall Stacks

NH3 (:,4) =           1.06.*(28761.72.*(Tall_Stack {4,1}(:,1)')*((NH4_Cal_tall.*Tall_Stack {5,1})))';
NOx (:,4) =           1.35.*(28761.72.*(Tall_Stack {4,1}(:,2)')*((NOx_Cal_tall.*Tall_Stack {1,1})))';
PM_25_Primary (:,4) =       (28761.72.*(Tall_Stack {4,1}(:,4)')*((PM25_Cal_tall.*Tall_Stack {2,1})))';
SO2 (:,4) =           1.50.*(28761.72.*(Tall_Stack {4,1}(:,5)')*((SO2_Cal_tall.*Tall_Stack {3,1})))';

A_VOC (:,4) =               (28761.72.*(Tall_Stack {4,1}(:,6)')*(VOC_Cal_tall.*Tall_Stack {2,1}))';

% New Tall Stacks

NH3 (:,5) =           1.06.*(28761.72.*(New_Tall {4,1}(:,1)')*((NH4_Cal_tall2.*New_Tall {5,1})))';
NOx (:,5) =           1.35.*(28761.72.*(New_Tall {4,1}(:,2)')*((NOx_Cal_tall2.*New_Tall {1,1})))';
PM_25_Primary (:,5) =       (28761.72.*(New_Tall {4,1}(:,4)')*((PM25_Cal_tall2.*New_Tall {2,1})))';
SO2 (:,5) =           1.50.*(28761.72.*(New_Tall {4,1}(:,5)')*((SO2_Cal_tall2.*New_Tall {3,1})))';

A_VOC (:,5) =               (28761.72.*(New_Tall {4,1}(:,6)')*(VOC_Cal_tall2.*New_Tall {2,1}))';

    run Nitrate_Sulfate_Ammonium
    run PM_25_Base_Raw
    run PM_25_Health_Base
    
clear CB_COI CB Visibility PM_Emission
'''