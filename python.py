import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
l=[]
o={}
k=[]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
target_url='https://api.scrapingdog.com/scrape?api_key=6421e6a0c1f5f352e3f0f386&url=https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Marketing&location=Brasil&locationId=&geoId=106057199&start={}&dynamic=false'
print("testando aqui")
for i in range(math.ceil(300/25)):
    res = requests.get(target_url.format(i))
    soup=BeautifulSoup(res.text,'html.parser')
    alljobs_on_this_page=soup.find_all("li")
    print(len(alljobs_on_this_page))
    print(pd.DataFrame(k))
    #df = pd.DataFrame(k)
    #df.to_csv("linkedin.csv",index=False, encoding='utf-8')
    for x in range(0,len(alljobs_on_this_page)):
        jobid = alljobs_on_this_page[x].find("div",{"class":"base-card"}).get('data-entity-urn').split(":")[3]
        l.append(jobid)

target_url='https://api.scrapingdog.com/scrape?api_key=6421e6a0c1f5f352e3f0f386&url=https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}&dynamic=false'
print("tá aqui")
for j in range(0,len(l)):
    print('entrou aqui')
    print(target_url.format(l[j]))
    resp = requests.get(target_url.format(l[j]))
    soup=BeautifulSoup(resp.text,'html.parser')

    try:
        o["company"]=soup.find("div",{"class":"top-card-layout__card"}).find("a").find("img").get('alt')
    except:
        o["company"]=None

    try:
        o["job-title"]=soup.find("div",{"class":"top-card-layout__entity-info"}).find("a").text.strip()
    except:
        o["job-title"]=None

    try:
        o["level"]=soup.find("ul",{"class":"description__job-criteria-list"}).find("li").text.replace("Seniority level","").strip()
    except:
        o["level"]=None
    
    try:
        o["time"]=soup.find("time",{"class":"job-search-card__listdate--new"}).find("li").text.replace("Seniority level","").strip()
    except:
        o["time"]="default"

    k.append(o)
    o={}
    df = pd.DataFrame(k)
    df.to_csv("linkedin12.csv",index=False, encoding='utf-8')
print(k)