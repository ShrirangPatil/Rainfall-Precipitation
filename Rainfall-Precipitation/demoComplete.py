import csv
from numpy import *
#from scipy.interpolate import *
from matplotlib.pyplot import *
#from scipy.stats import *
#import math
set_printoptions(threshold= np.nan)
file = open("ChikmagalurRainTrain.csv")# opening the learning data
reader = csv.reader(file)# creating a reader
flag = 0# for avoiding the headers in csv file from including in arrays
dataRain = array([])# stores the annual rain data
dataYear = array([])# correspnding year
for i in reader:
    if flag == 0:
        flag = 1
    else:
        for j in range(1,13):
            if flag == 1:
                startYearOfTestDataTrain = int(i[0])
                flag = 2
            dataYear = append(dataYear,int(i[0])+(int(i[0])*(j-1))/12)#taking years like for jan 1900 + (1900*0)/12 for feb 1900 + (1900*1)/12
            dataRain = append(dataRain,float(i[j]))
#print("Data Year","Data Rain")
#for i in range(len(dataYear)):
    #print(dataYear[i],dataRain[i])
year = (1920 - startYearOfTestDataTrain)*12
#print(year)
#print(dataRain[year:year+13])
p1 = polyfit(dataYear,dataRain,8)# fitting the data into a quadratic polynomial
plot(dataYear[year:year+13],dataRain[year:year+13],'o')# plotting the actual rain data on graph as blue dots
plot(dataYear[year:year+13],polyval(p1,dataYear[year:year+13]),'r-')# drawing a curve formed by polynomial
xlabel("Years"+str(year/12+startYearOfTestDataTrain))
ylabel("RainFall")
title("Prototype1")
#print(dataYear[year],dataRain[year],polyval(p1,dataYear[year]),sep = " ")
show()


file.close()

testDataYear = array([])# stores the test data years
testDataRain = array([])# stores the test data rain
file = open("ChikmagalurRainTest.csv")
reader = csv.reader(file)
flag1 = 0
for i in reader:
    for j in range(1,13):
            testDataYear = append(testDataYear,int(i[0])+(int(i[0])*(j-1))/12)
            testDataRain = append(testDataRain,float(i[j]))
            if flag1 == 0:
                startYearOfTestData = int(i[0])
                flag1 = 1
#print(startYearOfTestData)
#for i in range(len(testDataYear)):
    #print(testDataYear[i],testDataRain[i])
#predictedData = p1[0] * testDataYear**3 + p1[1] * testDataYear**2 + p1[2] * testDataYear + p1[3]
#predictedData = p1[0] * testDataYear**4 + p1[1] * testDataYear**3 + p1[2] * testDataYear**2 + p1[3] * testDataYear + p1[4]
#predictedData = p1[0] * testDataYear**5 + p1[1] * testDataYear**4 + p1[2] * testDataYear**3 + p1[3] * testDataYear**2 + p1[4] * testDataYear + p1[5]
#predictedData = p1[0] * testDataYear**6 + p1[1] * testDataYear**5 + p1[2] * testDataYear**4 + p1[3] * testDataYear**3 + p1[4] * testDataYear**2 + p1[5] * testDataYear + p1[6]
#predictedData = p1[0] * testDataYear**7 + p1[1] * testDataYear**6 + p1[2] * testDataYear**5 + p1[3] * testDataYear**4 + p1[4] * testDataYear**3 + p1[5] * testDataYear**2 + p1[6] * testDataYear + p1[7]
predictedData = p1[0] * testDataYear**8 + p1[1] * testDataYear**7 + p1[2] * testDataYear**6 + p1[3] * testDataYear**5 + p1[4] * testDataYear**4 + p1[5] * testDataYear**3 + p1[6] * testDataYear**2 + p1[7] * testDataYear + p1[8]
#predictedData = p1[0] * testDataYear**9 + p1[1] * testDataYear**8 + p1[2] * testDataYear**7 + p1[3] * testDataYear**6 + p1[4] * testDataYear**5 + p1[5] * testDataYear**4 + p1[6] * testDataYear**3 + p1[7] * testDataYear**2 + p1[8] * testDataYear + p1[9]
#predictedData = p1[0] * testDataYear**14 + p1[1] * testDataYear**13 + p1[2] * testDataYear**12 + p1[3] * testDataYear**11 + p1[4] * testDataYear**10 + p1[5] * testDataYear**9 + p1[6] * testDataYear**8 + p1[7] * testDataYear**7 + p1[8] * testDataYear**6 + p1[9] * testDataYear**5 + p1[10] * testDataYear**4 + p1[11] * testDataYear**3 + p1[12] * testDataYear**2 + p1[13] * testDataYear + p1[14]
#predictedData = p1[0] * testDataYear**2 + p1[1] * testDataYear + p1[2]# stores the predicted rain data
#predictedData = p1[0] * testDataYear**3 + p1[1] * testDataYear**2 + p1[2] * testDataYear + p1[3]
print("Year"+"\t"+"Month"+"Actual Rain"+"\t"+"Predicted Rain")

