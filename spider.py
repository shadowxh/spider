#!/usr/bin/env python  
#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import re
proxies={"http":"222.78.248.10:3128","https":"222.78.248.10:3128",};
headers = {
		#'content-type': 'application/json',
           	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
		
}
def tag_text_is_dianzan(tag):
	return ((tag.name=='span') and (tag.string==u'点赞'));

def is_chinese(uchar):
	if uchar>=u'\u4e00' and uchar<=u'\u9fa5':return True;
	else:return False;

urlname='http://chuansong.me/account/';
public_names=['AspirinMuseum'];
for public_name in public_names:
	count=0;
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
		#time.sleep(1);
		j=i*12;
		while True:
			r=requests.get(url=urlname+public_name,params={'start':j},headers=headers);
			r.encoding='utf-8';
			if r.ok==True:break;

		soup=BeautifulSoup(r.text,'lxml');
		articles=soup.find_all('a',class_='question_link');

		for article in articles:
			#article_names.append(article.string.encode('utf-8'));
			if article['href']=="/n/1458302751513":continue;
			while True:
                        	r=requests.get(url="http://chuansong.me"+article['href'],headers=headers);#get every article
                        	r.encoding='utf-8';
                        	if r.ok==True:break;
			soup=BeautifulSoup(r.text,'lxml');
			zan_cnt=soup.find_all(tag_text_is_dianzan);
			if len(zan_cnt)==0:
				zan_cnt="-1";
			else:
				zan_cnt=zan_cnt[0].next_sibling.next_sibling.contents[0].string;
			articles_all.append((article.string,"http://chuansong.me"+article['href'],int(zan_cnt)));
			count+=1;
			print count,zan_cnt;

	articles_all.sort(key=lambda article:article[2],reverse=True);
	print "total:"+str(len(articles_all));
	for i in range(0,30):#grab the contents of the first 30 articles
		if i>=len(articles_all):break;
		print "the ",i+1,"th article";
		while True:
                	r=requests.get(url=articles_all[i][1],headers=headers);
                        r.encoding='utf-8';
                        if r.ok==True:break;
             	soup=BeautifulSoup(r.text,'lxml');
		content=soup.find_all(id='img-content')[0];
		_file=open(public_name+'.txt','a+');
		lines=[];
		for line in content.strings:
			lines.append(line.encode('utf-8'));
		_file.writelines(lines);
		
	_file.close();
