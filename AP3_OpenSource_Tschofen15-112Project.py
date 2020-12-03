import numpy as np
import tkinter, winsound

#import pandas as pd
#import scipy.io as sio

path='C:/Users/ptsch/Box/AP3_Open_Access_Model/Course_Project/Model_Components'

# function that prompts user to type in year for reading in emissions,
# stores year as a variable for other functions 
def emissionVitalsEntry():
    global year
    global areaSourceEmissions
    global lowStackEmissions
    global medStackEmissions
    global tallStackEmissions
    global tall2StackEmissions
    year = input("Enter valid NEI year (2008, 2011, 2014 or 2017): ")

    if not ((year == '2008') | (year == '2011') 
            | (year == '2014') | (year == '2017')): 
        print('Year input invalid, please enter among the options provided.')
        year = input("Enter valid NEI year (2008, 2011, 2014 or 2017)")

    # read in emissions
    areaSourceEmissions = np.genfromtxt(path + '/Emissions/area_sources_' + year +
    '.csv', delimiter=',')
    lowStackEmissions = np.genfromtxt(path + '/Emissions/low_' + year +
    '.csv', delimiter=',')
    medStackEmissions = np.genfromtxt(path + '/Emissions/medium_' + year +
    '.csv', delimiter=',')
    tallStackEmissions = np.genfromtxt(path + '/Emissions/tall_' + year +
    '.csv', delimiter=',')
    tall2StackEmissions = np.genfromtxt(path + '/Emissions/tall2_' + year +
    '.csv', delimiter=',')

    global population
    global mortality
    # read in demographic data (population and mortality)
    population = np.genfromtxt(path + '/Population_Mortality/pop_' + year +
    '.csv', delimiter=',')
    mortality = np.genfromtxt(path + '/Population_Mortality/mort_' + year +
    '.csv', delimiter=',')

# reads in model framework inputs (source-receptor matrices)
def sourceReceptorReadin():
    # read in source/receptor matrices
    ## Area
    global areaSRNOx
    global areaSRPMVOC
    global areaSRSO2
    global areaSRNH3

    global lowSRNOx
    global lowSRPMVOC
    global lowSRSO2
    global lowSRNH3
    
    global medSRNOx
    global medSRPMVOC
    global medSRSO2
    global medSRNH3
    
    global tallSRNOx
    global tallSRPMVOC
    global tallSRSO2
    global tallSRNH3
    
    global tall2SRNOx
    global tall2SRPMVOC
    global tall2SRSO2
    global tall2SRNH3
    
    areaSRNOx = np.genfromtxt(path + '/SR_Matrices/Area_NOx.csv', 
    delimiter=',')
    areaSRPMVOC = np.genfromtxt(path + '/SR_Matrices/Area_PM_VOC.csv', 
    delimiter=',')
    areaSRSO2 = np.genfromtxt(path + '/SR_Matrices/Area_SO2.csv', 
    delimiter=',')
    areaSRNH3 = np.genfromtxt(path + '/SR_Matrices/Area_NH3.csv', 
    delimiter=',')

    ## Low
    lowSRNOx = np.genfromtxt(path + '/SR_Matrices/Low_NOx.csv', 
    delimiter=',')
    lowSRPMVOC = np.genfromtxt(path + '/SR_Matrices/Low_PM_VOC.csv', 
    delimiter=',')
    lowSRSO2 = np.genfromtxt(path + '/SR_Matrices/Low_SO2.csv', 
    delimiter=',')
    lowSRNH3 = np.genfromtxt(path + '/SR_Matrices/Low_NH3.csv', 
    delimiter=',')

    ## Medium
    medSRNOx = np.genfromtxt(path + '/SR_Matrices/Med_NOx.csv', 
    delimiter=',')
    medSRPMVOC = np.genfromtxt(path + '/SR_Matrices/Med_PM_VOC.csv', 
    delimiter=',')
    medSRSO2 = np.genfromtxt(path + '/SR_Matrices/Med_SO2.csv', 
    delimiter=',')
    medSRNH3 = np.genfromtxt(path + '/SR_Matrices/Med_NH3.csv', 
    delimiter=',')

    ## Tall
    tallSRNOx = np.genfromtxt(path + '/SR_Matrices/Tall_NOx.csv', 
    delimiter=',')
    tallSRPMVOC = np.genfromtxt(path + '/SR_Matrices/Tall_PM_VOC.csv', 
    delimiter=',')
    tallSRSO2 = np.genfromtxt(path + '/SR_Matrices/Tall_SO2.csv', 
    delimiter=',')
    tallSRNH3 = np.genfromtxt(path + '/SR_Matrices/Tall_NH3.csv', 
    delimiter=',')

    ## Tall2
    tall2SRNOx = np.genfromtxt(path + '/SR_Matrices/Tall2_NOx.csv', 
    delimiter=',')
    tall2SRPMVOC = np.genfromtxt(path + '/SR_Matrices/Tall2_PM_VOC.csv', 
    delimiter=',')
    tall2SRSO2 = np.genfromtxt(path + '/SR_Matrices/Tall2_SO2.csv', 
    delimiter=',')
    tall2SRNH3 = np.genfromtxt(path + '/SR_Matrices/Tall2_NH3.csv', 
    delimiter=',')

