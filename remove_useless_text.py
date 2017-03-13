#!/usr/bin/env python  
#-*- coding:utf-8 -*-
import os
import os.path
rootdir="./article_content";
for parent,dirs,files in os.walk(rootdir):
        for file_name in files:
                print file_name;
                if file_name[-4:]!=".txt":continue;
                _file=open(os.path.join(parent,file_name),"r");
                articles=[];
                for line in _file:
                        if len(line)<=200:continue;
                        articles.append(line);
                _file.close();
                _file=open(os.path.join(parent,file_name[:-4]+"_new.txt"),"a+");
		_file.writelines(articles);
		_file.close();
