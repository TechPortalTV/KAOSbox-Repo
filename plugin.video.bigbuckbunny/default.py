import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,shutil
from resources.libs.common_addon import Addon
addon_id = 'plugin.video.bigbuckbunny'
addon = Addon(addon_id, sys.argv)
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.PNG'))
thumb = 'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Big_Buck_Bunny_first_23_seconds_1080p.ogv/mid-Big_Buck_Bunny_first_23_seconds_1080p.ogv.jpg'

def INDEX():
        addDir('Big Buck Bunny - Stereoscopic 3D','url',5,thumb,'',fanart)
        addDir('Big Buck Bunny - Anaglyph 3D','url',6,thumb,'',fanart)
        addDir('Big Buck Bunny - 4K, Quad-Full-HD (3840x2160)','url',7,thumb,'',fanart)
        addDir('Big Buck Bunny - Full HD (1920x1080)','url',1,thumb,'',fanart)
        addDir('Big Buck Bunny - 720p HD (1280x720)','url',2,thumb,'',fanart)
        addDir('Big Buck Bunny - 480p HD (854x480)','url',3,thumb,'',fanart)
	addDir('Birds - Bitrate Test','url',8,thumb,'',fanart)
	addDir('High Bitrate Sample Videos','url',9,thumb,'',fanart)

def ten(url):
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p 60 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p 30 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_30fps_normal.mp4',4,thumb,'',fanart)


def nine(url):
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 20 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird20.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 24 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird24.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 28 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird28.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 34 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird34.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 38 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird38.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 42 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird42.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 50 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird42.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 55 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird55.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 60 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird60.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 70 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird70.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 80 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird80.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MKV[/COLOR][/B] 90 Mbps','http://dl.ganjanetwork.ru/Files/Video%20Test%20Files/Bitrate/Birds/bird90.mkv',4,thumb,'',fanart)


def three(url):
        addLink('[B][COLOR gold]Sintel[/COLOR][/B] 1920x1080','http://www.libde265.org/hevc-bitstreams/sintel-1080-cfg02.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]Sintel[/COLOR][/B] 4096x1720','http://www.libde265.org/hevc-bitstreams/sintel-4096x1744-cfg02.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]Elephants Dream[/COLOR][/B] 1920x1080','http://www.libde265.org/hevc-bitstreams/elephants-dream-1080-cfg02.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]Spreed - The Meeting[/COLOR][/B] 1920x1080','http://www.libde265.org/hevc-bitstreams/spreed-1080p.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]Tears of Steel[/COLOR][/B] 1720x720','http://www.libde265.org/hevc-bitstreams/tos-1720x720-cfg01.mkv',4,thumb,'',fanart)
        addLink('[B][COLOR gold]Tears of Steel[/COLOR][/B] 4096x1720','http://www.libde265.org/hevc-bitstreams/tos-4096x1720-tiles.mkv',4,thumb,'',fanart)



def seven(url):
         addLink('[B][COLOR gold]MP4[/COLOR][/B]             720p 24fps','http://mirrorblender.top-ix.org/peach/bigbuckbunny_movies/big_buck_bunny_720p_surround.avi',4,thumb,'',fanart)

def four(url):
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              480p 24 fps','http://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_480p_surround-fix.avi',4,thumb,'',fanart)

def fourk(url):
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              4K, Quad-Full-HD 60 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_2160p_60fps_normal.mp4',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              4K, Quad-Full-HD 30 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_2160p_30fps_normal.mp4',4,thumb,'',fanart)

def Stereoscopic(url):
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p 60 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_stereo_abl.mp4',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p 30 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_30fps_stereo_abl.mp4',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              4K, Quad-Full-HD 30 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_2160p_30fps_stereo_abl.mp4',4,thumb,'',fanart)

def Anaglyph(url):
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p Red-Cyan Dubois 60 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_stereo_arcd.mp4',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p Red-Cyan Full Colour 60 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_stereo_arcc.mp4',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p Green-Magenta 60 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_stereo_agmh.mp4',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p Red-Cyan Dubois 30 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_30fps_stereo_arcd.mp4',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p Red-Cyan Full Colour 30 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_30fps_stereo_arcc.mp4',4,thumb,'',fanart)
        addLink('[B][COLOR gold]MP4[/COLOR][/B]              1080p Green-Magenta 30 fps','http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_30fps_stereo_agmh.mp4',4,thumb,'',fanart)

        
def PLAYLINK(name,url):
                playlist = xbmc.PlayList(1)
                playlist.clear()
                listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
                listitem.setInfo("Video", {"Title":name})
                listitem.setProperty('mimetype', 'video/x-msvideo')
                listitem.setProperty('IsPlayable', 'true')
                playlist.add(url,listitem)
                xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
                xbmcPlayer.play(playlist)

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
                                param[splitparams[0]]=splitparams[1]    
        return param
               
def addDir(name,url,mode,iconimage,description,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,mode,iconimage,description,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
 
 
params=get_params(); url=None; name=None; mode=None; site=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
 
print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)
 
if mode==None or url==None or len(url)<1: INDEX()
elif mode==1: ten(url)
elif mode==2: seven(url)
elif mode==3: four(url)
elif mode==4: PLAYLINK(name,url)
elif mode==5: Stereoscopic(url)
elif mode==6: Anaglyph(url)
elif mode==7: fourk(url)
elif mode==8: nine(url)
elif mode==9: three(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
