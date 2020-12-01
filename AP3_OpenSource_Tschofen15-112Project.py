import numpy as np
import tkinter, winsound

#import pandas as pd
#import scipy.io as sio
#from os.path import dirname, join as pjoin

path='C:/Users/ptsch/Box/AP3_Open_Access_Model/Course_Project/Model_Components'

# function that prompts user to type in year for reading in emissions,
# stores year as a variable for other functions 
def emissionVitalsEntry():
    global year
    global areaSources
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
    areaSources = np.genfromtxt(path + '/Emissions/area_sources_' + year +
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
    global vrmr = 9186210
    global drAdult = 0.005826891
    global drInfant = 0.006765865
    if year == 2008:
        global nh4Cal = .3
        global noxCal = .52
        global pm25Cal = .58
        global so4Cal = 1.1
        global vocCal = .03
    elif year == 2011:
        global nh4Cal = .26
        global noxCal = .54
        global pm25Cal = .64
        global so4Cal = 1.4
        global vocCal = .023
    elif year == 2014:
        global nh4Cal = .28
        global noxCal = .58
        global pm25Cal = .72
        global so4Cal = 1.52
        global vocCal = .02
    else: 
        global nh4Cal = .3
        global noxCal = .46
        global pm25Cal = .76
        global so4Cal = 1.54
        global vocCal = .04        

calibrationCoefficientReadin(year)


# there is a secondary calibration step to the model that
# I'm skipping for now

#### input secondary calibration here ###



deaths = population * mortality

winsound.Beep(800, 200)
