#!/usr/bin/env python3

import sys
import json
import requests
from asterisk.agi import *
import mysql.connector
import os
import constant as ct
import urllib.parse

#initialising agi
agi = AGI()
agi.verbose("Entering into Python AGI...")
agi.answer()

#receive data from arguments
call_id = sys.argv[1]
did_number = sys.argv[2]
caller = sys.argv[3]
account_id = sys.argv[4]
bot_status = sys.argv[5]
intent = sys.argv[6]
entity_name = sys.argv[7]
entity_value = sys.argv[8]
action_url = urllib.parse.unquote(sys.argv[9])
entities = sys.argv[10]

#just verbose received arguments
agi.verbose('INTENT is %s' % sys.argv[6])
agi.verbose('ENTITY NAME is %s' % sys.argv[7])
agi.verbose('ENTITY VALUE is %s' % sys.argv[8])
agi.verbose('ACTION URL is %s' % sys.argv[9])

#Here call API to get recording type setting
payload={}
#post required data here
call_data = {"account_id":account_id,"call_id":call_id,"caller":caller,"did_number":did_number,"callee":"","bot_status":bot_status,"intent":intent,"entity_name":entity_name,"entity_value":entity_value,"entities":entities}
response = requests.request("POST", str(action_url),data=payload,json=call_data)

response = json.loads(response.text)
app = response['response']['app']

if(app=='play'):
    agi.verbose('App is %s' % app)
    agi.set_variable('app',response['response']['app'])
    agi.set_variable('url',response['response']['url'])
elif(app=='say'):
    agi.verbose('App is %s' % app)
    agi.set_variable('app',response['response']['app'])
    agi.set_variable('text',response['response']['text'])
    if "voice" in response['response'] and response['response']['voice']!='':
        agi.set_variable('voice',response['response']['voice'])
    else:
        agi.set_variable('voice','en-US-JennyNeural')
elif(app=='collect'):
    agi.verbose('App is %s' % app)
    agi.set_variable('app',response['response']['app'])
    agi.set_variable('text',response['response']['text'])
    if "voice" in response['response'] and response['response']['voice']!='':
        agi.set_variable('voice',response['response']['voice'])
    else:
        agi.set_variable('voice','en-US-JennyNeural')
    agi.set_variable('action',response['response']['action'])
    agi.set_variable('timeout',response['response']['timeout'])
    agi.set_variable('attempts',response['response']['attempts'])
    agi.set_variable('numdigits',response['response']['numdigits'])
elif(app=='dial_number'):
    agi.verbose('App is %s' % app)
    agi.set_variable('app',response['response']['app'])
    numbers = response['response']['numbers']
    numbers=numbers.split(",")
    dial_string=''
    trunk_name='kamtrunk'
    for num in numbers:
        dial_string+="PJSIP/"+num+"@"+trunk_name+"&"
    dial_string = dial_string.rstrip('&')
    agi.set_variable('numbers',dial_string)
    agi.set_variable('action',response['response']['action'])
    agi.set_variable('timeout',response['response']['timeout'])
elif(app=='dial_sip'):
    agi.verbose('App is %s' % app)
    agi.set_variable('app',response['response']['app'])
    agents = response['response']['agents']
    agents = agents.split(",")
    dial_string=''
    for agnt in agents:
        dial_string+="PJSIP/"+agnt+"&"
    dial_string = dial_string.rstrip('&')
    agi.set_variable('agents',dial_string)
    agi.set_variable('action',response['response']['action'])
    agi.set_variable('timeout',response['response']['timeout'])
elif(app=='voicemail'):
    agi.verbose('App is %s' % app)
    agi.set_variable('app',response['response']['app'])
    agi.set_variable('text',response['response']['text'])
    if "voice" in response['response'] and response['response']['voice']!='':
        agi.set_variable('voice',response['response']['voice'])
    else:
        agi.set_variable('voice','en-US-JennyNeural')
    agi.set_variable('maxduration',response['response']['maxduration'])
    agi.set_variable('action',response['response']['action'])
    agi.set_variable('errortext',response['response']['errortext'])
    agi.set_variable('successtext',response['response']['successtext'])
elif(app=='voicebot'):
    agi.verbose('App is %s' % app)
    agi.set_variable('app',response['response']['app'])
    agi.set_variable('text',response['response']['text'])
    if "voice" in response['response'] and response['response']['voice']!='':
        agi.set_variable('voice',response['response']['voice'])
    else:
        agi.set_variable('voice','en-US-JennyNeural')
    agi.set_variable('silence',response['response']['silence'])
    agi.set_variable('minspeaktime',response['response']['minspeaktime'])
    agi.set_variable('action',response['response']['action'])
    #agi.set_variable('timeouttext',response['response']['timeouttext'])
