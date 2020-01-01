from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
import collections
import urllib
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from operator import itemgetter 
import re
import sys

main = Blueprint('main', __name__)
CORS(main)

@main.route('/getkeywordrecommendations')
def jsonified_recommendations():
	keyword_data = request.headers['search']
	keywords_parsed = parse_text(keyword_data)
	j = []
	for i in keywords_parsed:
		name = urllib.parse.quote_plus(i)
		url = 'https://www.indeed.com/q-'+name+'-jobs.html'
		result = requests.get(url)
		soup = BeautifulSoup(result.text, "html.parser")
		j.extend(get_jobs(soup))
	df = mappify_keywords(j)
	ls = []
	for i,j in df.items():
		dictionary_of_json = collections.defaultdict(dict)
		dictionary_of_json['keyword'] = i
		dictionary_of_json['percent'] = j
		dictionary_updated = dict(dictionary_of_json)
		ls.append(dictionary_updated)
	return jsonify({'keywords': ls})


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
			if not "-" in s and not "/" in s and not "and" in s and not "Nerd" in s:
				if s in job_map and s[0].isupper():
					job_map[s] = job_map[s] + 1
				else:
					job_map[s] = 1
	jm = OrderedDict(sorted(job_map.items(), key = itemgetter(1), reverse = True))
	dict_jm = dict(jm)
	first15pairs = {k: dict_jm[k] for k in list(dict_jm)[:30]}
	the_sum = sum(first15pairs.values())
	for i in first15pairs:
		first15pairs[i] = str(round(float(first15pairs[i])/the_sum * 100, 2))
	return first15pairs



def parse_text(skilltext):
	if skilltext == "":
		return []
	skilltext_split = skilltext.split(",")
	return skilltext_split
