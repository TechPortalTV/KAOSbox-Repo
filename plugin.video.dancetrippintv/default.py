#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib,re,os
import xbmcplugin,xbmcgui
import xbmcaddon,xbmc
import requests

addon = xbmcaddon.Addon(id='plugin.video.dancetrippintv')
home = addon.getAddonInfo('path').decode('utf-8')
image = xbmc.translatePath(os.path.join(home, 'icon.png'))

pluginhandle = int(sys.argv[1])

def categories():
	dance = 'http://player.dancetrippin.tv/video/list/'
        addDir('Episodes',dance+'dj/','listVideos',image)
        addDir('Sol Sessions',dance+'sol/','listVideos',image)
        addDir('Ibiza Global Radio',dance+'igr/','listVideos',image)
        addDir('Other Videos',dance+'other/','listVideos',image)
        xbmcplugin.endOfDirectory(pluginhandle)

def listVideos():
	url = params['url']
	videos = requests.get(url).json()
	for video in videos:
	  title = video['title']
	  image = video['image']
	  slug = video['slug']
	  url = 'http://player.dancetrippin.tv/video/embed/'+slug
	  thumb = 'http://dancetrippin.tv/media/'+image
	  addLink(title,url,'playVideos',thumb)
        xbmcplugin.endOfDirectory(pluginhandle)

def playVideos():
	url = params['url']
	clip = requests.get(url).json()['clip']
	hoster = clip['url']
	if 'youtube' in hoster:
	  id = hoster.split('youtube.com/watch?v=')
	  stream = 'plugin://plugin.video.youtube/play/?video_id=' + id[1]
	if 'vimeo' in hoster:
	  id = hoster.split('vimeo.com/')
	  stream = 'plugin://plugin.video.vimeo/play/?video_id=' + id[1]
        listitem = xbmcgui.ListItem(path = stream)
        xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)

def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
        item=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        item.setInfo( type="Video", infoLabels={ "Title": name } )
        item.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(pluginhandle,url=u,listitem=item)

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
        item=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        item.setInfo( type="Video", infoLabels={ "Title": name } )
        xbmcplugin.addDirectoryItem(pluginhandle,url=u,listitem=item,isFolder=True)

def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
	  params=sys.argv[2]
	  cleanedparams=params.replace('?','')
	  if (params[len(params)-1]=='/'):
	    params=params[0:len(params)-2]
	  pairsofparams=cleanedparams.split('&')
	  param={}
	  for i in range(len(pairsofparams)):
	    splitparams={}
	    splitparams=pairsofparams[i].split('=')
	    if (len(splitparams))==2:
	      param[splitparams[0]]=urllib.unquote_plus(splitparams[1])
	return param

params=get_params()
try:
    mode=params["mode"]
except:
    mode=None
print "Mode: "+str(mode)
print "Parameters: "+str(params)

if mode==None:
    categories()
else:
    exec '%s()' % mode