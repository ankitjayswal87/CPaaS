#!/usr/bin/env python3

import sys
import json
import requests
from asterisk.agi import *
import mysql.connector
import os
import constant as ct
import urllib.parse

#mysql connection
mydb = mysql.connector.connect(
  host=ct.HOST,
  user=ct.DBUSER,
  password=ct.DBPASSWORD,
  database=ct.DATABASE
)

#initialising agi
agi = AGI()
agi.verbose("Entering into Python AGI...")
agi.answer()

#receive data from arguments
read_status = sys.argv[1]
press_digit = sys.argv[2]
process_digit_url = urllib.parse.unquote(sys.argv[3])

#just verbose received arguments
agi.verbose('READSTATUS is %s' % sys.argv[1])
agi.verbose('PRESS DIGIT is %s' % sys.argv[2])

if(read_status=='TIMEOUT'):
    agi.verbose('TIMEOUT HAPPENED...')
    press_digit=read_status

#get interface_id from the did_number
#mycursor = mydb.cursor()
#mycursor.execute("SELECT * FROM did_number WHERE did_number="+str(did_number))
#myresult = mycursor.fetchall()
#incoming_url_voice = myresult[0][2]

#agi.verbose('URL is %s' % str(incoming_url_voice))

#Here call API to get recording type setting
payload={}
#post required data here
data = {"digits":press_digit}
response = requests.request("POST", str(process_digit_url),data=payload,json=data)

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
elif(app=='collect'):
    agi.verbose('App is %s' % app)
    agi.set_variable('app',response['response']['app'])
    agi.set_variable('text',response['response']['text'])
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
