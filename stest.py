#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Notify', '0.7')
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')
from gi.repository import Notify,Gtk,Gdk,Keybinder
import requests
import json

key = "trnsl.1.1.20170812T141122Z.7c616ae86afcd2a9.648b19fc570b5bab50563de83902d5bc6eb4dcc7"

def send_notify(app_name,title,text,timeout=5000):
	Notify.init(app_name)
	n = Notify.Notification.new(title, text)
	n.set_timeout(timeout)
	n.show()

def get_selected_text():
	try:
		clipboard = Gtk.Clipboard.get(Gdk.SELECTION_PRIMARY)
		select = clipboard.wait_for_text()
	except:
		return ""
	return  select

def translate(shortcut_key=None):
	text =  get_selected_text().strip()
	if not text: # if len(text) == 0
		return
	
	r=requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang=en-ar".format(key,text)).json()	
	send_notify("MYPROGRAM",text,r["text"][0])
	
	#send_notify("arpytrans",text,result["text"][0]+"\nPowered by Yandex.Translate\nhttp://translate.yandex.com",timeout=notify_timeout)

	

def main():
	Keybinder.init()
	Keybinder.bind("<Alt>J", translate)

	Gtk.main()

main()
