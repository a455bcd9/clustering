import sys
import json
from math import sqrt
import random

# Load input JSON file containing Twitter friends entries.  
input = open(sys.argv[1])
lines = []
for line in input:
    data = json.loads(line)
    for x in data:
       description = str(x['description']).split()
       print x['name']
       apple = [x['name'], x['followers_count'], x['favourites_count']]
       lines.append(apple)