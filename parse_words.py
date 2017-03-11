#encoding=utf-8
import os
import os.path
import jieba
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
rootdir="./article_content";
for parent,dirs,files in os.walk(rootdir):
	for file_name in files:
		print file_name;
		_file=open(os.path.join(parent,file_name),"r",encoding="utf-8");
		articles="";
		for line in _file:
			if len(line)<=100:continue;
			articles+=line.rstrip().lstrip();
		#print articles;
		words=jieba.cut(articles);
		"""
		for j in words:
			print j;
		"""
		_file.close();
		break;
		
