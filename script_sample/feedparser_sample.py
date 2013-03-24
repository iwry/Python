#coding:utf-8

import feedparser
import time

feeds = feedparser.parse('http://feeds.feedburner.com/hatena/b/hotentry')

#Print site name
print feeds.feed.title

#Print feed's title & URL
for i in range(10):
	print feeds.entries[i].title
	print feeds.entries[i].link
	#Time of Newest article 
	updatetime = time.strftime('%Y/%m/%d %X', feeds.entries[i].updated_parsed)
	print updatetime