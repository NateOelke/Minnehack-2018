import csv
import numpy as np

cvdata = np.loadtxt('exampledata_val.csv', delimiter=',')
predictdata = np.loadtxt('exampledata_val_predictions.csv', delimiter=',')

squarediffs = 0
naive = 0
l = 0
avg = np.mean(cvdata[:,42])
for i in range(0,cvdata.shape[0]):
    squarediffs = squarediffs + (cvdata[i][42] - predictdata[i])**2
    naive = naive + (cvdata[i][42] - avg)**2
    l = l + 1
squarediffs = (squarediffs/l)**0.5
naive = (naive/l)**0.5
print(squarediffs)
print(naive)