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
record_status = sys.argv[5]
recorded_file = sys.argv[6]
voicemail_recording_url = urllib.parse.unquote(sys.argv[7])

recorded_file = os.path.basename(recorded_file)
recorded_file = ct.BUCKET_URL+str(recorded_file)+".wav"

#Here call API to get json app response
payload={}
call_data = {"account_id":account_id,"call_id":call_id,"caller":caller,"did_number":did_number,"callee":"","record_status":record_status,"recorded_file":recorded_file}
response = requests.request("POST", str(voicemail_recording_url),data=payload,json=call_data)

