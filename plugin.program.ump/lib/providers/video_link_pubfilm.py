import json
import re
import socket
import time

domain="http://movie.pubfilmno1.com"
encoding="utf-8"

def match_results(link,inf,names):
	prefix=""
	submatch=False
	subpage=ump.get_page(link,encoding,referer=domain)
	imdbid=re.findall('"(http://www.imdb.com/title/tt.*?)"',subpage)
	if len(imdbid)>0:
		imdbid=imdbid[0]
		if imdbid.endswith("/"):
			imdbid=imdbid[:-1]
		imdbid=imdbid.split("/")[-1]
		if imdbid==inf["code"]:
			submatch=True
			ump.add_log("pubfilm matched %s with imdbid: %s"%(names[0],imdbid))
	else:
		mname=re.findall('<span style\="font-size\: large\;">(.*?)<',subpage)
		if len(mname)>0:
			for name in names:
				if submatch: break
				if ump.is_same(name,mname[0]):
					year=re.findall('\>([0-9]{4})\s',subpage)
					if len(year)>0:
						submatch=inf["year"]==int(year[0])
	prefix0=re.findall("itemprop='title'>.*?\((.*?)\)</span>",subpage)
	if len(prefix0)>0:
		prefix=prefix0[0].upper()
		if "HD" == prefix:
			prefix=""
		else:
			prefix="[%s]"%prefix
	return prefix,submatch,subpage
	

def run(ump):
	globals()['ump'] = ump
	i=ump.info
	is_serie,names=ump.get_vidnames()
	match=False

	mlink=""
	prefix=""

	if is_serie:
		return None

	try:
		for name in names:
			ump.add_log("pubfilm is searching %s" % name)
			data={"alt":"json-in-script","max-results":9999,"callback":"showResult","q":name}
			page=ump.get_page(domain+"/feeds/posts/summary",encoding,data=data,referer=domain)
			js=re.findall("showResult\((.*?)\);",page)
			if len(js)>0:
				js=json.loads(js[0])
				if "entry" in js["feed"].keys():
					for feed in js["feed"]["entry"]:
						if match: break
						for link in feed["link"]:
							if match: break
							if link["rel"]=="alternate":
								prefix,match,page=match_results(link["href"],i,names)
								mlink=link["href"]
				else:
					time.sleep(1)
					continue
			if match: break
	except socket.timeout:
		ump.add_log("pubfilm sitesearch is down, trying google")
		for u in ump.web_search("site:movie.pubfilmno1.com \"%s\""%name):
			if match: break
			prefix,match,page=match_results(link["href"],i,names)

	if not match:
		ump.add_log("pubfilm can't match %s"%name)
		return None

	link1=re.findall('"(http://player.pubfilm.com/api.*?)"',page)
	for link in link1:
		page=ump.get_page(link,encoding,referer=mlink)
		try:
			data=eval(re.findall("sources\:(.*?\])",page)[0])
			mparts={}
			for link in data:
				mparts[link["label"]]=link["file"]
			parts=[{"url_provider_name":"google", "url_provider_hash":mparts,"referer":link1}]
			ump.add_mirror(parts,"%s %s"%(prefix,name))			
		except:
			ump.add_log("pubfilm cant scrape %s"%link)
			
