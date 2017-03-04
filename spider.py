#!/usr/bin/env python  
#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import re
headers = {
		#'content-type': 'application/json',
           	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
		
}
def tag_text_is_dianzan(tag):
	return (tag.name=='span') and (tag.string==u'点赞');

urlname='http://chuansong.me/account/';
public_names=['thefair2']#,'mimeng7','AspirinMuseum'];
for public_name in public_names:
	articles_all=[];
	while True:
		r=requests.get(url=urlname+public_name,params={'start':0},headers=headers);
		r.encoding='utf-8';
		if r.ok==True:break;

	soup=BeautifulSoup(r.text,'lxml');
	url_pattern='/account/'+public_name+"\?.*";
	page_cnt=soup.find_all('a',href=re.compile(url_pattern));
	page_cnt=int(page_cnt[-2].string);
	
	print page_cnt;
	for i in range(0,page_cnt):#visit each page
		time.sleep(1);
		j=i*12;
		while True:
			r=requests.get(url=urlname+public_name,params={'start':j},headers=headers);
			r.encoding='utf-8';
			if r.ok==True:break;

		soup=BeautifulSoup(r.text,'lxml');
		articles=soup.find_all('a',class_='question_link');

		for article in articles:
			#article_names.append(article.string.encode('utf-8'));
			while True:
                        	r=requests.get(url="http://chuansong.me"+article['href'],headers=headers);#get every article
                        	r.encoding='utf-8';
                        	if r.ok==True:break;
			soup=BeautifulSoup(r.text,'lxml');
			zan_cnt=soup.find_all(tag_text_is_dianzan);
			zan_cnt=zan_cnt[0].next_sibling.next_sibling.contents[0].string;
			articles_all.append((article.string.encode('utf-8'),int(zan_cnt)));
			print zan_cnt;	

	articles_all.sort(key=lambda article:article[1],reverse=True);
	tmp=[];
	for i in articles_all:
		tmp.append(i[0][1:]+":"+str(i[1]));

	print "total:"+str(len(articles_all));
	_file=open(public_name+'_articles.txt','w');
	_file.writelines(tmp);
	_file.close();
