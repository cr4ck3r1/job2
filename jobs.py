from bs4 import BeautifulSoup
import requests
import time
print(" aw esha bnusa ka sharaza nit teyda")
unfamiliar_skill =  input(' >>')
print(f'filtere {unfamiliar_skill} dakat ...')
def find_job():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        company_name = job.find('h3', class_ ='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ ='srp-skills').text.replace(' ', '')
        zanyare_zyatr = job.h2.a['href']
        if unfamiliar_skill not in skills:
            print (f"Company Name: {company_name.strip()} \n")
            print (f"Required skills: {skills.strip()} \n ")
            print(f"Zanyare Zyatr {zanyare_zyatr}\n \n \n ")
            with open(f'job{index}.txt', 'w') as f:
                f.write(f"Company Name: {company_name.strip()} \n")
                f.write(f"Required skills: {skills.strip()} \n ")
                f.write(f"Zanyare Zyatr {zanyare_zyatr}\n \n \n ")


if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
