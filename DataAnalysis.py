import pymongo
import re
import datetime


connection = pymongo.MongoClient()

db = connection.twitter

keywords = ['Chikungunya', 'Chikv', 'rash', 'high fever', 'joint pain', 'nausea', 'vomit', 'photophobia', 'arthralgia', 'Dengue', 'flu', 'sick', 'cough']
allValues = []

# keywords = ['Chikungunya']

myFile = open('test1.txt', 'w')

# Starting with Sunday, 1/5/14 @ Date(1388880000000) until week of 1/10/2015 also Sunday
# check the dates given increments of maybe a week? using date manipulation
weekTime = 604800
numWeeks = 54
datenum = 1388880000

# compute
for week in xrange(numWeeks):
	lowDate = datetime.datetime.fromtimestamp(datenum)
	datenum = datenum + weekTime
	highDate = datetime.datetime.fromtimestamp(datenum)
	values = []

	for myKeyword in keywords:
		keyRegex = re.compile("\\b.*" + myKeyword, re.IGNORECASE)
		values.append(db.geoTweets.find({'cr' : {'$gte' : lowDate, '$lte' : highDate}, 'tlt' : {'$exists' : True}, 't' : keyRegex}).count())

	allValues.append(values)

# printouts to file

# headers
myFile.write("\t")
for myKeyword in keywords:
	myFile.write(myKeyword + "\t")
myFile.write("\n")

# reset values
datenum = 1388880000

for week in xrange(numWeeks):
	lowDate = datetime.datetime.fromtimestamp(datenum)
	datenum = datenum + weekTime
	myFile.write(str(lowDate) + "\t")

	for idx in xrange(len(allValues[week])):
		myFile.write(str(allValues[week][idx]) + "\t")
	myFile.write("\n")