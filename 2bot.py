# -*- coding: utf-8 -*-

import JECKY
from JECKY.lib.curve.ttypes import *
from JECKY.lib.curve.ttypes import Message
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile,glob
import requests
import urllib
import urllib2
import subprocess
import profile
import wikipedia
import requests
import os
from gtts import gTTS
from bs4 import BeautifulSoup
from threading import Thread

cl = JECKY.LINE() #Self
cl.login(token=""
cl.loginResult()

ki = JECKY.LINE() #bot1
ki.login(token=""
ki.loginResult()

ki2 = JECKY.LINE() #bot2
ki2.login(token=""
ki2.loginResult()


print u"Already Running 🎵"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""        
╭════════╬♥╬═════════╮
                   .̲̅.̲̅.̲̅.̲̅ᴅ͎̼̙̲͆̀̅͠ᴋ̙͔̲̈́́͌̅ᴢ̙̳̞̲̒͒̀̅ᵀ͉̼̲́̅͜͝ᴱ̦̫̲͊͆͐̅͜ᴬ͔̫̲͆͐̅̚ᴹ̡͚̲̐̽̔̅ʙ̝̺̻̲͊͊̅ᴏ͕͍͔̲̿̈́̒̅ᴛ̞͉̲͑͋̐̅.̲̅.̲̅.̲̅.̲̅
╰═════════♥══════════╯
╭════════════════════╮
║   🔯🎵ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅ 🎵🔯
║╰═══════════════════╯
║🔯 「 ɪᴅ」
║🔯 「 ᴍᴇ 」
║🔯 「 ʜᴇʟᴘ」
║🔯 「 ᴄᴏᴘʏ」
║🔯 「 ɢɪғᴛ」
║🔯 「 ᴘɪᴄ」
║🔯 「 ᴍɪᴅ」
║🔯 「 ᴍɪᴅ @」
║🔯 「 ɴᴋ 」
║🔯 「 ʟʏʀɪᴄ」
║🔯 「 ᴡɪᴋɪ 」
║🔯 「 ᴀʙᴏᴜᴛ」
║🔯 「 ɪɴsᴛᴀɢʀᴀᴍ 」
║🔯 「 ᴛɪᴍᴇ 」
║🔯 「 ʏᴏᴜᴛᴜʙᴇ 」
║🔯 「 ᴠɪᴅɪᴏ : ᴛᴇxᴛ 」
║🔯 「 sɪᴀᴘᴀ : ᴛᴇxᴛ 」
║🔯 「 ᴅᴏsᴀ : ᴛᴇxᴛ 」
║🔯 「 ᴀᴘᴀᴋᴀʜ : ᴛᴇxᴛ 」
║🔯 「 ᴄᴏᴠᴇʀ」
║🔯 「 ᴍʏɴᴀᴍᴇ 」
║🔯 「 ᴄʀᴇᴀᴛᴏʀ 」
║🔯 「 ᴄᴀɴᴄᴇʟᴀʟʟ 」
║╭════════════════════╮
║🔯        🎵ᴄʜᴀᴛ ʀᴇʟᴀᴛᴇᴅ 🎵    
║╰════════════════════╯
║🔯 「 ᴘᴘ 」
║🔯 「 ᴄᴏᴠᴇʀ 」
║🔯 「 ᴍᴜsɪᴄ」
║🔯 「 ɪᴍᴀɢᴇ」
║🔯 「 ᴍʏᴠɪᴅ 」
║🔯 「 ᴍʏʙɪᴏ 」
║🔯 「 ᴘᴘ ɢʀᴏᴜᴘ」
║🔯 「 ɢʀᴏᴜᴘ ɴᴀᴍᴇ」
║🔯 「 ɢʀᴏᴜᴘ ɪᴅ」
║🔯 「 ɢᴇᴛᴠɪᴅ」
║🔯 「 ɢʙʀᴏᴀᴅᴄᴀsᴛ : ᴛᴇxᴛ」
║🔯 「 ᴄʙʀᴏᴀᴅᴄᴀsᴛ : ᴛᴇxᴛ」
║🔯 「 ᴄʜᴀᴛʙᴏᴛ ᴏɴ/ᴏғғ」
║🔯 「 ʀᴇsᴘᴏɴ1 ᴏɴ/ᴏғғ」
║🔯 「 ʀᴇsᴘᴏɴ2 ᴏɴ/ᴏғғ」
║🔯 「 ʀᴇsᴘᴏɴ3 ᴏɴ/ᴏғғ」
║╭════════════════════╮
║🔯       🎵ᴄᴏᴍᴍᴀɴᴅ ᴍɪᴍɪᴄ🎵   
║╰════════════════════╯
║🔯 「 ᴍɪᴍɪᴄ ᴀᴅᴅ @」
║🔯 「 ᴍɪᴍɪᴄ ᴅᴇʟ @」
║🔯 「 ᴍɪᴍɪᴄʟɪsᴛ」
║🔯 「 ᴍɪᴍɪᴄ ᴏɴ」
║🔯 「 ᴍɪᴍɪᴄ ᴏғғ」
║╭════════════════════╮
║🔯           🎵ᴅᴇsᴛʀᴏʏᴇʀ🎵
║╰════════════════════╯
║🔯 「 ғᴜᴄᴋ @ 」
║🔯 「 ᴋɪʟʟ @」
║🔯 「 ᴄʀᴀsʜ」
║🔯 「 ɴᴜᴋᴇ」
║🔯 「 ᴋɪᴄᴋᴛᴀɢ ᴏɴ/ᴏғғ」
║🔯 「 sᴘᴀᴍᴄʜᴀᴛ @」
║🔯 「 sᴘᴀᴍᴄᴏɴᴛᴀᴄᴛ」
║╭════════════════════╮
║🔯     🎵ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ🎵
║╰════════════════════╯
║🔯 「 ɢᴜʀʟ」
║🔯 「 ᴄᴇᴋ」
║🔯 「 ʀᴇᴀᴅ」
║🔯 「 ɪɴғᴏ 」
║🔯 「 ᴠᴋɪᴄᴋ」
║🔯 「 ᴏᴜʀ」
║🔯 「 ғᴜᴄᴋ」
║🔯 「 ᴋɪʟʟ」
║🔯 「 ɴᴜᴋᴇ」
║🔯 「 ᴄᴜʀʟ」
║🔯 「 sᴇᴛ 」
║🔯 「 ᴍʏʙᴀᴄᴋᴜᴘ 」
║🔯 「 ᴍᴇ @ʙʏᴇ 」
║🔯 「 ʀᴇʙᴏᴏᴛ 」
║🔯 「 ʀᴜɴᴛɪᴍᴇ」
║🔯 「 ᴍᴇᴍʟɪsᴛ」
║🔯 「 ɢɪɴғᴏ」
║🔯 「 ᴄʀᴇᴀᴛᴏʀ 」
║🔯 「 ɢʀᴏᴜᴘs」
║🔯 「 sᴘ/sᴘᴇᴇᴅ 」
║🔯 「 ᴛᴀɢ/ᴀᴛs 」
║🔯 「 ᴄᴀɴᴄᴇʟ」
║🔯 「 ʟɪɴᴋ ᴏɴ/ᴏғғ」
║╭════════════════════╮
║🔯    🎵sᴇᴛ ʙᴀɴᴇᴅ/ᴜɴʙᴀɴᴇᴅ🎵
║╰════════════════════╯
║🔯 「 ʙᴀɴ:ᴏɴ」
║🔯 「 ᴜɴʙᴀɴ:ᴏɴ」
║🔯 「 ʙᴀɴ @」
║🔯 「 ᴜɴʙᴀɴ @」
║🔯 「 ᴄᴇᴋʙᴀɴ」
║🔯 「 ʙᴀɴʟɪsᴛ」
║🔯 「 ʙʟᴏᴄᴋʟɪsᴛ」
║🔯 「 ᴄʟᴇᴀʀʙᴀɴ」
║╭════════════════════╮
║🔯    🎵ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴋɪᴄᴋᴇʀ🎵
║╰════════════════════╯
║🔯 「 ᴘɪɴɢ」
║🔯 「 ᴍᴀsᴜᴋ/ᴊᴏɪɴ」
║🔯 「 ᴘᴜʟᴀɴɢ/ʙʏᴇ」
║🔯 「 ʙᴏᴛ1 - ʙᴏᴛ2 ʙʏᴇ」
║🔯 「 ᴀʟʟɢɪғᴛ 」
║🔯 「 ʙᴏᴛ1 - ʙᴏᴛ2 ɢɪғᴛ 」
║🔯 「 ʀᴇsᴘᴏɴs」
║🔯 「 ɴᴜᴋᴇ」
║🔯 「 1ɴᴀᴍᴇ - 2ɴᴀᴍᴇ」
║🔯 「 ᴀʟʟ ᴍɪᴅ 」
║🔯 「 ᴍʏʙᴏᴛ 」
║🔯 「 ʙᴀᴄᴋᴜᴘ 」
║🔯 「 ʙʏᴇ ᴀʟʟɢʀᴏᴜᴘ」
║╭════════════════════╮
║🔯        🎵sᴇᴛᴛɪɴɢs ᴏɴʟʏ🎵
║╰════════════════════╯
║🔯 「 sɪᴅᴇʀ ᴏɴ/ᴏғғ」
║🔯 「 ʀᴇsᴘᴏɴ1 ᴏɴ/ᴏғғ」
║🔯 「 ʀᴇsᴘᴏɴ2 ᴏɴ/ᴏғғ」
║🔯 「 ʀᴇsᴘᴏɴ3 ᴏɴ/ᴏғғ」
║🔯 「 ᴡᴇʟᴄᴏᴍᴇ ᴏɴ/ᴏғғ」
║🔯 「 ᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ 」
║🔯 「 sʜᴀʀᴇ ᴏɴ/ᴏғғ 」
║🔯 「 ᴋɪᴄᴋᴛᴀɢ ᴏɴ/ᴏғғ 」
║🔯 「 ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ/ᴏғғ」
║🔯 「 ᴄᴏɴᴛᴀᴄᴛ ᴏɴ/ᴏғғ」
║🔯 「 ᴀᴜᴛᴏᴊᴏɪɴ ᴏɴ/ᴏғғ」
║🔯 「 ᴀᴜᴛᴏᴄᴀɴᴄᴇʟ ᴏɴ/ᴏғғ」
║🔯 「 ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏɴ/ᴏғғ」
║🔯 「 ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ」
║🔯 「 ɪɴᴠɪᴛᴇᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ」
║🔯 「 ᴄᴀɴᴄᴇʟᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ」
╰════════════════════╯
╭════════════════════╮
              ❨♪ ʙᴏᴛs ᴠ1.09 ♪❩
╰════════════════════╯
╭════════╬♥╬════════╮
          ̶ ̶ ̶ ̶ ̶ ̶̶ ̶ ̶ ̶̶ ̶̶ ̶s̶ᴜ̶ᴘ̶ᴘ̶ᴏ̶ʀ̶ᴛ̶ᴇ̶ᴅ̶ ̶ʙ̶ʏ̶ ̶ ̶ ̶ ̶ ̶ ̶̶ ̶ ̶ ̶̶ ̶̶ ̶
                  ŧ€₳ᴍжħ₳ʗҝ฿❂ŧ
          ❨  🚘 ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ 🚘 ❩             
╰════════╬♥╬════════╯
"""""
helo=""

KAC=[cl,ki,ki2]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
Bots = [mid,kimid,ki2mid]
admsa = ""
admin = ""

mulai = time.time()

wait = {
    "likeOn":False,
    "alwaysRead":False,
    "detectMention":False,    
    "detectMention2":False,
    "detectMention3":False,
    "kickMention":False,
    "duedate":{},
    "steal":True,
    'pap':{},
    'invite':{},
    "spam":{},
    "sider":{},
    "members":1,
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":50},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'alwayRead':False,
    "detectMention":False,
    'point':False,
    'sidermem':False,
    'message':"Thanks For add : By Team Dkz",
    "lang":"JP",
    "comment":"Thanks For add : By Team Dkz",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "winvite":False,
    "cyduk":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "displayname":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "rblacklist":False,
    "rdblacklist":False,
    "mid":{},
    "protect":False,
    "sendMessage":True,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "welcome":False,
    "re":False
    
    
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{},
    }
    
settings = {
    "simiSimi":{}
    }
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

res = {
    'num':{},
    'us':{},
    'au':{},
    }
    
setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup = ki2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def tagall(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "✮ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
      cl.sendMessage(msg)
    except Exception as error:
      print error
      
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
    
      
  #Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"    
            
def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()      
      
def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': objectId,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudio(self, to_, path):
        M = Message(to=to_,contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True
        
def sendAudioWithURL(self, to_, url):
        path = 'pythonLiness.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e

def waktu(secs):
      mins, secs = divmod(secs,60)
      hours, mins = divmod(mins,60)
      return '[ %02d : Jam 🎵 %02d : Menit 🎵 %02d : Detik ]' % (hours, mins, secs)
       

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
  
            
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e    
  
            if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Hallo " + "👉 " + Name + " 👈" + "\nCie cie yang jones ngintip aja cie . . .\nSini napa nes 😕")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        cl.sendText(op.param1, "Hallo " + "👉 " + Name + " 👈" + "\nBisulan tujuh turunan cctv telus . . .\Bintitan lu 😕 ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    cl.sendText(op.param1, "Hallo " + "👉 " + Name + " 👈" + "\nKak ngapain ngintip ? \nSini Dong ih.. 😕  ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass   

            pass        
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "" + data['result']['response'].encode('utf-8'))     
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + " Maaf aku lagi sibuk , ", cName + " Yang tag bisulan amin ",  cName + " Apasih kak? ganggu aku lagi tidur aja  ", "Maaf aku lagi nikung jangan ganggu, " + cName + "?","Au ah tag mulu, ", "Lagi anu kak tanggung mau keluar, "]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas =["Nama,: " + cName + ",\nKasus, : Tukang Tag Orang,\nHukuman, : Tari Bugil,\n\nProfil Saya Pajang Dibawah 👇"]
                    balas0 = "Potonya 👇"
                    balas1 = "Cover Nya 👇"
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    cu = cl.channel.getCover(msg.from_)          
                    path = str(cu)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:                       	     
                                  cl.sendText(msg.to,ret_)
                                  cl.sendText(msg.to,balas0)
                                  cl.sendImageWithURL(msg.to,image)  
                                  cl.sendText(msg.to,balas1)
                                  cl.sendImageWithURL(msg.to, path)                              
                                  break     

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Males Gue di tag mulu ma si " + cName]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                                  cl.sendMessage(msg)    
                                  msg.contentType = 7   
                                  msg.text = None   
                                  msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}    
                                  cl.sendMessage(msg)
                                  msg.contentType = 7
                                  msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                                  msg.text = None
                                  cl.sendMessage(msg)
                                  break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + " Maaf ", cName + " Minta Dikick ya  " + cName + "Ini Balasan Untukmu Yang Tag", "Fakyu " + cName + "Oke Saya Kick","Saya Bilang Jangan Tag", "Kena Kau"]
                     ret_ = "[Auto Kicktag Aktif] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break           
            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)      
            if msg.contentType == 13:
                  if msg.from_ in admin:
                    if wait["wblacklist"] == True:
                       if msg.contentMetadata["mid"] in wait["blacklist"]:
                         cl.sendText(msg.to,"Is already banned")
                       wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"has been banned by :")

            elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                       del wait["blacklist"][msg.contentMetadata["mid"]]
                       cl.sendText(msg.to,"Has been Unbanned deleted by :")
                       wait["dblacklist"] = False

                    else:
                       wait["dblacklist"] = False
                       kk.sendText(msg.to,"is not in banned!")
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)        
        if op.type == 17:
          if wait["welcome"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"ʜᴀʟʟᴏ 👉" + cl.getContact(op.param2).displayName + "\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ 👉" + str(ginfo.name) + " 👈" + "\nsɪʟᴀʜᴋᴀɴ ᴄᴇᴋ ɴᴏᴛᴇ......\nsᴀʟᴀᴍ ᴋᴇɴᴀʟ ʏᴀ......\nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴄᴀʀɪ ᴛɪᴋᴜɴɢᴀɴ.....\n\n❨ ᴛɪᴍᴇ : "+  datetime.now().strftime('%H:%M:%S ❩') +"\n❨ ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ❩")
            cl.sendText(op.param1, "ᴏᴡɴᴇʀ ɢʀᴏᴜᴘ 👉" + str(ginfo.name) +"\n👉 : " + ginfo.creator.displayName)
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)  
            summon(op.param1,[op.param2])
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER HAS LEFT THE GROUP"
        if op.type == 15:
            if op.param2 in admin:
                return
            cl.sendText(op.param1, "ɢᴏᴏᴅ ʙʏᴇ 🎵" + cl.getContact(op.param2).displayName + "\nsᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ʏᴀ..... \nsᴜᴋsᴇs sᴇʟᴀʟᴜ ʙᴜᴀᴛᴍᴜ.....\nsᴀᴍᴘᴀɪ ᴊᴜᴍᴘᴀ ᴅᴀᴅᴀʜ.....\n🙌🙌🙌🙌🙌 \n\n❨ ᴛɪᴍᴇ : "+  datetime.now().strftime('%H:%M:%S ❩') +"\n❨ ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ❩")
            print "MEMBER HAS LEFT THE GROUP" 
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u7099fa4af6676fcae8fac00bcc388143":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
                           
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         cl.findAndAddContactsByMid(invite)
                                         cl.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Contact is ready in blacklist♪")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Contact has been make to Blacklist♪")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Contact has been deleted to Blacklist ♪")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Nothing in banlist♪")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return

 #---------------------------------------------------------
 
            elif msg.text in ["Key","View","Help"]:
                cl.sendText(msg.to,helpMessage)
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
 #---------------------------------------------------------         
            elif msg.text in ["Pp","pp"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
         
            elif msg.text in ["Cover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
                    
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"••••••••••[StatusMessage]••••••••••\n" + h.statusMessage)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
 
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
                 
        #==================================================
            elif 'lyric ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif 'wiki ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))  
            elif 'instagram ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "__________Info Profile__________\n"
                    details = "\n__________Info Profile__________"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
                
            elif "Time" in msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))   
                  
            elif "youtube " in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
                       
            elif 'Vidio ' in msg.text:
	      if msg.from_ in admin:
                try:
                    textToSearch = (msg.text).replace('Vidio ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    cl.sendVideoWithURL(msg.to,ght)
                except:
                    cl.sendText(msg.to,"Could not find it")      
                    
            elif "Siapa " in msg.text:
    		tanya = msg.text.replace("Siapa ","")
    		jawab = ("Itu anak tetangga sebelah nyolong ayam","Biasa bro orang edan")
    		jawaban = random.choice(jawab)
		tts = gTTS(text=jawaban, lang='id')
		tts.save('tts.mp3')
    		cl.sendAudio(msg.to,'tts.mp3')
    

#==========================================
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("Banyak banget bro","Dosa dia segunung","70 % kuadarat","Gak usah tanya diamah pawang dosa bro","Hahaha dosa dia segudang")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                cl.sendText(msg.to,"Dosanya dia cek suara di bawah ")
                cl.sendAudio(msg.to,'tts.mp3')    
                
            
            elif "Apakah " in msg.text:
                apk = msg.text.replace("Apakah ","")
                rnd = ["Mana Gua Tau","Palamu Botak","Apa yang lagi kau pikirkan dasar jones"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")         
#---------------------------------------------------------
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
 #---------------------------------------------------------
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
                    
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
                
            elif "Pp group" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)    
#---------------------------------------------------------
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
#---------------------------------------------------------
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#---------------------------------------------------------          
            elif msg.text.lower() == 'mybot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
#---------------------------------------------------------
            
            elif "Bot1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Bot2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
#---------------------------------------------------------
            
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            
            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)
                 
                
            elif msg.text.lower() == 'allgift':
            	msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                

            elif msg.text in ["B Cancel","Cancel dong","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
#---------------------------------------------------------

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
    #---------------------------------------------------------            
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
 #---------------------------------------------------------
 
            elif "Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
               
 #---------------------------------------------------------        
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Bot1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Bot2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
             
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
 #---------------------------------------------------------
 
            elif "Reboot" in msg.text:
                print "[Command]Reboot"
                try:
                 cl.sendText(msg.to,"I'Il come back later")
                 cl.sendText(msg.to,"Restarted done 🎵")
                 restart_program()
                except:
                 cl.sendText(msg.to,"Please wait")
                restart_program()
                pass
 
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
              #---------------------------------------------------------
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
             #---------------------------------------------------------       
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to," Done Update Name " + string + "👈")

#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag","Ats","Hem","Muach"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                  if jml <= 100:
                      tagall(msg.to, nama)
                  if jml > 100 and jml < 500:
                      for i in range(0,99):
                          nm1 += [nama[i]]
                      tagall(msg.to, nm1)
                      for j in range(100, len(nama)-1):
                          nm2 += [nama[j]]
                      tagall(msg.to, nm2)
                      for k in range(200, len(nama)-1):
                          nm3 += [nama[k]]
                      tagall(msg.to, nm3)
                      for l in range(300, len(nama)-1):
                          nm4 += [nama[l]]
                      tagall(msg.to, nm4)
                      for m in range(400, len(nama)-1):
                          nm5 += [nama[m]]
                      tagall(msg.to, nm5)
                  cnt = Message()
                  cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                  cnt.to = msg.to
                  cl.sendMessage(cnt)
                  cl.sendText(msg.to,"❨ᴍᴇɴᴛɪᴏɴᴇs ʙʏ : 🤖 ᵈᵏᶻᴘʀᴏᴛᴇᴄᴛɪᴏɴ™ 🤖❩")
                  if jml > 500:
                      cnt = Message()
                      cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                      cnt.to = msg.to
                      cl.sendMessage(cnt)
                      cl.sendText(msg.to,"❨ᴍᴇɴᴛɪᴏɴᴇs ʙʏ : 🤖 ᵈᵏᶻᴘʀᴏᴛᴇᴄᴛɪᴏɴ™ 🤖❩")
#-------------Fungsi Tag All Finish---------------#
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
#---------------------------------------------------------
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           

            elif "Gbroadcast: " in msg.text:
                bc = msg.text.replace("Gbroadcast: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.sendText(i, bc)
                    
            elif "Cbroadcast: " in msg.text:
                bc = msg.text.replace("Cbroadcast: ","")
                gid = cl.getAllContactIds()
                for i in gid:
                    cl.sendText(i, bc)
#---------------------------------------------------------
            elif "1name:" in msg.text:
                string = msg.text.replace("1name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to," Done Update Name " + string + "👈")

            elif "2name:" in msg.text:
                string = msg.text.replace("2name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to," Done Update Name " + string + "👈")
                    
            
#---------------------------------------------------------
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
#---------------------------------------------------------
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already off 🎵")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off 🎵")
                    else:
                        cl.sendText(msg.to,"Already off 🎵")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off 🎵")
                    else:
                        cl.sendText(msg.to,"Already off 🎵")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
            elif msg.text.lower() == 'linkprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵 ")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
            elif msg.text.lower() == 'autojoin on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵 ")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")

 #---------------------------------------------------------
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text in ["Allprotect on","Mode on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")      
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Allprotect on done")
            elif msg.text in ["Allprotect off","Mode Off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                    else:
                        cl.sendText(msg.to,"Invite OFF")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")      
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text.lower() == 'autojoin off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set off 🎵")
                    else:
                        cl.sendText(msg.to,"Autojoin set off 🎵")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set off 🎵")
                    else:
                        cl.sendText(msg.to,"Autojoin set off 🎵")
                        
            elif msg.text in ["Chatbot on","Chatbot:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Chatbot mode On")
                
            elif msg.text in ["Chatbot off","Chatbot:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Chatbot mode Off")  
                   
            elif msg.text in ["Respon1 on"]:
                wait["detectMention"] = True
                cl.sendText(msg.to,"Autorespon1 Tag Dkz Aktif ")
              
            elif msg.text in ["Respon1 off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"Autorespon1 Tag Dkz Off")
                
            elif msg.text in ["Respon2 on"]:
                wait["detectMention2"] = True
                cl.sendText(msg.to,"Autorespon2 Image Dkz Aktif ")
              
            elif msg.text in ["Respon2 off"]:
                wait["detectMention2"] = False
                cl.sendText(msg.to,"Autorespon2 Image Dkz Off")
                
            elif msg.text in ["Respon3 on"]:
                wait["detectMention3"] = True
                cl.sendText(msg.to,"Autorespon3 Sticker Dkz Aktif ")
             
            elif msg.text in ["Autolike on"]:
                wait["likeOn"] = True
                cl.sendText(msg.to,"Autolike Already on 🎵")
                
            elif msg.text in ["About"]:
                wait["duedate"] = False
                cl.sendText(msg.to,"Impormation Selbots :\n\nType : Selfbots\nVersion : V1.09\nCreator : JP\nMasa Aktif Sampai : Cek List Creator" +" \n\nline.me/ti/p/~dekradakz\n❨ ᴛɪᴍᴇ : "+  datetime.now().strftime('%H:%M:%S ❩'))  
              
            elif msg.text in ["Autolike off"]:
                wait["likeOn"] = False
                cl.sendText(msg.to,"Autolike Already Off")
                
            elif msg.text in ["Respon3 off"]:
                wait["detectMention3"] = False
                cl.sendText(msg.to,"Autorespon3 Sticker Dkz Off")  
                
            elif msg.text in ["Kicktag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"Autokick Tag Dkz Aktif")
                
            elif msg.text in ["Kicktag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"Autokick Tag Dkz Off")
            elif "Time" in msg.text:
              if msg.toType == 2:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
                  
            elif msg.text in ["Autoread off","Read:off"]:
               if wait["cyduk"] ==False:
               	if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Auto read Off")
               else:
                 if wait["cyduk"] == False:
                	if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Auto read Off")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set off 🎵")
                    else:
                        cl.sendText(msg.to,"Protect set off 🎵")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set off 🎵")
                    else:
                        cl.sendText(msg.to,"It is already open ")
            elif msg.text in ["Linkprotect off","linkprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Linkprotect set off 🎵")
                    else:
                        cl.sendText(msg.to,"Linkprotect set off 🎵")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Linkprotect set off 🎵")
                    else:
                        cl.sendText(msg.to,"Linkprotect set off 🎵")
            elif msg.text in ["Wc on","Welcome on"]:
                if wait["welcome"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                else:
                    wait["welcome"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Wc off","Welcome off"]:
                if wait["welcome"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off 🎵")
                else:
                    wait["welcome"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off 🎵")   
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Inviteprotect set off 🎵")
                    else:
                        cl.sendText(msg.to,"Inviteprotect set off 🎵")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Inviteprotect set off 🎵")
                    else:
                        cl.sendText(msg.to,"It is already open ")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancelprotect set off 🎵")
                    else:
                        cl.sendText(msg.to,"Cancelprotect set off 🎵")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancelprotect set off 🎵")
                    else:
                        cl.sendText(msg.to,"Cancelprotect set off 🎵")
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Autoleave on","Autoleave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
            elif msg.text in ["Autoleave off","Autoleave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoleave set off 🎵")
                    else:
                        cl.sendText(msg.to,"Autoleave set off 🎵")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoleave set off 🎵")
                    else:
                        cl.sendText(msg.to,"Autoleave set off 🎵")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set off 🎵")
                    else:
                        cl.sendText(msg.to,"Share set off 🎵")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set off 🎵")
                    else:
                        cl.sendText(msg.to,"Share set off 🎵")

            elif msg.text.lower() == 'set':
                md ="____________________________\n┃❨❄  Settings Only  ❄❩\n┃____________________________\n"                                                                                      
                if wait["contact"] == True: md+="┃•❄Contact on  🎵\n"
                else: md+="┃•❄Contact off  🎵\n"
                if wait["autoJoin"] == True: md+="┃•❄Autojoin on 🎵\n"
                else: md +="┃•❄Autojoin off 🎵\n"
                if wait["autoCancel"]["on"] == True:md+="┃•❄Autocancel:" + str(wait["autoCancel"]["members"]) + " 🎵\n"
                else: md+= "┃•❄Autocancel off 🎵\n"
                if wait["leaveRoom"] == True: md+="┃•❄Autoleave on 🎵\n"
                else: md+="┃•❄Autoleave off 🎵\n"
                if wait["timeline"] == True: md+="┃•❄Share on 🎵\n"
                else:md+="┃•❄Share off 🎵\n"
                if wait["autoAdd"] == True: md+="┃•❄Autoadd on 🎵\n"
                else:md+="┃•❄Autoadd off 🎵\n"
                if wait["protect"] == True: md+="┃•❄Protect on 🎵\n"
                else:md+="┃•❄Protect off🎵\n"
                if wait["linkprotect"] == True: md+="┃•❄Linkprotect on 🎵\n"
                else:md+="┃•❄Linkprotect off 🎵\n"
                if wait["inviteprotect"] == True: md+="┃•❄Inviteprotect on 🎵\n"
                else:md+="┃•❄Inviteprotect off 🎵\n"
                if wait["welcome"] == True: md+="┃•❄Welcome on 🎵\n"
                else:md+="┃•❄Welcome off 🎵\n" 
                if wait["detectMention"] == True: md+="┃•❄Respon1 on 🎵\n"
                else:md+="┃•❄Respon1 off 🎵\n" 
                if wait["detectMention2"] == True: md+="┃•❄Respon2 on 🎵\n"
                else:md+="┃•❄Respon2 off 🎵\n"  
                if wait["detectMention3"] == True: md+="┃•❄Respon3 on 🎵\n"
                else:md+="┃•❄Respon3 off 🎵\n"  
                if wait["sider"] == True: md+="┃•❄Sider on 🎵\n"
                else:md+="┃•❄Sider off 🎵\n" 
                if wait["kickMention"] == True: md+="┃•❄Kicktag on 🎵\n"
                else:md+="┃•❄Kicktag off 🎵\n" 
                if wait["likeOn"] == True: md+="┃•❄Autolike on 🎵\n"
                else:md+="┃•❄Autolike off 🎵\n" 
                if wait["cancelprotect"] == True: md+="┃•❄Cancel Protect on 🎵\n"
                else:md+="┃•❄Cancel Protect off 🎵\n┃____________________________\n            ❨ ᴛɪᴍᴇ : "+  datetime.now().strftime('%H:%M:%S ❩') +"\n           ❨ ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ❩"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                
                
            elif msg.text.lower() == 'runtime':
             eltime = time.time() -mulai
             van = "( Myself sudah berjalan selama )\n" +waktu(eltime)
             cl.sendText(msg.to,van)
#---------------------------------------------------------
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                h = cl.getContact(mid)
                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid':"u7099fa4af6676fcae8fac00bcc388143"}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"😎 Kill you 😎")
                
            elif msg.text in ["Me @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
			cl.sendText(msg.to,"See you all 🙌")
                        cl.leaveGroup(msg.to)
                    except:
                        pass        
      #---------------------------------------------------------          
            elif msg.text in ["Cancelall"]:
                if msg.from_ in admin:
                  gid = cl.getGroupIdsInvited()
                  for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"Eror")	
                    

                    
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"Sider Dkz Already On")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Sider Dkz Already Off")
                    
            
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Bye Allgroup"]:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
                    
            elif msg.text in ["Clear ban","Clearban"]:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Removed banlist user target succes.")       
                    
            
                    
            elif msg.text in ["Autoadd on","Autoadd:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on 🎵")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
            elif msg.text in ["Autoadd off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoadd set off 🎵")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoadd set off 🎵")
                    else:
                        cl.sendText(msg.to,"Autoadd set off 🎵")
            
            
            
            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")              
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Bot1 gurl" in msg.text:
                if msg.toType == 1:
                    gid = msg.text.replace("gurl","")
                    gurl = ki.reissueGroupTicket(gid)
                    ki.sendText(msg.to,"line://ti/g" + gurl)
                else:
                    ki.sendText(msg.to,"error")

            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki3.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki3.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)


            elif msg.text == "Cek":
                    cl.sendText(msg.to, "ᴍᴇʀᴇᴋᴀᴍ ᴘᴀʀᴀ ᴊᴏɴᴇs...")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text in ["Glist","Groups","Group"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠○⏩ %s\n" % (cl.getGroup(i).name +"➡["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"╠══════════════════\n╠ 👑👑👑 My Group 👑👑👑\n╠══════════════════\n"+ h +"\n👑 Total Group 👑 = " +""+str(len(gid))+"")

            elif msg.text == "Read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "__________________________________\n🍮 ᴄᴄᴛᴠ ᴛᴇʀᴛᴀɴɢᴋᴀᴘ ʙᴀsᴀʜ 🍮%s\n\n\n\n__________________________________\n🍮 ᴊᴏɴᴇsᴛ ᴛᴇʟᴀʜ ᴛᴇʀᴄɪᴅᴜᴋ 🍮\n%s\n\n\n__________________________________\n•sᴜᴘᴏʀᴛᴇᴅ ᴛᴇᴀᴍ ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ•\n🍮%s am🍮"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
                        
                        
	
#-----------------------------------------------------------

            elif ("Fuck " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Vk " in msg.text:                  
                       nk0 = msg.text.replace("Beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Good Bye")

#----------------------------------------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki.findAndAddContactsByMid(msg.from_)
                            ki.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#-----------------------------------------------------------
                          #=====================================
            elif "Spam chat @" in msg.text:
                if msg.toType == 2:
                  bctxt = msg.text.replace("Spam chat @", "")
                  t = cl.getAllContactIds()
                  t = 500
                  while(t):
                    cl.sendText(msg.to, (bctxt))
                    t-=1
#==============================================

            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
                       
            elif 'Say' in msg.text:
                 psn = msg.text.replace("Say ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')          
                        
            elif ("Mimic add " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target Aded")
                        break
                    except:
                        cl.sendText(msg.to,"Aded")
                        break
                    
            elif ("Mimic del " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target Deleted")
                        break
                    except:
                        cl.sendText(msg.to,"Deleted")
                        break
                    
            elif msg.text in ["Mimic list"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Mimic Mode On")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Mimic Mode Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
            elif "Hay @" in msg.text:
                _name = msg.text.replace("Hay @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")  
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"

            elif "Hallo " in msg.text:
                midd = msg.text.replace("Hallo ","")
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,[miid] + "Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#-----------------------------------------------------------)
            
#-----------------------------------------------------------

            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
                                    

            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki2.updateDisplayPicture(backup.pictureStatus)
                    ki2.updateProfile(backup)
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------<------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------

            
            elif msg.text in ["Sp","Speed"]:
                cl.sendText(msg.to,str(time.time()/100000000000.0) + ' secconds')
                ki.sendText(msg.to,str(time.time()/100000000000.0) + ' secconds')
                ki2.sendText(msg.to,str(time.time()/100000000000.0) + ' secconds')
                
            elif "friendpp: " in msg.text:
              if msg.from_ in admin:
                suf = msg.text.replace('friendpp: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == suf:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)

            elif "Checkmid: " in msg.text:
                saya = msg.text.replace("Checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                cl.sendMessage(msg)
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Checkid: " in msg.text:
                saya = msg.text.replace("Checkid: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).id
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="\n╠══════════════════\n╠○⏩Members List\n╠══════════════════"
                for ids in group:
                    msgs+="\n╠○⏩%i ❩ %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal Members In The Group : %i" % len(group)
                cl.sendText(msg.to, msgs)
                cl.sendText(msg.to,"❨ʙʏ : 🤖 ᵈᵏᶻᴘʀᴏᴛᴇᴄᴛɪᴏɴ™ 🤖❩")
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="═════════List Friend Mid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════List Friend Mid═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)  
#-----------------------------------------------------------
            elif msg.text.lower() == 'respons':
                profile = ki.getProfile()
                text = profile.displayName + " 😎 "
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + " 😎 "
                ki2.sendText(msg.to, text)
#-------------------------------------------------------------------

#------------------------------------------------------------------	
            elif "Cover @" in msg.text:            
                print "[Command]Cover executing"
                _name = msg.text.replace("Cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]Cover executed"			
#------------------------------------------------------------------
            elif "Pic @" in msg.text:            
                print "[Command]Pic executing"
                _name = msg.text.replace("Pic @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]Pic executed"			
 #------------------------------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            #---------------------------------------------BANED
            elif "Ban @" in msg.text:   #jadi
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,_nametarget + " has been banned succes")
                            except:
                                cl.sendText(msg.to,"Error")                                
            elif "Unban @" in msg.text:  #jadi
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,_nametarget + " has been unbaned succes.")
                            except:
                                cl.sendText(msg.to,_nametarget + " There was no blacklist user")
                                                         
#------------------------------- COVER BY TAG -------------------------------
            elif ("Proban:on " in msg.text):
              if msg.from_ in admin:
                 if msg.toType == 2:
                     print "[BL]Ok"
                     key = eval(msg.contentMetadata["MENTION"])
                     key["MENTIONEES"][0]["M"]
                     targets = []
                     for x in key["MENTIONEES"]:
                         targets.append(x["M"])
                     for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Has been banned succes..")
                        except:
                            pass
            elif ("Prounban:on " in msg.text):
              if msg.from_ in creator:
                 if msg.toType == 2:
                     print "[WL]Ok"
                     key = eval(msg.contentMetadata["MENTION"])
                     key["MENTIONEES"][0]["M"]
                     targets = []
                     for x in key["MENTIONEES"]:
                         targets.append(x["M"])
                     for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Has been unbaned succes...")
                        except:
                            pass
                            
            elif msg.text in ["Ban:on","Ban on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send a contact to hass banned")
            elif msg.text in ["Unban:on","Unban on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send a contact to hass unbanned")

            elif msg.text in ["Ban on repeat","Ban:on repeat"]:
                wait["rblacklist"] = True
                cl.sendText(msg.to,"Send a contact to hass banned")
            elif msg.text in ["Unban on repeat","Unban:on repeat"]:
                wait["rdblacklist"] = True
                cl.sendText(msg.to,"Send a contact to hass unbanned")
					
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to, "Not user banlist")
                else:
                    num=1
                    mc = "User Banlist \n________________________\n"
                    for mi_d in wait["blacklist"]:
                        mc += "%i. %s\n" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    mc += "\n\n「%i」 User banlist add" % len(wait["blacklist"])
                    cl.sendText(msg.to, mc)
            elif msg.text in ["Cekban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                       cl.sendText(msg.to, "Not user banlist in the groups")
                       return
                    num=1
                    cocoa = "User banlist in the groups\n________________________\n"
                    for mm in matched_list:
                        cocoa += "%i. %s\n" % (num, cl.getContact(mm).displayName)
                        num=(num+1)
                    cocoa += "\n\n「%i」User banlist in the groups" % len(matched_list)
                    cl.sendText(msg.to, cocoa)
#========================print===========
            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Nuke" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuke","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    ki.sendText(msg.to,"Just some casual cleansing ")
                    ki2.sendText(msg.to,"Group cleansed.")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        ki2.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Group cleanse")
                                ki2.sendText(msg,to,"Group cleanse")


            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
                    
            elif "Vkick" in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                                    try:
                                        cl.kickoutFromGroup(msg.to,[target])
                                        cl.inviteIntoGroup(msg.to,[target])
                                        cl.cancelGroupInvitation(msg.to,[target])
                                    except:
                                        cl.sendText(msg.to, "Error")    
    
            elif msg.text in ["Canceall"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"Done")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
                    


                       
#-----------------------------------------------
            elif msg.text in ["Masuk","Join"]:
                if msg.from_ in admsa:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2),
                        
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text.lower() == 'Sp come':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Bot1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Bot2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#---------------------------------------------
#-----------------------------------------------
            elif msg.text in ["Pulang","Bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki2.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = ki2.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass

#-----------------------------------------------


            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Sayang say " in msg.text:
				bctxt = msg.text.replace("Sayang say ","")
				ki2.sendText(msg.to,(bctxt))
            elif "say" in msg.text:
              if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				
				
            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Pong 🤣")
                ki2.sendText(msg.to,"Pong 🤣")

#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki1mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki1mid:
                        G = ki1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
            except:
                pass

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki4.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n-> " + Nama
                        wait2['ROM'][op.param1][op.param2] = "-> " + Nama
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()



while True:
    bot(cl.Poll.stream(0000000))