emissionVitalsEntry()
sourceReceptorReadin()

# function to read in other model parameters
# there may be options added here for different damage functions later

def calibrationCoefficientReadin(year):
    global vrmr
    global drAdult
    global drInfant

    vrmr = 9186210
    dradult = 0.005826891
    drInfant = 0.006765865

    global nh4Cal
    global noxCal
    global pm25Cal
    global so4Cal
    global vocCal

    if year == 2008:
        nh4Cal = .3
        noxCal = .52
        pm25Cal = .58
        so4Cal = 1.1
        vocCal = .03
    elif year == 2011:
        nh4Cal = .26
        noxCal = .54
        pm25Cal = .64
        so4Cal = 1.4
        vocCal = .023
    elif year == 2014:
        nh4Cal = .28
        noxCal = .58
        pm25Cal = .72
        so4Cal = 1.52
        vocCal = .02
    else: 
        nh4Cal = .3
        noxCal = .46
        pm25Cal = .76
        so4Cal = 1.54
        vocCal = .04        

calibrationCoefficientReadin(year)

# there is a secondary calibration step to the model that
# I'm skipping for now

#### input secondary calibration here ###

deaths = sum(sum(population * mortality))

def baselineRun():

    # Annual emission to ug/m^3 conversion
    global NH3conv
    global NOxconv
    global SO2conv
    global PMVOCconv

    NH3conv = 1.06 * 28761.72
    NOxconv = 1.35 * 28761.72
    SO2conv = 1.5 * 28761.72
    PMVOCconv = 28761.72

    NH3 = NH3conv * (np.dot(areaSourceEmissions[:, 0],  areaSRNH3) + 
                    np.dot(lowStackEmissions[:, 0],  lowSRNH3) + 
                    np.dot(medStackEmissions[:, 0],  medSRNH3) + 
                    np.dot(tallStackEmissions[:, 0],  tallSRNH3) + 
                    np.dot(tall2StackEmissions[:, 0],  tall2SRNH3))

    NOx = NOxconv * (np.dot(areaSourceEmissions[:, 1],  areaSRNOx) + 
                    np.dot(lowStackEmissions[:, 1],  lowSRNOx) + 
                    np.dot(medStackEmissions[:, 1],  medSRNOx) + 
                    np.dot(tallStackEmissions[:, 1],  tallSRNOx) + 
                    np.dot(tall2StackEmissions[:, 1],  tall2SRNOx))

    PM25p = PMVOCconv * (np.dot(areaSourceEmissions[:, 3],  areaSRPMVOC) + 
                        np.dot(lowStackEmissions[:, 3],  lowSRPMVOC) + 
                        np.dot(medStackEmissions[:, 3],  medSRPMVOC) + 
                        np.dot(tallStackEmissions[:, 3],  tallSRPMVOC) + 
                        np.dot(tall2StackEmissions[:, 3],  tall2SRPMVOC))

    SO2 = SO2conv * (np.dot(areaSourceEmissions[:, 4],  areaSRSO2) + 
                    np.dot(lowStackEmissions[:, 4],  lowSRSO2) + 
                    np.dot(medStackEmissions[:, 4],  medSRSO2) + 
                    np.dot(tallStackEmissions[:, 4],  tallSRSO2) + 
                    np.dot(tall2StackEmissions[:, 4],  tall2SRSO2))

    VOC = PMVOCconv * (np.dot(areaSourceEmissions[:, 5],  areaSRPMVOC) + 
                    np.dot(areaSourceEmissions[:, 6],  areaSRPMVOC) + 
                    np.dot(lowStackEmissions[:, 5],  lowSRPMVOC) + 
                    np.dot(medStackEmissions[:, 5],  medSRPMVOC) + 
                    np.dot(tallStackEmissions[:, 5],  tallSRPMVOC) + 
                    np.dot(tall2StackEmissions[:, 5],  tall2SRPMVOC))

    NH4 = NH3
    NH4e = (NH3 / 18 - 1.5 * SO2 / 96)
    NH4e = NH4e.clip(10**-12)

    HNO3 = NOx/62

    NO3 = 0.6509*(0.33873*HNO3+0.121008*NH4e+ 3.511482*(HNO3*NH4e))*62
    SO4 = 1.375 * SO2

    # compute baseline PM25 concentrations
    PM25b = NO3 + SO4 + VOC + PM25p + NH4

