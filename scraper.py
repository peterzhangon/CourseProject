#############################
#############################
#############################
####START CODE####

#### Requirement - 
# beautifulsoup4 <= 4.9.3

import requests
from bs4 import BeautifulSoup
import re

def get_links(base_url,faculty_extension):
    reqs = requests.get(base_url+faculty_extension)
    soup = BeautifulSoup(reqs.text, "html.parser") #'lxml'
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    #print('Total URLs - ',len(links))
    print 'Total URLs - '+str(len(links))
    
    links = [str(x).lower() for x in links]
    links = list(set(links))
    links = [x for x in links if x.startswith('tel:')==False]
    links = [x for x in links if x.startswith('mailto:')==False]
    links1 = [x for x in links if x.startswith('http')==True]
    links2 = [base_url+'/'+x for x in links if x.startswith('http')==False and x.startswith('/')==False] #
    links3 = [base_url+x for x in links if x.startswith('http')==False and x.startswith('/')==True] #
    links = links1+links2+links3
    links = list(set(links))
    #print('Useful URLs - ',len(links))
    print 'Useful URLs - '+str(len(links))
    
    
    #####
    work_links = []
    for i in links:
        if  i.find("bio")>-1 or i.find("faculty")>-1 or i.find("staff")>-1 or i.find("people")>-1 or i.find("facultystaff")>-1 or i.find("directory")>-1 :
            work_links.append(i)
    #print('Faculty URLs - ',len(work_links))
    print 'Faculty URLs - '+str(len(work_links))
    assert len(work_links)>0,'No Faculty links found. Kindly enter another link!'
    #print('\n-> Got all links!')
    print '\n-> Got all links!'
    return work_links

def get_text(work_links):
    #url = "https://cs.illinois.edu/about/people/all-faculty/zilles"
    required_text = []
    profile_text = []
    count=0
    for url in work_links:
        #print('URL - ', url)
        count+=1
        print 'Fetched link - '+str(count)
#        if count>5:
#            break
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text,'html.parser')#'lxml'
        table = soup.find_all('p')#,attrs={"class":"directory-profile maxwidth800"}) #find_all
        for x in table:
            try:
                sentence = str(x.text)
                sentence = sentence.replace('\n',' ')
                match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', sentence)
                if len(match)==0:
                    profile_text.append(sentence)
            except:
                continue
        profile_text = [x for x in profile_text if len(x)>200]
        profile_text = list(set(profile_text))
        required_text = required_text+profile_text
        required_text = list(set(required_text))
    #print('\n-> Scraped all the text!')
    print '\n-> Scraped all the text!'
    return required_text

def save_files(required_text):
    c=1
    for i in required_text:
        #print('Saved file'+str(c))
        print 'Saved file'+str(c)
        f = open('<Path_to_the_dir>'+str(c)+".txt", "a")
        f.write(i.strip())
        f.close()
        c+=1 
    #print('\n->Saved all files!')
    print '\n->Saved all files!'

#1 example
base_url = 'https://cs.illinois.edu' # 'https://illinois.edu' 
faculty_extension = '/about/people/all-faculty' #'/'#

#2 example
#base_url  = 'https://www.stern.nyu.edu'
#faculty_extension = '/faculty/search_name_form'

#3 example
#base_url  = 'https://history.uchicago.edu'
#faculty_extension =  '/directories/full/current-faculty'

####Fetch links
work_links = get_links(base_url,faculty_extension)
####Fetch texts
required_text = get_text(work_links)
####Save texts (given path)
save_files(required_text)

##--##--##--##--##--##--##--##--##--##--##--##
### End of code
