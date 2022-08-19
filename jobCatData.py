from requests_html import HTMLSession
import time

ini = time.time()
session = HTMLSession()

jobCatUrl = 'https://www.careerguide.com/career-options' #target URL for data
r = session.get(jobCatUrl) #get requesting the URL
rows = r.html.find('.c-body > .row') #finding rows in source code

jobData=[]

for i in rows:
    cols = i.find('.col-md-4') #finding columns in each row
    for j in cols:
        if(j.text.startswith('Institutes in India')):
            continue #ignoring institutes in india section because it only contains name of institutes
        elif(j.text.startswith('Exams and Syllabus')):
            continue
        elif (j.text.startswith('Psychometric Career Test')):
            continue
        elif (j.text.startswith('Public Admin & Government')):
            continue
        elif (j.text.startswith('Study Abroad')):
            continue


        resTemp = j.text.split('\n')
        jsonRes = {'category': resTemp[0], 'subCategories': resTemp[1:]}
        jobData.append(jsonRes)

print("Careerguide data scraped in: {}s".format(round(time.time() - ini, 2)))

#this code always needs to be runned for exectuing main.py since we are storing the data in memory as a list. Usually I store it in DB and run this code
#separately at the start so I dont need to run it everytime I run main.py