#for i in range(testDataYear.size):
    #print(testDataYear[i],"\t",testDataRain[i],"\t",predictedData[i])
year = (2004 - startYearOfTestData)*12
temp = startYearOfTestData
i = 0
print(predictedData[year:year+13])
while i < int(testDataRain.size):
    for j in range(1,13):
        if predictedData[i]<0:
            predictedData[i] = 0
        print(startYearOfTestData,j,"\t\t",testDataRain[i],"\t\t",predictedData[i])
        i+=1
    startYearOfTestData+=1

plot(testDataYear[year:year+13],testDataRain[year:year+13],'r--')# actual curve
plot(testDataYear[year:year+13],predictedData[year:year+13],"b--")# predicted curve
xlabel("Years"+str(year/12+temp))
ylabel("RainFall")
title("Prototype1")
show()

#rainfit = p1[0] * dataYear**2 + p1[1] * dataYear + p1[2]
#rainfit = p1[0] * dataYear**3 + p1[1] * dataYear**2 + p1[2] * dataYear + p1[3]
#rainfit = p1[0] * dataYear**4 + p1[1] * dataYear**3 + p1[2] * dataYear**2 + p1[3] * dataYear + p1[4]
#rainfit = p1[0] * dataYear**5 + p1[1] * dataYear**4 + p1[2] * dataYear**3 + p1[3] * dataYear**2 + p1[4] * dataYear + p1[5]
#rainfit = p1[0] * dataYear**6 + p1[1] * dataYear**5 + p1[2] * dataYear**4 + p1[3] * dataYear**3 + p1[4] * dataYear**2 + p1[5] * dataYear + p1[6]
#rainfit = p1[0] * dataYear**7 + p1[1] * dataYear**6 + p1[2] * dataYear**5 + p1[3] * dataYear**4 + p1[4] * dataYear**3 + p1[5] * dataYear**2 + p1[6] * dataYear + p1[7]
rainfit = p1[0] * dataYear**8 + p1[1] * dataYear**7 + p1[2] * dataYear**6 + p1[3] * dataYear**5 + p1[4] * dataYear**4 + p1[5] * dataYear**3 + p1[6] * dataYear**2 + p1[7] * dataYear + p1[8]
#rainfit = p1[0] * dataYear**9 + p1[1] * dataYear**8 + p1[2] * dataYear**7 + p1[3] * dataYear**6 + p1[4] * dataYear**5 + p1[5] * dataYear**4 + p1[6] * dataYear**3 + p1[7] * dataYear**2 + p1[8] * dataYear + p1[9]
#rainfit = p1[0] * dataYear**14 + p1[1] * dataYear**13 + p1[2] * dataYear**12 + p1[3] * dataYear**11 + p1[4] * dataYear**10 + p1[5] * dataYear**9 + p1[6] * dataYear**8 + p1[7] * dataYear**7 + p1[8] * dataYear**6 + p1[9] * dataYear**5 + p1[10] * dataYear**4 + p1[11] * dataYear**3 + p1[12] * dataYear**2 + p1[13] * dataYear + p1[14]
yresid = dataRain - rainfit
SSresid = sum(pow(yresid,2))
SStotal = len(dataRain)*var(dataRain)
rsq = 1- SSresid/SStotal
print(rsq)
#x = 2017+(2017*8)/12
#jan2018Rainfall = p1[0] * x**8 + p1[1] * x**7 + p1[2] * x**6 + p1[3] * x**5 + p1[4] * x**4 + p1[5] * x**3 + p1[6] * x**2 + p1[7] * x + p1[8]
#print(jan2018Rainfall)
