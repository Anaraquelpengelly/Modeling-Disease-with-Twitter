import pymongo
import datetime

# Connect to client
client = pymongo.MongoClient('mongo-clusterAA5/twitter')'
db = client.test

# Enter as if we had run "mongo mongo-clusterAA5/twitter"
db.setSlaveOk(true)
db.geoTweets.find(
    {
        t : {
            $regex : /.*Harvard.*/i
        }
    }
).pretty()


# how to subset and save the results of this
db.geoPRTweets = db.geoTweets.find(
   {
     loc: {
       $geoWithin: {
          $geometry: {
             type : "Box" ,
             coordinates: [ [ [ 0, 0 ], [ 3, 6 ], [ 6, 1 ], [ 0, 0 ] ] ]
          }
       }
     }
   }
)