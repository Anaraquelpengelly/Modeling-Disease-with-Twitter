import pymongo
import re
import datetime


connection = pymongo.MongoClient()

db = connection.twitter

keywords = ['Chikungunya']
datedValues = []

myFile = open('twitterTextByDate.txt', 'w')

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
		keyRegex = re.compile("\\b" + myKeyword, re.IGNORECASE)
		values.append(db.geoTweets.find({'cr' : {'$gte' : lowDate, '$lte' : highDate}, 't' : keyRegex}))

	datedValues.append(values)

# printouts to file

# reset values
datenum = 1388880000

for week in xrange(numWeeks):
	lowDate = datetime.datetime.fromtimestamp(datenum)
	datenum = datenum + weekTime
	myFile.write(str(lowDate) + "\t")

	for idx in xrange(len(datedValues[week])):
		for tweet in datedValues[week][idx]:
			# just write the first text
			myFile.write(tweet['t'].encode('ascii', 'ignore'))

			break
		myFile.write("\n")
		break
