import pymongo

# how to connect to "mongo mongo-clusterAA5/twitter"
client = pymongo.MongoClient()
db = client.test

# Enter as if we had run "mongo mongo-clusterAA5/twitter"
db.setSlaveOk(true)
var tempTest = db.geoTweets.find(
    {
        t : {
            $regex : /.*st.*/
        }
    }
).pretty()

# sort by date
db.geoTweets.find().sort({"cr":-1})


# tln, tlt order where ln runs north to south and thus has increments of W/E
# lower left bound is 68W, 17.5N, top right bound is 65W, 18.7N
# from http://docs.mongodb.org/manual/reference/operator/query/geoWithin/
var prTweets = db.geoTweets.find( 
    {
    loc: {
        $geoWithin: {
            $box: [
                [-68, 17.5],
                [-65, 18.7]
            ]
        }
    }
)


# TODO:     create a 2dsphere index as per http://docs.mongodb.org/manual/tutorial/build-a-2dsphere-index/