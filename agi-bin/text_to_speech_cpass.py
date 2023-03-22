#!/usr/bin/env python3

import sys
import uuid
import os
import json
import time
import requests
import urllib.parse
from asterisk.agi import *
import azure.cognitiveservices.speech as speechsdk
import constant as ct

value1 = sys.argv[1]
say_data = urllib.parse.unquote(sys.argv[2])
voice = sys.argv[3]

def text_to_speech(data,filename):
    speech_config = speechsdk.SpeechConfig(subscription=ct.SUBSCRIPTION_KEY, region=ct.REGION)
    audio_config = speechsdk.audio.AudioOutputConfig(filename="/tmp/"+filename+".wav")
    speech_config.speech_synthesis_voice_name=str(voice)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result = speech_synthesizer.speak_text_async(data).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return filename
    else:
        filename='thank_you-8khz'
        return filename

temp_filename = text_to_speech(say_data,str(value1))

