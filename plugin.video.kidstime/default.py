# -*- coding: utf-8 -*-
#------------------------------------------------------------
# KidsTime
# (c) 2016 - KAOSbox
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.kidstime'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addonID + '/resources/art/'))

channellist=[
    ("Baby", "baby", ART+'baby.png'),
    ("Peuter / kleuter", "peuter", ART+'peuter.png'),
    ("Schoolgaand", "schoolgaand", ART+'schoolgaand.png'),
    ("Muziek", "muziek", ART+'muziek.png'),
    ("Engelse Muziek kanalen", "muziekengels", ART+'muziekengels.png'),
    ("Engelse Explore kanalen", "engels", ART+'engels.png'),
    ]


baby=[
     ("[COLOR blue]baby >>[/COLOR] BabyTV", "user/BabyTVNederlands", "http://i.imgur.com/MATAOSW.jpg"),
     ("[COLOR blue]baby >>[/COLOR] Bumba", "user/BumbaKanaal", "http://i.imgur.com/bqzCBPB.jpg"),
     ("[COLOR blue]baby >>[/COLOR] Uki", "channel/UCqT1TEgyJyfC7lpM-_6rVRQ", "http://i.imgur.com/KUQD04d.jpg"),
     ]

peuter=[
     ("[COLOR green]peuter / kleuter >>[/COLOR] Peuter & Kleuter liedjes", "user/Peuterliedjes", "http://i.imgur.com/oKIZdmK.jpg"),
     ("[COLOR green]peuter / kleuter >>[/COLOR] Peppa Pig", "channel/UCwNR9UNtcgzmRmNewxjsbmg", "http://i.imgur.com/pV3X12Z.jpg"),
     ("[COLOR green]peuter / kleuter >>[/COLOR] Nijntje", "user/NIJNTJE", "http://i.imgur.com/f31Qinn.jpg"),
     ("[COLOR green]peuter / kleuter >>[/COLOR] Mickey Mouse Clubhouse", "playlist/PLal1fCW8NLt_NMPmaAD6DGLsuR6xY5_Ff", "http://i.imgur.com/8YYm91m.jpg"),
     ("[COLOR green]peuter / kleuter >>[/COLOR] Efteling Sprookjesboom", "user/SprookjesboomTv", "http://i.imgur.com/JVMcRTa.jpg"),
     ("[COLOR green]peuter / kleuter >>[/COLOR] Efteling Jokie & Jet", "user/JokieEfteling", "http://i.imgur.com/SGVsy1l.jpg"),
     ("[COLOR green]peuter / kleuter >>[/COLOR] Kabouter Plop", "user/KabouterPlopKanaal", "http://i.imgur.com/bTO5mR4.jpg"),
     ]

schoolgaand=[
     ("[COLOR orange]schoolgaand >>[/COLOR] National Geographic Junior", "playlist/PL16F97188D646E450", "http://i.imgur.com/KebLOpC.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Walt Disney Studios Nederland", "user/WaltDisneyStudiosNL", "http://i.imgur.com/Ui0lVz5.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Prinsessia", "user/prinsessiatv", "http://i.imgur.com/Ou2MNZo.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Tita Tovernaar", "user/Titatovenaar", "http://i.imgur.com/nQSmo7I.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Efteling Raveleijn", "user/Raveleijn", "http://i.imgur.com/2kuMsEf.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Bassie en Adriaan", "user/bassieadriaanchannel", "http://i.imgur.com/REyFIga.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Amika", "user/AmikaKanaal", "http://i.imgur.com/XRNctz8.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Mega Mindy", "user/MegaMindyKanaal", "http://i.imgur.com/dQ8EQn2.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Heidi", "user/HeidiKanaal", "http://i.imgur.com/wX7N9kJ.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] De Smurfen", "channel/UCeR6gZ7LpF-DB-d0clvwY4w", "http://i.imgur.com/wHGEfVH.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Oggy", "channel/UCNEKMkg_DG8eAyR1BNWsSvw", "http://i.imgur.com/fBLojgW.jpg"),
     ("[COLOR orange]schoolgaand >>[/COLOR] Galaxy Park", "user/GalaxyParkKanaal", "http://i.imgur.com/Fzh5SOj.jpg"),
     ]

muziek=[
     ("[COLOR red]muziek >>[/COLOR] Mini Disco", "channel/UCaynZO752koKaWub6EDaApA", "http://i.imgur.com/oKIZdmK.jpg"),
     ("[COLOR red]muziek >>[/COLOR] Kinderen voor Kinderen", "user/ClubKVK", "http://i.imgur.com/1oho2f6.jpg"),
     ("[COLOR red]muziek >>[/COLOR] K3", "user/K3Kanaal", "http://i.imgur.com/NDp5gYX.jpg"),
     ("[COLOR red]muziek >>[/COLOR] Dirk Scheele", "user/DirkScheele", "http://i.imgur.com/fJXADSo.jpg"),
     ]

muziekengels=[
     ("[COLOR red]engels (muziek) >>[/COLOR] DisneyStars", "user/DisneyStars", icon),
     ("[COLOR red]engels (muziek) >>[/COLOR] KIDZ BOP", "user/KidzBopMusicVEVO", icon),
     ("[COLOR red]engels (muziek) >>[/COLOR] Recess Monkey", "user/recessmonkey3", icon),
     ("[COLOR red]engels (muziek) >>[/COLOR] childrenlovetosing", "user/childrenlovetosing", icon),
     ("[COLOR red]engels (muziek) >>[/COLOR] Little Kids Rock", "user/littlekidsrock", icon),
     ]

engels=[
     ("[COLOR yellow]engels (explore) >>[/COLOR] Art for Kids", "user/ArtforKidsHub", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Mister Maker", "user/mistermaker", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] ItsyArtist", "user/itsyartist", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] ArtDaniela", "user/ArtDaniela", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] batteryPOP", "user/batteryPOPkids", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Play Doh Guide", "user/PeppaPigUK", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] MyFroggyStuff", "user/MyFroggyStuff", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Muffalo Potato", "user/muffalopotato", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] RosannaPansino", "user/RosannaPansino", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] The Pet Collective", "user/ThePetCollective", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Cosmic Kids Yoga", "user/CosmicKidsYoga", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Cute Girls Hairstyles", "user/CuteGirlsHairstyles", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Madnes64", "user/madnes64", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] MADABOUTLEGO", "user/MADABOUTLEGO", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Wizz", "channel/UCHzoeK57op5kRPY7baseKaQ", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] ErinsAnimals", "user/ErinsHamsters", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Brave Wilderness", "user/BreakingTrail", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Enterprisingengine93", "user/Enterprisingengine93", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Trains!", "user/sklepowich", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] Fun2draw", "user/Fun2draw", icon),
     ("[COLOR yellow]engels (explore) >>[/COLOR] NerdECrafter", "user/NerdyCraftsies", icon),
     ]


sublists = {
    'baby': sorted((i for i in baby)),
    'peuter': sorted((i for i in peuter)),
    'schoolgaand': sorted((i for i in schoolgaand)),
    'muziek': sorted((i for i in muziek)),
    'muziekengels': sorted((i for i in muziekengels)),
    'engels': sorted((i for i in engels)),
    }


# Entry point
def run():
    plugintools.log("kidstime.run")
    
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
        plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )        

run()