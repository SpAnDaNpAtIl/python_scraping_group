from jobCatData import *
import json

if __name__ == "__main__":
    with open('jsondata.json', 'w') as outfile:
        json.dump(jobData, outfile)