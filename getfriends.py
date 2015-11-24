# lists all of a given user's friends (ie, followees)

from twitter import *
import json

# load our API credentials
config = {}
execfile("config.py", config)

# create twitter API object
twitter = Twitter(
        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

# this is the user whose friends we will list
username = "ADssx"

# perform a basic search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/friends/ids
query = twitter.friends.ids(screen_name = username)

# tell the user how many friends we've found.
# note that the twitter API will NOT immediately give us any more 
# information about friends except their numeric IDs...
print "Found %d friends" % (len(query["ids"]))

# now we loop through them to pull out more info, in blocks of 100.
# Returns fully-hydrated user objects for up to 100 users per request
for n in range(0, len(query["ids"]), 100):
    ids = query["ids"][n:n+100]

    # create a subquery, looking up information about these users
    # twitter API docs: https://dev.twitter.com/docs/api/1/get/users/lookup
    subquery = twitter.users.lookup(user_id = ids)

    for user in subquery:
    # now print out user info, starring any users that are verified
        # print " [%s] %s" % ("*" if user["verified"] else " ", user["screen_name"])
        # print "%r" % user
        with open('friendsADssxUser.js', 'w') as outfile:
            json.dump(user, outfile)

    data = json.dumps(subquery, sort_keys=True,indent=4, separators=(',', ': '))

    filename = "friendsADssx.js"
    target = open(filename, 'w')
    target.write(data)
    target.close()

    with open('friendsADssx3.js', 'a') as outfile:
        # outfile.write(data)
        # json.dump(subquery, outfile, sort_keys=True,indent=4, separators=(',', ': '))
        json.dump(subquery, outfile)