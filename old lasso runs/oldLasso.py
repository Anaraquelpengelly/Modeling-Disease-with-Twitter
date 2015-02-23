import numpy as np
import pandas as pd
from sklearn.linear_model import LassoCV
from sklearn import cross_validation

# data format:
# no row headers
# column headers
# last row is target

# 49 by 19
# sandbox!
# print inData.ix[:3, -1:].as_matrix()
#print (inData.loc[inData.index[:3]][-1:]).as_matrix()


start = 22

# read in file
numbersData = pd.read_csv('test.csv', index_col = 0)
print "data" + str(numbersData.shape)
# set up dynamic prediction list
numbersResult = []

# don't run for last row
for i in xrange(start+3, numbersData.shape[0]-1):
	print i
	# use i before it
	kf = cross_validation.KFold(i-start, n_folds = 3, shuffle = True)
	lasso = LassoCV(cv=kf, n_jobs=-1, positive=True)
	# features is up to last column, target in last column
	lassofit = lasso.fit(numbersData.ix[start:i,:-1], numbersData.ix[start:i,-1])
	print lassofit.coef_

	# predict the ith index (which is the i+1 due to 0-indexing)
	numbersResult.append(lassofit.predict(numbersData.ix[i,:-1]))

# read in file
numbersLaggedData = pd.read_csv('numbersForLassoLagged2.csv', index_col = 0)
print "lagged" + str(numbersLaggedData.shape)
# set up dynamic prediction list
numbersLaggedResult = []

# don't run for last row
for i in xrange(start+3, numbersLaggedData.shape[0]-1):
	print i
	# use i before it
	kf = cross_validation.KFold(i-start, n_folds = 3, shuffle = True)
	lasso = LassoCV(cv=kf, n_jobs=-1, positive=True)
	# features is up to last column, target in last column
	lassofit = lasso.fit(numbersLaggedData.ix[start:i,:-1], numbersLaggedData.ix[start:i,-1])
	# predict the ith index (which is the i+1 due to 0-indexing)
	numbersLaggedResult.append(lassofit.predict(numbersLaggedData.ix[i,:-1]))


# read in file
ratiosData = pd.read_csv('ratiosForLasso2.csv', index_col = 0)

# set up dynamic prediction list
ratiosResult = []

# don't run for last row
for i in xrange(start+3, ratiosData.shape[0]-1):
	print i
	# use i before it
	kf = cross_validation.KFold(i-start, n_folds = 3, shuffle = True)
	lasso = LassoCV(cv=kf, n_jobs=-1, positive=True)
	# features is up to last column, target in last column
	lassofit = lasso.fit(ratiosData.ix[start:i,:-1], ratiosData.ix[start:i,-1])
	# predict the ith index (which is the i+1 due to 0-indexing)
	ratiosResult.append(lassofit.predict(ratiosData.ix[i,:-1]))

# read in file
ratiosLaggedData = pd.read_csv('ratiosForLassoLagged2.csv', index_col = 0)

# set up dynamic prediction list
ratiosLaggedResult = []

# don't run for last row
for i in xrange(start+3, ratiosLaggedData.shape[0]-1):
	print i
	# use i before it
	kf = cross_validation.KFold(i-start, n_folds = 3, shuffle = True)
	lasso = LassoCV(cv=kf, n_jobs=-1, positive=True)
	# features is up to last column, target in last column
	lassofit = lasso.fit(ratiosLaggedData.ix[start:i,:-1], ratiosLaggedData.ix[start:i,-1])
	# predict the ith index (which is the i+1 due to 0-indexing)
	ratiosLaggedResult.append(lassofit.predict(ratiosLaggedData.ix[i,:-1]))

# set up outfile
outFile = open('dynamicPredictions.txt', 'w')

# write headers
outFile.write('Numbers\tRatios\tNumbersLagged\tRatiosLagged\n')

# write all data (lagged will have one less row)
for i in xrange(len(numbersResult)):

	outFile.write(str(numbersResult[i]))
	outFile.write('\t')
	outFile.write(str(ratiosResult[i]))
	outFile.write('\t')

	# lagged data has one less row
	if i == len(numbersLaggedResult):
		outFile.write('\n')
		continue

	outFile.write(str(numbersLaggedResult[i]))
	outFile.write('\t')
	outFile.write(str(ratiosLaggedResult[i]))
	outFile.write('\n')