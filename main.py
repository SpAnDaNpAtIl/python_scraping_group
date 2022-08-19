from linkedInScrape import *
import json

if __name__ == "__main__":
    with open('jobData.json', 'w') as outfile:
        json.dump(jobData, outfile)

    with open('companiesData.json', 'w') as outfile:
        json.dump(companies, outfile)