import numpy as np
import pandas as pd
from sklearn.linear_model import LassoCV
from sklearn import cross_validation

# data format:
# no row headers
# column headers
# last row is target

# start 6/15 as first week with data
start = 7
end = 17

# read in file
numbersData = pd.read_csv('numbersLaggedFull.csv', index_col = 0)
print "data" + str(numbersData.shape)
# set up dynamic prediction list
numbersResult = []

# use i before it
kf = cross_validation.KFold(end-start, n_folds = 3, shuffle = True)
lasso = LassoCV(cv=kf, n_jobs=-1, positive=True)
# features is up to last column, target in last column
lassofit = lasso.fit(numbersData.ix[start:end,:-1], numbersData.ix[start:end,-1])
print lassofit.coef_

for i in xrange(end-start):
	# predict the next
	numbersResult.append(lassofit.predict(numbersData.ix[start+i,:-1]))

#set up outfile
outFile = open('staticLassoFullPeak.txt', 'w')

# write headers
outFile.write('Predicted\tReal\n')

for i in xrange(end-start):
	outFile.write(str(numbersResult[i]))
	outFile.write("\t")
	outFile.write(str(numbersData.ix[start+i,-1]))
	outFile.write("\n")

# write coef labels
for i in xrange(numbersData.shape[1]):
	outFile.write(str(numbersData.columns[i]))
	outFile.write("\t")

outFile.write("\n")

for i in xrange(len(lassofit.coef_)):
	outFile.write(str(lassofit.coef_[i]))
	outFile.write('\t')