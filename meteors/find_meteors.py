import math
import requests

def calc_dist(lat1, lon1, lat2, lon2):

	# distance between latitudes
	# and longitudes
	dLat = (lat2 - lat1) * math.pi / 180.0
	dLon = (lon2 - lon1) * math.pi / 180.0

	# convert to radians
	lat1 = (lat1) * math.pi / 180.0
	lat2 = (lat2) * math.pi / 180.0

	# apply formulae
	a = (pow(math.sin(dLat / 2), 2) +
		pow(math.sin(dLon / 2), 2) *
			math.cos(lat1) * math.cos(lat2));
	rad = 6371
	c = 2 * math.asin(math.sqrt(a))
	return rad * c

#get_dist
def get_dist(meteor):
	return meteor.get('distance',math.inf)

my_loc = (19.283160,72.879900)

meteor_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
meteor_data = meteor_resp.json()

for meteor in meteor_data:
	if not ('reclat' in meteor and 'reclong' in meteor): continue
	meteor['distance'] = calc_dist(float(meteor['reclat']),float(meteor['reclong']),my_loc[0],my_loc[1])


meteor_data.sort(key=get_dist) # note function is passed instead of return values

print(meteor_data[0:10])
