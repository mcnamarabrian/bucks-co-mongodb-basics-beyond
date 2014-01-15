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

# Looks an aweful lot like the Javascript shell find syntax
print "Who likes Meetups?"
meetup_likers = db.attendees.find({'likes':'meetups'},{'name':1})

for person in meetup_likers:
	print '%s likes Meetups!' % (person.get('name'))

# Let's look for people that haven't been to a Bucks Co DevOps Meetup since 2013 Jun 01
print
print "Who hasn't been here in some time?"
target_date = datetime(2013, 6, 1, 0)
been_some_time = db.attendees.find({'last_attended': {"$lt": target_date}}, {'name':1, 'last_attended':1})

for person in been_some_time:
	print '%s (Last attended: %s)' % (person.get('name'), person.get('last_attended'))

# Let's use regular expressions in our find!
print
print "Who's name starts with a B?  They must be good people..."
b_people = db.attendees.find({'name': {'$regex':'^B'}})

for person in b_people:
	print '%s' % (person.get('name'))
