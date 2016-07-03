# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Back to the 80s
# (c) 2016 - KAOSbox
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.backtothe80s'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addonID + '/resources/art/'))

channellist=[
    ("80er jaren Muziek Playlists >>", "music", ART+'music.png'),
    ("80er jaren Muziek Documentaires >>", "musicdoc", ART+'musicdoc.png'),
    ("BBC - I Love The 80s >>", "bbc", ART+'love.png'),
    ("80er jaren Televisie >>", "tv", ART+'tv.png'),
    ("Commercials uit de jaren 80 >>", "commercials", ART+'commercials.png'),
    ("Gaming en computers in de 80er jaren >>", "gaming", ART+'gaming.png'),
    ("Documentaires over de 80er jaren >>", "doc", ART+'doc.png'),
    ]


sublists= {

'music':[
        ("[COLOR red]Playlist[/COLOR] Nederlandstalig Jaren 80", "playlist/PLIj84zT8vo2kHrHGkRXbDBgG--rZGZKVk", ART+'music.png'),
	("[COLOR red]Playlist[/COLOR] Jaren 80 nummer 1 hits", "playlist/PLFdjwk0_rPKpBvycOv1SP7qPLR7Tmigvx", ART+'music.png'),
	("[COLOR red]Playlist[/COLOR] 80s Playlist", "playlist/PLL55rJswZPUY6pNadCpeBlZaivnbA42PM", ART+'music.png'),
	("[COLOR red]Playlist[/COLOR] The Great 80s", "user/meliberty", ART+'music.png'),
	("[COLOR red]Playlist[/COLOR] VH1's 100 Greatest Songs of the 80s", "playlist/PLCF2B29B9312CE35D", ART+'music.png'),
     ],

'musicdoc':[
	("[COLOR yellow]Documentaire[/COLOR] MTV Decade 1980-1989", "play/?video_id=s9nQjJ_hLXU", ART+'musicdoc.png'),
	("[COLOR yellow]Documentaire[/COLOR] When Metal Ruled The World 80's LA Sunset Strip Story", "play/?video_id=AUrHVWa3s2Y", ART+'musicdoc.png'),
	("[COLOR yellow]Documentaire[/COLOR] VH1 Presents the 80's: Pop", "play/?video_id=XaGNEof6t4g", ART+'musicdoc.png'),
	("[COLOR yellow]Documentaire[/COLOR] VH1 Presents the 80's: Heavy Metal", "play/?video_id=quhEVLqsTpw", ART+'musicdoc.png'),
	("[COLOR yellow]Documentaire[/COLOR] VH1 Presents the 80's: New Wave/Alternative Rock", "play/?video_id=3dQrTOf7nhw", ART+'musicdoc.png'),
	("[COLOR yellow]Documentaire[/COLOR] VH1 Presents the 80's: Hip Hop/R&B", "play/?video_id=RRt78cZOBOo", ART+'musicdoc.png'),
	("[COLOR yellow]Documentaire[/COLOR] VH1 Presents the 80's: Impact of MTV and Music Videos", "play/?video_id=-6inD_qXXfE&", ART+'musicdoc.png'),
	("[COLOR yellow]Documentaire[/COLOR] Hip Hop: The Early Years 1979 - 1986", "play/?video_id=XXhE_6koCtU", ART+'musicdoc.png'),
     ],


'bbc':[
	("BBC - I Love 1980", "play/?video_id=ulyTQE3SXGM", ART+'love.png'),
	("BBC - I Love 1981", "play/?video_id=Dneq7YRFB_E", ART+'love.png'),
	("BBC - I Love 1982 Part 1", "play/?video_id=p02_KO910FE", ART+'love.png'),
	("BBC - I Love 1982 Part 2", "play/?video_id=tXOnOJZvU1A", ART+'love.png'),
	("BBC - I Love 1982 Part 3", "play/?video_id=8Rmbw1KG1pA", ART+'love.png'),
	("BBC - I Love 1982 Part 4", "play/?video_id=ghu1NKxxH6U", ART+'love.png'),
	("BBC - I Love 1982 Part 5", "play/?video_id=6MXPOgCu6vg", ART+'love.png'),
	("BBC - I Love 1982 Part 6", "play/?video_id=OO9Um8lmF9o", ART+'love.png'),
	("BBC - I Love 1982 Part 7", "play/?video_id=V878EGb5ORA", ART+'love.png'),
	("BBC - I Love 1983", "play/?video_id=UuULCYfvSRw", ART+'love.png'),
	("BBC - I Love 1984", "play/?video_id=DPLcf5pp8GE", ART+'love.png'),
	("BBC - I Love 1985", "play/?video_id=kj8NCb41ygA", ART+'love.png'),
	("BBC - I Love 1986", "play/?video_id=RQgijroNioQ", ART+'love.png'),
	("BBC - I Love 1987", "play/?video_id=_q_0SJnZY50", ART+'love.png'),
	("BBC - I Love 1988", "play/?video_id=kS0xjf6NagQ", ART+'love.png'),
	("BBC - I Love 1989", "play/?video_id=CQZyX538Rv8", ART+'love.png'),
     ],


'tv':[
        ("TV jaren 80", "playlist/PLAF48B7774AC57550", ART+'tv.png'),
	("Tijd voor 80 - televisie", "playlist/PLdgTESJsxLJKuG8eyqDORuX19nvjpY57Q", ART+'tv.png'),
	("80's TV Theme Songs", "playlist/PL6z6OgcOWW85HpkeoNwQQtw-qpGvPXM7i", ART+'tv.png'),
	("80's Television Intro Mania", "playlist/PL236630F8CC8834EB", ART+'tv.png'),
	("Top 25 80's childrens tv intro's", "play/?video_id=dy3RTFFhSYs", ART+'tv.png'),
     ],

'commercials':[
    	("Commercials from the 80s/Reclames uit de jaren 80 (1)", "playlist/PL497CFFFC18385690", ART+'commercials.png'),
	("Commercials from the 80s/Reclames uit de jaren 80 (2)", "playlist/PL9DF22EABA0820251", ART+'commercials.png'),
	("Reclame jaren 80", "playlist/PL7CDDA0B2444BC5FD", ART+'commercials.png'),
	("80s Commercials", "playlist/PLC3458763E3A3C5A2", ART+'commercials.png'),
	("80s Commercials Vol. 2", "playlist/PL6676FB688D404E2A", ART+'commercials.png'),
     ],

'gaming':[
    	("Retro Gaming Shows", "channel/UCUVnfQaEmCIhFZC5d_JniyQ", ART+'gaming.png'),
    	("Old Classic Retro Gaming", "user/oldclassicgame", ART+'gaming.png'),
    	("Retro Video Gaming", "user/stopXwhispering", ART+'gaming.png'),
    	("Retro Gamers Society", "user/RetroGamersSociety", ART+'gaming.png'),
    	("RetroGamerVX", "user/RetroGamerVX", ART+'gaming.png'),
	("[COLOR yellow]Documentaire[/COLOR] Terminal Madness (A 1980 Documentary About Personal Computers)", "play/?video_id=F4jr1I17Gxs", ART+'gaming.png'),
	("[COLOR yellow]Documentaire[/COLOR] The Computer Chronicles: MIDI Music (1986)", "play/?video_id=D8lSMytqdEY", ART+'gaming.png'),
	("[COLOR yellow]Documentaire[/COLOR] Sinclair Research computer history", "play/?video_id=WUDPSzhfPQo", ART+'gaming.png'),
	("[COLOR yellow]Documentaire[/COLOR] The Fall of Imagine Software 1984 / The Age Of The ZX Spectrum The Documentary", "play/?video_id=dyLNrpvcgkk", ART+'gaming.png'),
     ],


'doc':[
	("The Grumpy Guide To The 80s", "play/?video_id=1gIZqykrT-A", ART+'doc.png'),
	("Video World - The Death of a Video Store (Video Store Documentary)", "play/?video_id=4jogbom8v4U", ART+'doc.png'),
     ],
	
}



# Entry point
def run():
    plugintools.log("80time.run")
    
       # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        sub_list(action)
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("kidstime.main_list "+repr(params))

    for name, id, icon in channellist:
        url = sys.argv[0] + "?action=" + id
        plugintools.add_item(title=name,url=url,thumbnail=icon,folder=True )

def sub_list(action):
    plugintools.log("kidstime.sub_list "+repr(action))
    for List in sublists[str(action)]:
        name = List[0]
        id = List[1]
        icon = List[2]
        pluginurl = "plugin://plugin.video.youtube/"+id
        folder=False
        if not 'video_id' in pluginurl:
            pluginurl = pluginurl + "/"
            folder=True
        plugintools.add_item(title=name,url=pluginurl,thumbnail=icon,folder=folder )        

run()