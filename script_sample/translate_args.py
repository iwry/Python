#! /usr/bin/env python
# coding: utf-8

from urllib import quote
import feedparser

URL = u"http://pipes.yahoo.com/poolmmjp/ej_translation_api?_render=rss&text=%s"

def main(s):
	eng_trans_quote = quote(s)
	api_url = URL % (eng_trans_quote, )
	d = feedparser.parse(api_url)
	items = d['items']
	if len(items) == 1:
		title = items[0].title
		desc = items[0].description
		return title + ":" + desc
	return ""

if __name__ == "__main__":
	import sys
	args = sys.argv
	if len(args) > 1:
		s = u"".join(args[1:])
		print s
		r = main(s)
		print r
		
