import pymongo
import re
import datetime


connection = pymongo.MongoClient()

db = connection.twitter

myFile = open('visDataNoProfileGPS.txt', 'w')

keyRegex = re.compile("\\b" + 'Chikungunya' + "\\b", re.IGNORECASE)

counter = 0
# printouts to file
for tweet in db.geoTweets.find({'t': keyRegex, 'tlt' : {'$exists' : True}, 'tln' : {'$exists' : True}})[:]:
	counter += 1
	print counter
	myFile.write(str(tweet['cr']))
	myFile.write("\t")
	myFile.write(str(tweet['tlt']))
	myFile.write("\t")
	myFile.write(str(tweet['tln']))
	myFile.write("\n")

# printouts to file
#for tweet in db.geoTweets.find({'t': keyRegex, 'tlt' : {'$exists' : False}, 'tln' : {'$exists' : False}, 'plt' : {'$exists' : True}, 'pln' : {'$exists' : True}})[:]:
#	counter += 1
#	print counter
#	myFile.write(str(tweet['cr']))
#	myFile.write("\t")
#	myFile.write(str(tweet['plt']))
#	myFile.write("\t")
#	myFile.write(str(tweet['pln']))
#	myFile.write("\n")