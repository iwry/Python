# !/usr/bin/env python
# coding:utf-8

# トリグラム例

def ngram(text, n):
	results = []
	if len(text) >= n:
		for i in xrange(len(text)-n+1):
			results.append(text[i:i+n])
	return results

text = u'激おこぷんぷん丸'
for e in ngram(text, 3):
	print e