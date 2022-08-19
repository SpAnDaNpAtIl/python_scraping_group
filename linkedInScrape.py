from jobCatData import *

linkedInUrl = 'https://www.linkedin.com/jobs/search/?keywords='



for i in jobData:
    category = i['category']
    subCategories = i['subCategories']
    print("Currently in Category: ", category)
    for j in subCategories:
        print("Currently in SubCategory: {} after {}s".format(j, round(time.time() - ini, 2)))
        j = j.replace(' ', '+')
        r = session.get(linkedInUrl + j)
        jobListLinkedIn = r.html.find('.jobs-search__results-list > li')
        if(len(jobListLinkedIn) == 0):
            break
        else:
            jobListLinkedIn = r.html.find('.jobs-search__results-list > li')[:10]  # restricting to 10 jobs per category
        jobSubCatAvailable = []
        for k in jobListLinkedIn:
            jobPosition = k.find('.base-search-card__title', first=True).text
            jobCompany = k.find('.base-search-card__subtitle', first=True).text
            jobLocation = k.find('.base-search-card__metadata > span:nth-child(1)', first=True).text
            jobSubCatAvailable.append({'Job Position': jobPosition, 'Job Company': jobCompany, 'Job Location': jobLocation})

        jobDataIndex = jobData.index(i)
        subCatIndex = subCategories.index(j)
        jobData[jobDataIndex]['subCategories'][subCatIndex] = {'Job Name': j, 'Job Listing Data': jobSubCatAvailable}



print(jobData)