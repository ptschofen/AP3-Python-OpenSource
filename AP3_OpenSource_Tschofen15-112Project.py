import numpy as np
import tkinter, winsound, time, multiprocessing

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
    drAdult = 0.005826891
    drInfant = 0.006765865

    global nh4Cal
    global noxCal
    global pm25Cal
    global so4Cal
    global vocCal

    if year == '2008':
        nh4Cal = .3
        noxCal = .52
        pm25Cal = .58
        so4Cal = 1.1
        vocCal = .03
    elif year == '2011':
        nh4Cal = .26
        noxCal = .54
        pm25Cal = .64
        so4Cal = 1.4
        vocCal = .023
    elif year == '2014':
        nh4Cal = .28
        noxCal = .58
        pm25Cal = .72
        so4Cal = 1.52
        vocCal = .02
    else: 
        nh4Cal = .24
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
    tic = time.perf_counter()
    # Annual emission to ug/m^3 conversion
    global nh3Conv
    global noxConv
    global pmvocConv
    global so2Conv

    nh3Conv = 1.06 * 28761.72
    noxConv = 1.35 * 28761.72
    so2Conv = 1.5 * 28761.72
    pmvocConv = 28761.72

    global NH3
    global NOx
    global PM25p
    global SO2
    global VOC
    NH3 = nh3Conv * nh4Cal * (np.dot(areaSourceEmissions[:, 0], areaSRNH3) + 
                              np.dot(lowStackEmissions[:, 0], lowSRNH3) + 
                              np.dot(medStackEmissions[:, 0], medSRNH3) + 
                              np.dot(tallStackEmissions[:, 0], tallSRNH3) + 
                              np.dot(tall2StackEmissions[:, 0],tall2SRNH3))

    NOx = noxConv * noxCal * (np.dot(areaSourceEmissions[:, 1], areaSRNOx) + 
                              np.dot(lowStackEmissions[:, 1], lowSRNOx) + 
                              np.dot(medStackEmissions[:, 1], medSRNOx) + 
                              np.dot(tallStackEmissions[:, 1], tallSRNOx) + 
                              np.dot(tall2StackEmissions[:, 1],tall2SRNOx))

    PM25p=pmvocConv*pm25Cal * (np.dot(areaSourceEmissions[:, 3], areaSRPMVOC) + 
                               np.dot(lowStackEmissions[:, 3], lowSRPMVOC) + 
                               np.dot(medStackEmissions[:, 3], medSRPMVOC) + 
                               np.dot(tallStackEmissions[:, 3], tallSRPMVOC) + 
                               np.dot(tall2StackEmissions[:, 3], tall2SRPMVOC))

    SO2 = so2Conv * so4Cal * (np.dot(areaSourceEmissions[:, 4], areaSRSO2) + 
                              np.dot(lowStackEmissions[:, 4], lowSRSO2) + 
                              np.dot(medStackEmissions[:, 4], medSRSO2) + 
                              np.dot(tallStackEmissions[:, 4], tallSRSO2) + 
                              np.dot(tall2StackEmissions[:, 4], tall2SRSO2))

    VOC = pmvocConv * vocCal * (np.dot(areaSourceEmissions[:, 5], areaSRPMVOC) + 
                                np.dot(areaSourceEmissions[:, 6], areaSRPMVOC) + 
                                np.dot(lowStackEmissions[:, 5], lowSRPMVOC) + 
                                np.dot(medStackEmissions[:, 5], medSRPMVOC) + 
                                np.dot(tallStackEmissions[:, 5], tallSRPMVOC) + 
                                np.dot(tall2StackEmissions[:, 5],tall2SRPMVOC))

    global NH4
    global NH4e
    global HNO3
    global NO3
    global SO4

    NH4 = NH3
    NH4e = (NH3 / 18 - 1.5 * SO2 / 96)
    NH4e = NH4e.clip(10**-12)

    HNO3 = NOx/62

    NO3 = 0.6509*(0.33873*HNO3+0.121008*NH4e+ 3.511482*(HNO3*NH4e))*62
    SO4 = 1.375 * SO2

    # compute baseline PM25 concentrations
    global PM25b
    PM25b = NO3 + SO4 + VOC + PM25p + NH4

    adultMort = mortality[:, 7:18]
    adultImpact = 1-(1/(np.exp(drAdult*PM25b)))
    adultExposure = population[:, 7:18]
    
    infantMort = mortality[:, 1]
    infantImpact = 1-(1/(np.exp(drInfant*PM25b)))
    infantExposure = population[:, 1]

    adultDeaths = (adultMort * 
                   np.repeat(adultImpact, 11).reshape(3109, 11) * 
                   adultExposure)
    infantDeaths = (infantMort * 
                   infantImpact * 
                   infantExposure)
    
    global totalDeaths
    totalDeaths = sum(sum(adultDeaths)) + sum(infantDeaths)

    #print(f'Deaths for age groups in 5-year intervals: {sum(adultDeaths)}')

    damageInfants = sum(infantDeaths) * vrmr
    damageAdults =  sum(sum(adultDeaths)) * vrmr
    
    global damageTotal
    damageTotal = damageInfants + damageAdults

    infDmgReport = damageInfants/10**9
    aduDmgReport = damageAdults/10**9
    
    global totDmgReport
    totDmgReport = infDmgReport + aduDmgReport

    print(f'Damages --- Infants: {infDmgReport:.0f} $billion, ' +
    f'Adults: {aduDmgReport:.0f} $billion, ' +
    f'Total: {totDmgReport} $billion (2018 prices)')

    toc = time.perf_counter()
    print(f"Performed baseline run in {toc - tic:0.4f} seconds")

baselineRun()
# print(PM25b)

print( f'Total deaths across the United States in {year}: {deaths:.0f}')
print( f'Total deaths attributable to air pollution: {totalDeaths:.0f}')
print(f'Total monetary damages from air pollution: {totDmgReport:.0f} $billion')
#print( f'Among those: Infants: {infantDeaths}; Adults: {adultDeaths}')
winsound.Beep(800, 200)
