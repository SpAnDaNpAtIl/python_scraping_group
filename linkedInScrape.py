from jobCatData import *

import cloudscraper
from bs4 import BeautifulSoup

linkedInUrl = 'https://www.linkedin.com/jobs/search/?keywords='

companies = []

for i in jobData:
    category = i['category']
    subCategories = i['subCategories']
    print("Currently in Category: ", category)
    for j in subCategories:
        print("Currently in SubCategory: {} after {}s".format(j, round(time.time() - ini, 2)))
        j = j.replace(' ', '+')
        r = session.get(linkedInUrl + j)
        jobSubCatAvailable = []
        jobDataIndex = jobData.index(i)
        subCatIndex = subCategories.index(j.replace('+', ' '))
        try:
            jobListLinkedIn = r.html.find('.jobs-search__results-list > li')
        except:
            jobData[jobDataIndex]['subCategories'][subCatIndex] = {'Job Name': j, 'Job Listing Data': jobSubCatAvailable}

        if(len(jobListLinkedIn) == 0):
            jobData[jobDataIndex]['subCategories'][subCatIndex] = {'Job Name': j, 'Job Listing Data': jobSubCatAvailable}
        else:
            try:
                jobListLinkedIn = r.html.find('.jobs-search__results-list > li')[:10]  # restricting to 10 jobs per category
            except:
                jobData[jobDataIndex]['subCategories'][subCatIndex] = {'Job Name': j, 'Job Listing Data': jobSubCatAvailable}

        for k in jobListLinkedIn:
            jobPosition = k.find('.base-search-card__title', first=True).text
            jobCompany = k.find('.base-search-card__subtitle', first=True).text
            jobLocation = k.find('.base-search-card__metadata > span:nth-child(1)', first=True).text
            jobSubCatAvailable.append({'Job Position': jobPosition, 'Job Company': jobCompany, 'Job Location': jobLocation})
            companies.append(jobCompany)


        jobData[jobDataIndex]['subCategories'][subCatIndex] = {'Job Name': j, 'Job Listing Data': jobSubCatAvailable}


companies = list(set(companies))

scraper = cloudscraper.create_scraper()
for i in companies:
    print('Currently in Company: {} which is {}/{} after {}s'.format(i, companies.index(i)+1, (len(companies)), round(time.time() - ini, 2)))
    r = scraper.get('https://in.indeed.com/companies/search?q=' + i.replace(' ', '+')).text
    soup = BeautifulSoup(r, 'html.parser')
    companyIndex = companies.index(i)
    try:
        ID = soup.find('div', {'data-tn-component':'CompanyRow'}).find('a')['href']
    except:
        About = 'Unknown'
        Location = 'Unknown'
        NumberofEmployees = 'Unknown'
        companies[companyIndex] = {'Name': i, 'About': About, 'Location': Location, 'NumberofEmployees': NumberofEmployees}
        continue
    urlNew = 'https://in.indeed.com' + ID
    r = scraper.get(urlNew).text
    soup = BeautifulSoup(r, 'html.parser')
    try:
        Location = soup.find('li', {'data-testid':'companyInfo-headquartersLocation'}).text
        try:
            Location = soup.find('li', {'data-testid':'companyInfo-headquartersLocation'}).find('span').text
        except:
            Location = soup.find('li', {'data-testid': 'companyInfo-headquartersLocation'}).find_all('div')[-1].text
    except:
        Location = 'Location Unknown'

    try:
        NumberofEmployees = soup.find('li', {'data-testid':'companyInfo-employee'}).text
        try:
            NumberofEmployees = soup.find('li', {'data-testid':'companyInfo-employee'}).find('span').text
        except:
            NumberofEmployees = soup.find('li', {'data-testid': 'companyInfo-employee'}).find_all('div')[-1].text
    except:
        NumberofEmployees = 'Location Unknown'

    urlAbout = urlNew + '/about'
    r = scraper.get(urlAbout).text
    soup = BeautifulSoup(r, 'html.parser')
    try:
        About = soup.find('div', {'data-testid':'companyAbout'})
        if(About.find('div', {'data-testid':'emptyPageText'})):
            About = "No Description Provided"
        else:
            About = About.find('div', {'data-testid':'content'}).text
    except:
        About = "Unknown"
    companies[companyIndex] = {'Name': i, 'About': About, 'Location': Location, 'NumberofEmployees': NumberofEmployees}



