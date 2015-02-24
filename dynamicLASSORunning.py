import numpy as np
import pandas as pd
from sklearn.linear_model import LassoCV
from sklearn import cross_validation

# data format:
# no row headers
# column headers
# last row is target

# start 6/15 as first week with data
start = 0
#size = 8
#end = start+size

# read in file
numbersData = pd.read_csv('numbersLagged.csv', index_col = 0)
print "data" + str(numbersData.shape)
# set up dynamic prediction list
numbersResult = []
# set up coef used list
myCoefs = []

for end in xrange(3,numbersData.shape[0]):
	print end
	# use size rows before it to train
	kf = cross_validation.KFold(end-start, n_folds = 3, shuffle = True)
	lasso = LassoCV(cv=kf, n_jobs=-1, positive=True)
	# features is up to last column, target in last column
	lassofit = lasso.fit(numbersData.ix[start:end,:-1], numbersData.ix[start:end,-1])
	myCoefs.append(lassofit.coef_)

	# predict next
	numbersResult.append(lassofit.predict(numbersData.ix[end,:-1]))

#set up outfile
outFile = open('dynamicLassoRunning.txt', 'w')

# write headers
outFile.write('Predicted\tReal\n')

for i in xrange(len(numbersResult)):
	outFile.write(str(numbersResult[i]))
	outFile.write("\t")
	outFile.write(str(numbersData.ix[i+3,-1]))
	outFile.write("\n")

# write coefficients over time starting from first widow
coefOutFile = open('dynamicLassoRunningCoefs.txt', 'w')

for i in xrange(numbersData.shape[1]):
	coefOutFile.write(str(numbersData.columns[i]))
	coefOutFile.write("\t")

coefOutFile.write("\n")

for i in xrange(len(myCoefs)):
	for j in xrange(len(myCoefs[i])):
		coefOutFile.write(str(myCoefs[i][j]))
		coefOutFile.write('\t')
	coefOutFile.write('\n')