# import the necessary packages
from requests import exceptions
import argparse
import requests
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required=True, help="search query to search Bing Image API for")
ap.add_argument("-o", "--output", required=True, help="path to output directory of images")
args = vars(ap.parse_args())

API_KEY = "e03905dd934649659931be63098e10a3"
MAX_RESULTS = 1000
GROUP_SIZE = 50
 
# set the endpoint API URL
URL = "https://api.cognitive.microsoft.com/bing/v5.0/images/search"

EXCEPTIONS = set([IOError, FileNotFoundError,
	exceptions.RequestException, exceptions.HTTPError,
	exceptions.ConnectionError, exceptions.Timeout, exceptions.SSLError])

# store the search term in a convenience variable then set the
# headers and search parameters
term = args["query"]
headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
params = {"q": term, "offset": 0, "count": GROUP_SIZE}
 
# make the search
print("[INFO] searching Bing API for '{}'".format(term))
search = requests.get(URL, headers=headers, params=params)
search.raise_for_status()
 
# grab the results from the search, including the total number of
# estimated results returned by the Bing API
results = search.json()
estNumResults = min(results["totalEstimatedMatches"], MAX_RESULTS)
print("[INFO] {} total results for '{}'".format(estNumResults, term))

total = 0
# loop over the estimated number of results in `GROUP_SIZE` groups
for offset in range(0, estNumResults, GROUP_SIZE):
	# update the search parameters using the current offset, then
	# make the request to fetch the results
	print("[INFO] making request for group {}-{} of {}...".format(offset, offset + GROUP_SIZE, estNumResults))
	params["offset"] = offset
	search = requests.get(URL, headers=headers, params=params)
	search.raise_for_status()
	results = search.json()
	print("[INFO] saving images for group {}-{} of {}...".format(offset, offset + GROUP_SIZE, estNumResults))

	# save images in the current batch
	for v in results["value"]:
		try:
			print("[INFO] fetching: {}".format(v["contentUrl"]))
			req = requests.get(v["contentUrl"], timeout=30)

			# make the path to the image
			ext = v["contentUrl"][v["contentUrl"].rfind("."):]
			path = os.path.sep.join([args["output"], "{}{}".format(str(total).zfill(8), ext)])

			# write the image to disk
			f = open(path, "wb")
			f.write(req.content)
			f.close()
		
		except Exception as e:
			if type(e) in EXCEPTIONS:
				print("[INFO] skipping: {}".format(v["contentUrl"]))
				continue
		
		# check if image can be loaded by OpenCV
		image = cv2.imread(path)
		if image is None:
			print("[INFO] deleting: {}".format(path))
			os.remove(path)
			continue

		total += 1

