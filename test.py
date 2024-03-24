# encoding:utf-8
import requests
import sys
token = sys.argv[1] #在pushplus网站中可以找到
title= 'git action test' #改成你要的标题内容
content ='git action content testt' #改成你要的正文内容
url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
requests.get(url)