### Matlab Code for what comes next

'''

    run Nitrate_Sulfate_Ammonium

%% Compute concentrations of particulate nitrate, ammonium, and sulfate.
% 18 = MW particulate NH4
% 96 = MW particulate Sulfate
% 0.12028 = (1/8.314)PPM to Mole
% 339.9329 = (101300/298) PPM to Mole
% 0.01595 = 1/MW PNO3 = 62
% 0.00039 = (273K+10C)*(Gaseous Nitric Acid in ug/m^3)/(1,000*(12.187*62))
%   This yields gaseous nitric acid in ppm then coverted to moles as above.

%% Predictions from AP3

NH4(:,1) = (NH3(:,1) + NH3(:,2) + NH3(:,3) + NH3(:,4) + NH3(:,5));
SO4(:,1) = (SO2(:,1) + SO2(:,2) + SO2(:,3) + SO2(:,4) + SO2(:,5));
NH4e(:,1) = (NH4(:,1)./18 - 1.5.*SO4(:,1)./96);
HNO3(:,1) = (NOx(:,1) + NOx(:,2) + NOx(:,3) + NOx(:,4) + NOx(:,5))./62;

HNO3_Base = HNO3;

% Specifications from Charles: Fit 1
NO3(:,1) = 0.6509.*(0.33873.*HNO3+0.121008.*NH4e+ 3.511482.*(HNO3.*NH4e)).*62;

% NO3(:,1) = 0.385.*(exp(0.008267.*LN_HNO3(:,1)) +  (0.178005.*NH4e(:,1))./0.01595);
SO4(:,1) = (1.375.*(SO2(:,1) + SO2(:,2)+ SO2(:,3)+ SO2(:,4) + SO2(:,5)));

% Assemble species into total PM_25
PM_25(:,1) = (NO3(:,1)+SO4(:,1)+A_VOC(:,1)+A_VOC(:,2)+A_VOC(:,3)+A_VOC(:,4) + 
A_VOC(:,5) + B_VOC(:,1)+PM_25_Primary(:,1) +  PM_25_Primary(:,2) + PM_25_Primary(:,3) + 
PM_25_Primary(:,4)+ PM_25_Primary(:,5) + NH4);

    run PM_25_Base_Raw
PM_25_B(:,1) = (NO3(:,1)+SO4(:,1)+A_VOC(:,1)+A_VOC(:,2)+A_VOC(:,3)+A_VOC(:,4) + 
A_VOC(:,5) +B_VOC(:, 1) + PM_25_Primary(:,1) +  PM_25_Primary(:,2) + PM_25_Primary(:,3) + 
PM_25_Primary(:,4)+ PM_25_Primary(:,5)+NH4);

    run PM_25_Health_Base

% Pope, 2002 = 0.005826891 (BENMAP)
% Lepeule, 2012 = 0.01310283

% Mrozek, Taylor: $1,963,840 (2000)
% EPA: $ 7,400,000 (2006)

Cause = 1;

%% BenMAP Form
Deaths = (Mortality{3,1}.*(One'*(1-(1./(exp(DoseResponseAdult.*PM_25_B')))))').*Pop_over_30;

DB = sum(sum(Deaths));
   
Mort = sum(sum(Deaths.*WTP_Mort));

%% BenMAP Form
Infant = (Mortality{3,1}.*(One'*(1-(1./(exp(DoseResponseInfant.*PM_25_B')))))').*Pop_Infant;

Deaths_all=sum(sum(Deaths))+sum(sum(Infant));
Mort_Infant = sum(sum(Infant.*WTP_Mort));

All_Mort{1,1} = (Mort+Mort_Infant);
Damages = [All_Mort{Cause,1}];
B_25_Primary_MD = (sum(sum(Damages)));

clear CB_COI CB Visibility PM_Emission
'''

print( f'Total deaths across the United States in {year}: {deaths:.0f}')
winsound.Beep(800, 200)
