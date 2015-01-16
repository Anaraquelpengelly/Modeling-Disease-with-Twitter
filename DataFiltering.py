


# to dump
mongodump -h mongo-clusterAA5 -d twitter -c geoTweets -q '{t: {$regex : ".*Harvard.*"}}'

mongodump -h mongo-clusterAA5 -d twitter -c geoTweets --query "{'cr':{\$gte: new Date(1415633400)}}"



{ tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }
{ pln: { $lte: -65., $gte: -68.}, plt: { $lte: 18.7, $gte: 17.5} }

{ $or: [ { tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }, { pln: { $lte: -65., $gte: -68.}, plt: { $lte: 18.7, $gte: 17.5} } ] }


{cr : {$gte: new Date(1415633400000)}, $or: [ { tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }, { pln: { $lte: -65., $gte: -68.}, plt: { $lte: 18.7, $gte: 17.5} } ] }



db.geoTweets.find({ tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }).pretty()

db.geoTweets.find({cr : {$gte: new Date(1415633400000)}, $or: [ { tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }, { pln: { $lte: -65., $gte: -68.}, plt: { $lte: 18.7, $gte: 17.5} } ] }
).pretty()


import pymongo

# how to connect to "mongo mongo-clusterAA5/twitter"
client = pymongo.MongoClient()
db = client.test

# Enter as if we had run "mongo mongo-clusterAA5/twitter"

# find any occurance one method
db.setSlaveOk(true)
db.geoTweets.find(
    {
        t : {
            $regex : /.*st.*/
        }
    }
).pretty()

# find by date

db.geoTweets.find({
    "cr" : {"$gte": new Date("2014-11-10T15:30:00.000Z")}
})

# unix timestamp in milliseconds
db.geoTweets.find({
    "cr" : {"$gte": new Date(1415633400000)}
}).pretty()

1415633400000
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