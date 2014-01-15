from pymongo.mongo_replica_set_client import MongoReplicaSetClient
from pymongo.read_preferences import ReadPreference

from datetime import datetime

# Define seedlist of replicaset members
rsc = MongoReplicaSetClient(
	'r1,r2,r3',
	replicaset='bcdo',
	read_preference=ReadPreference.SECONDARY,
	tag_sets = [{'dc':'pa', 'env':'production'}, {'dc':'nj', 'dc':'production'}]
)

db = rsc.bcdo

smalley = {"name": "Michael Smalley", "likes": ["video games", "asterisk", "flag football", "meetups"], "last_attended": datetime(2013, 11, 15, 18, 00)}

print "If Michael Smalley is here then we should add him to the list of attendees..."
db.attendees.insert(smalley)
print
print "Since Pete's here we should add that he likes Ruby, too..."
db.attendees.update({'name':'Peter Shannon'}, {'$addToSet':{'likes':'ruby'}})
print
print "...and since everyone is here tonight we should update the last_attended field"
db.attendees.update({}, {'$set': {'last_attended': datetime(2014, 1, 15, 18, 00)}}, multi=True)