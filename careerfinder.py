import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from operator import itemgetter 
import os
import urllib
import re
import sys

def get_data(skills):
	j = []
	for i in skills:
		name = urllib.parse.quote_plus(i)
		url = 'https://www.indeed.com/q-'+name+'-jobs.html'
		result = requests.get(url)
		soup = BeautifulSoup(result.text, "html.parser")
		j.extend(get_jobs(soup))
	print(mappify_keywords(j))
		#print(mappify_keywords(get_jobs(soup)))

def get_jobs(soup):
	jobs = []
	for div in soup.find_all(name="div", attrs={"class":"row"}):
		for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
			jobs.append(a["title"])
	return(jobs)

def mappify_keywords(jobs):
	job_map = {}
	for i in jobs:
		split_string = i.split()
		for s in split_string:
			if s in job_map and s[0].isupper() and not s == "-" and not s == "/" and not s == "and":
				job_map[s] = job_map[s] + 1
			else:
				job_map[s] = 1
	jm = OrderedDict(sorted(job_map.items(), key = itemgetter(1), reverse = True))
	dict_jm = dict(jm)
	first5pairs = {k: dict_jm[k] for k in list(dict_jm)[:10]}
	return first5pairs


		

get_data(['java', 'python','html','css','django','mysql'])
#{'Developer': 34, 'Engineer': 17, 'Java': 15, 'Python': 15, 'Software': 9, 'Level': 7, 'Full': 6, 'Entry': 6, 'Data': 6, 'Technical': 6}