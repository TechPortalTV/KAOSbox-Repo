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
    ("[COLOR blue]Baby >>[/COLOR]", "baby", ART+'baby.png'),
    ("[COLOR green]Peuter & Kleuter >>[/COLOR]", "peuter", ART+'peuter.png'),
    ("[COLOR orange]Schoolgaand >>[/COLOR]", "schoolgaand", ART+'schoolgaand.png'),
    ("[COLOR red]Muziek >>[/COLOR] ", "muziek", ART+'muziek.png'),
    ("[COLOR red]Engelse Muziek kanalen >>[/COLOR] ", "muziekengels", ART+'muziekengels.png'),
    ("[COLOR yellow]Engelse Explore kanalen >>[/COLOR]", "engels", ART+'engels.png'),
    ]

sublists = {
'baby':[
     ("BabyTV", "user/BabyTVNederlands", "http://i.imgur.com/MATAOSW.jpg"),
     ("Bumba", "user/BumbaKanaal", "http://i.imgur.com/bqzCBPB.jpg"),
     ("Uki", "channel/UCqT1TEgyJyfC7lpM-_6rVRQ", "http://i.imgur.com/KUQD04d.jpg"),
     ],

'peuter':[
     ("Peuter & Kleuter liedjes", "user/Peuterliedjes", "http://i.imgur.com/oKIZdmK.jpg"),
     ("Peppa Pig", "channel/UCwNR9UNtcgzmRmNewxjsbmg", "http://i.imgur.com/pV3X12Z.jpg"),
     ("Nijntje", "user/NIJNTJE", "http://i.imgur.com/f31Qinn.jpg"),
     ("Mickey Mouse Clubhouse", "playlist/PLal1fCW8NLt_NMPmaAD6DGLsuR6xY5_Ff", "http://i.imgur.com/8YYm91m.jpg"),
     ("Efteling Sprookjesboom", "user/SprookjesboomTv", "http://i.imgur.com/JVMcRTa.jpg"),
     ("Efteling Jokie & Jet", "user/JokieEfteling", "http://i.imgur.com/SGVsy1l.jpg"),
     ("Kabouter Plop", "user/KabouterPlopKanaal", "http://i.imgur.com/bTO5mR4.jpg"),
     ],

'schoolgaand':[
     ("National Geographic Junior", "playlist/PL16F97188D646E450", "http://i.imgur.com/KebLOpC.jpg"),
     ("Walt Disney Studios Nederland", "user/WaltDisneyStudiosNL", "http://i.imgur.com/Ui0lVz5.jpg"),
     ("Prinsessia", "user/prinsessiatv", "http://i.imgur.com/Ou2MNZo.jpg"),
     ("Tita Tovernaar", "user/Titatovenaar", "http://i.imgur.com/nQSmo7I.jpg"),
     ("Efteling Raveleijn", "user/Raveleijn", "http://i.imgur.com/2kuMsEf.jpg"),
     ("Bassie en Adriaan", "user/bassieadriaanchannel", "http://i.imgur.com/REyFIga.jpg"),
     ("Amika", "user/AmikaKanaal", "http://i.imgur.com/XRNctz8.jpg"),
     ("Mega Mindy", "user/MegaMindyKanaal", "http://i.imgur.com/dQ8EQn2.jpg"),
     ("Heidi", "user/HeidiKanaal", "http://i.imgur.com/wX7N9kJ.jpg"),
     ("De Smurfen", "channel/UCeR6gZ7LpF-DB-d0clvwY4w", "http://i.imgur.com/wHGEfVH.jpg"),
     ("Oggy", "channel/UCNEKMkg_DG8eAyR1BNWsSvw", "http://i.imgur.com/fBLojgW.jpg"),
     ("Galaxy Park", "user/GalaxyParkKanaal", "http://i.imgur.com/Fzh5SOj.jpg"),
     ],

'muziek':[
     ("Roompot Minidisco", "playlist/PLal1fCW8NLt_pfOpanYsDSWZa9yJ9kHNk", icon),
     ("Sprookjesboom dansvideo's", "playlist/PLGJ8-PwGgVmQo8jXnMDCnAdaVSwi0yJvP", icon),
     ("Mini Disco", "channel/UCaynZO752koKaWub6EDaApA", "http://i.imgur.com/oKIZdmK.jpg"),
     ("Kinderen voor Kinderen", "user/ClubKVK", "http://i.imgur.com/1oho2f6.jpg"),
     ("K3", "user/K3Kanaal", "http://i.imgur.com/NDp5gYX.jpg"),
     ("Dirk Scheele", "user/DirkScheele", "http://i.imgur.com/fJXADSo.jpg"),
     ],

'muziekengels':[
     ("The Piano Guys", "user/ThePianoGuys", icon),
     ("Its JoJo Siwa", "channel/UCeV2O_6QmFaaKBZHY3bJgsA", icon),
     ("MattyBRaps", "user/MattyBRaps", icon),
     ("Angelic", "user/ThisIsAngelic", icon),
     ("Haschak Sisters", "playlist/PLTO6a06fTMaZXWABGhYda411fVh15gIIy", icon),
     ("DisneyStars", "user/DisneyStars", icon),
     ("KIDZ BOP", "user/KidzBopMusicVEVO", icon),
     ("Recess Monkey", "user/recessmonkey3", icon),
     ("childrenlovetosing", "user/childrenlovetosing", icon),
     ("Little Kids Rock", "user/littlekidsrock", icon),
     ],

'engels':[
     ("Art for Kids", "user/ArtforKidsHub", icon),
     ("Mister Maker", "user/mistermaker", icon),
     ("ItsyArtist", "user/itsyartist", icon),
     ("ArtDaniela", "user/ArtDaniela", icon),
     ("batteryPOP", "user/batteryPOPkids", icon),
     ("Play Doh Guide", "user/PeppaPigUK", icon),
     ("MyFroggyStuff", "user/MyFroggyStuff", icon),
     ("Muffalo Potato", "user/muffalopotato", icon),
     ("RosannaPansino", "user/RosannaPansino", icon),
     ("The Pet Collective", "user/ThePetCollective", icon),
     ("Cosmic Kids Yoga", "user/CosmicKidsYoga", icon),
     ("Cute Girls Hairstyles", "user/CuteGirlsHairstyles", icon),
     ("Madnes64", "user/madnes64", icon),
     ("MADABOUTLEGO", "user/MADABOUTLEGO", icon),
     ("Wizz", "channel/UCHzoeK57op5kRPY7baseKaQ", icon),
     ("ErinsAnimals", "user/ErinsHamsters", icon),
     ("Brave Wilderness", "user/BreakingTrail", icon),
     ("Enterprisingengine93", "user/Enterprisingengine93", icon),
     ("Trains!", "user/sklepowich", icon),
     ("Fun2draw", "user/Fun2draw", icon),
     ("NerdECrafter", "user/NerdyCraftsies", icon),
     ],

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