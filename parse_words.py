#encoding=utf-8
import os
import os.path
import jieba
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
rootdir="./article_content";
for parent,dirs,files in os.walk(rootdir):
	for file_name in files:
		print file_name;
		_file=open(os.path.join(parent,file_name),"r");
		articles="";
		for line in _file:
			if len(line)<=100:continue;
			articles+=line.rstrip().lstrip();
		_file.close();
		#print articles;
		jieba.load_userdict("/usr/lib/python2.7/site-packages/jieba/dict.txt.small");
		words=" ".join(jieba.cut(articles));
		"""
		for j in words:
			print j;
		"""
		wc=WordCloud(
                        font_path="/usr/share/fonts/chinese/MSYHBD.TTC",
                        background_color="white",
                        max_words=2000,
                        #mask=back_color,
                        max_font_size=100,
                        random_state=42,
                );
                wc.generate(words);
                wc.to_file(os.path.join(parent,file_name[:-5]+".png"));
