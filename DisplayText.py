import pymongo
import re
import datetime


connection = pymongo.MongoClient()

db = connection.twitter

myFile = open('twitterText.txt', 'w')

keyRegex = re.compile("\\b" + 'Chikungunya' + "\\b", re.IGNORECASE)

# printouts to file
for tweet in db.geoTweets.find({'t' : keyRegex})[:]:

	myFile.write(tweet['t'].encode('ascii', 'ignore'))
	myFile.write("\n")