import pymongo
import re
import datetime


connection = pymongo.MongoClient()

db = connection.twitter

myFile = open('totalTweets.txt', 'w')

# Starting with Sunday, 1/5/14 @ Date(1388880000000) until week of 1/10/2015 also Sunday
# check the dates given increments of maybe a week? using date manipulation
weekTime = 604800
numWeeks = 54
datenum = 1388880000

allValues = []

# compute
for week in xrange(numWeeks):
	lowDate = datetime.datetime.fromtimestamp(datenum)
	datenum = datenum + weekTime
	highDate = datetime.datetime.fromtimestamp(datenum)

	myCount = db.geoTweets.find({'cr' : {'$gte' : lowDate, '$lte' : highDate}}).count()
	allValues.append(myCount)

# printouts to file

# headers
myFile.write("\t")
myFile.write("Total Tweet Count\n")

# reset values
datenum = 1388880000

for week in xrange(numWeeks):
	lowDate = datetime.datetime.fromtimestamp(datenum)
	datenum = datenum + weekTime
	myFile.write(str(lowDate) + "\t")
	myFile.write(str(allValues[week]))
	myFile.write("\n")