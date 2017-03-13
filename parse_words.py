#encoding=utf-8
import os
import os.path
import jieba
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
rootdir="./article_content";
stoplist = {}.fromkeys([ line.strip() for line in open("stopwords.txt") ]);
for parent,dirs,files in os.walk(rootdir):
	for file_name in files:
		print file_name;
		if file_name[-9:]!="_new2.txt":continue;
		_file=open(os.path.join(parent,file_name),"r");
		articles="";
		for line in _file:
			if len(line)<=100:continue;
			articles+=line.strip();
		_file.close();
		#print articles;
		jieba.load_userdict("/usr/lib/python2.7/site-packages/jieba/dict.txt.small");
		words=jieba.cut(articles);
		#words=[word.encode('utf-8') for word in list(words)];
		words= [word for word in words if word.encode('utf8') not in stoplist];
		
		word_freq={};
		for tmp in words:
			word_freq[tmp]=word_freq.get(tmp,0)+1;
		items = word_freq.items()
		items.sort(key=lambda x: x[1],reverse=True);
		for ele in items:
			print ele[0].encode('utf-8'),ele[1];

		words=" ".join(words);
		wc=WordCloud(
                        font_path="/usr/share/fonts/chinese/MSYHBD.TTC",
                        background_color="white",
                        max_words=2000,
                        #mask=back_color,
                        max_font_size=100,
                        random_state=42,
                );
                wc.generate(words);
                wc.to_file(os.path.join(parent,file_name[:-4]+".png"));
