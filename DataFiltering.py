


# to dump
mongodump -h mongo-clusterAA5 -d twitter -c geoTweets -q '{t: {$regex : ".*Harvard.*"}}'

mongodump -h mongo-clusterAA5 -d twitter -c geoTweets --query "{'cr':{\$gte: new Date(1415633400000)}}"

mongodump -h mongo-A1 -d twitter -c geoTweets --query "{'tln': { \$lte: -65., \$gte: -68.}, 'tlt': { \$lte: 18.7, \$gte: 17.5}}"


# no plt locations
mongodump -h mongo-A1 -d twitter -c geoTweets --query "{'cr' : {\$gte: new Date(1388534400000)}, 'tln': { \$lte: -65., \$gte: -68.}, 'tlt': { \$lte: 18.7, \$gte: 17.5}}"

# from 1/1/14 all PR both tlt and plt
mongodump -h mongo-A1 -d twitter -c geoTweets --query "{'cr' : {\$gte: new Date(1388534400000)}, \$or: [ { 'tln': { \$lte: -65., \$gte: -68.}, 'tlt': { \$lte: 18.7, \$gte: 17.5} }, { 'pln': { \$lte: -65., \$gte: -68.}, 'plt': { \$lte: 18.7, \$gte: 17.5} } ] }"

# dump the local one for Chikungunya keywords only

mongodump -o "C:/dump1" -d twitter -c geoTweets --query "{'t' : /\\\bChikungunya\\\b/i}"


mongorestore dump/twitter # once the dump is in the mongo bin folder in program files

# 1/1/14, Wednesday
# 1388534400000

# 1/5/14, Sunday
# 1388880000000

# each week is
# 604800000



{ tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }
{ pln: { $lte: -65., $gte: -68.}, plt: { $lte: 18.7, $gte: 17.5} }

{ $or: [ { tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }, { pln: { $lte: -65., $gte: -68.}, plt: { $lte: 18.7, $gte: 17.5} } ] }


{cr : {$gte: new Date(1415633400000)}, tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5}}

{cr : {$gte: new Date(1415633400000)}, $or: [ { tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }, { pln: { $lte: -65., $gte: -68.}, plt: { $lte: 18.7, $gte: 17.5} } ] }



db.geoTweets.find({ tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }).pretty()

db.geoTweets.find({cr : {$gte: new Date(1415633400000)}, $or: [ { tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }, { pln: { $lte: -65., $gte: -68.}, plt: { $lte: 18.7, $gte: 17.5} } ] }
).pretty()

db.geoTweets.find({tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5}}).explain()


db.geoTweets.find({cr : {$gte: new Date(1415633400000)}, $or: [ { tln: { $lte: -65., $gte: -68.}, tlt: { $lte: 18.7, $gte: 17.5} }, { pln: { $lte: -65., $gte: -68.}, plt: { $lte: 18.7, $gte: 17.5} } ] }).count()

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