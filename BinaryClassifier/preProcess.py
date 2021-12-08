import requests
from bs4 import BeautifulSoup

base_urls = ['https://www.coursera.org', 'https://www.apple.com', 'https://www.linkedin.com',
             'https://github.com', 'https://stackoverflow.com', 'https://aclibrary.org', 
             'https://www.youtube.com','https://twitter.com/', 'https://store.google.com', 
             'http://www.google.com', 'https://www.udemy.com/', 'https://harness.io/', 
             'https://blockchain.berkeley.edu/', 'https://openclassrooms.com/', 
             'https://campuswire.com/', 'https://docs.oracle.com/', 
             'https://algs4.cs.princeton.edu/', 'https://www.outreachy.org/', 
             'https://world.taobao.com/']

f = open('urls_negative.txt', 'w')

for url in base_urls:
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    s = 'http'
    for link in soup.find_all('a'):
        url2 = str(link.get('href'))
        if s in url2:
            f.write(url2)
            f.write('\n')
        else:
            url_new = url + url2
            f.write(url_new)
            f.write('\n')
f.close()


# Read from positive urls
my_file_p = open('urls_positive.txt', 'r')
contents_p = my_file_p.readlines()
my_file_p.close()

# Read from negative urls
my_file_n = open('urls_negative.txt', 'r')
contents_n = my_file_n.readlines()
my_file_n.close()

# collection of all the attributes
keywords_ = ['faculty','staff','people','professor','bio','index','id','profile','outcome']

# Write attribute into the data file
my_data = open('bio_Binary.csv', 'w')
s = ','
keyword_str = s.join(keywords_)
my_data.write(keyword_str)
my_data.write('\n')

m = len(contents_p)
n = len(contents_n)
k = len(keywords_)

my_data_arr = ['']*(m+n)
for i in range(m):
    for j in range(k-1):
        if keywords_[j] in contents_p[i]:
            my_data_arr[i] += ('1,')
        else:
            my_data_arr[i] += ('0,')
    my_data_arr[i] += ('1')
    my_data.write(my_data_arr[i])
    my_data.write('\n')

for i in range(m, m+n):
    for j in range(k-1):
        if keywords_[j] in contents_n[i-m]:
            my_data_arr[i] += ('1,')
        else:
            my_data_arr[i] += ('0,')
    my_data_arr[i] += ('0')
    my_data.write(my_data_arr[i])
    my_data.write('\n')

my_data.close()


