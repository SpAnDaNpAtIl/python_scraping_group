import json
import sqlite3

conn = sqlite3.connect('SQLDatabase.db')




with open('jobData.json') as f:
    data = json.load(f)

with open('companiesData.json') as f:
    companiesdata = json.load(f)



companyList = []
for i in companiesdata:
    companyList.append(i.get('Name'))

companyListStatesCategories = [[] for i in companyList]


stateList = []
jobJsonData =[]
for i in data:
    JobJsonlist = i.get('subCategories')
    for j in JobJsonlist:

        if j.get('Job Listing Data') != []:
            for k in j.get('Job Listing Data'):
                jobJsonData.append(k)
                companyName = k.get('Job Company')
                location_info = k.get('Job Location')
                boolerRemote = False
                if(boolerRemote == False and 'remote' in location_info.lower()):
                    stateList.append('Remote')
                    boolerRemote = True
                stateList.append(location_info.split(', ')[-1])
                indexer = companyList.index(companyName)
                companyListStatesCategories[indexer].append([location_info.split(', ')[-1], j.get('Job Name').replace('+',' ')])


stateList = list(set(stateList))
stateListNew = []
for i in range(len(stateList)):
    if len(stateList[i])==2:
        stateListNew.append(stateList[i])



#code for inserting data into states table
"""
for i in range(len(stateListNew)):
    conn.execute("INSERT INTO STATES (ID,STATE) VALUES (?,?)",(i+1,stateListNew[i]))

conn.commit()
conn.close()
"""


#code for inserting data into categories table and subcategories table
"""
categoryList = []
subcategoryList =[]

for i in data:
    categoryList.append(i.get('category'))
    for j in i.get('subCategories'):
        subcategoryList.append(j.get('Job Name').replace('+',' '))

categoryList = list(set(categoryList))
subcategoryList = list(set(subcategoryList))

for i in range(len(categoryList)):
    conn.execute("INSERT INTO CATEGORIES (ID,CATEGORY) VALUES (?,?)",(i+1,categoryList[i]))

for i in range(len(subcategoryList)):
    conn.execute("INSERT INTO SUBCATEGORIES (ID,SUBCATEGORY) VALUES (?,?)",(i+1,subcategoryList[i]))


conn.commit()
conn.close()
"""

#code for inserting data into jobs table
"""
for i in range(len(jobJsonData)):
    companyName = jobJsonData[i].get('Job Company')
    jobPosition = jobJsonData[i].get('Job Position')
    location = jobJsonData[i].get('Job Location')
    conn.execute("INSERT INTO JOBS (ID,COMPANYNAME,JOBPOSITION,LOCATION) VALUES (?,?,?,?)",(i+1,companyName,jobPosition,location))

conn.commit()
conn.close()
"""

#after adding jobs table, I found out linkedin had multiple job listings of same company with same designation.
#always use select distinct to avoid duplicates


#code for inserting data into companydetails table
"""
companydetailsID = 1
for i in range(len(companyList)):
    for j in range(len(companyListStatesCategories[i])):
        conn.execute("INSERT INTO COMPANYDETAILS (ID, COMPANYNAME, ABOUT, STATES, SUBCATEGORY) VALUES (?,?,?,?,?)", (companydetailsID, companiesdata[i].get('Name'), companiesdata[i].get('About'), companyListStatesCategories[i][j][0], companyListStatesCategories[i][j][1]))
        companydetailsID+=1

conn.commit()
conn.close()
"""








