# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from pynput.keyboard import Key, Listener
from logging import Handler
from typing import Any, Text, Dict, List

from rasa_sdk import Action , Tracker
from rasa_sdk import events
from rasa_sdk.events import (
    ConversationPaused,
    ConversationResumed
)
from rasa_sdk.executor import CollectingDispatcher

from random import randint
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path
import socketio
from time import sleep # just used for timing the messages
#load environment variable

env_path = Path(".")/".env"
load_dotenv(dotenv_path = env_path)

# <=======================socket programming======================>

sio = socketio.Client()
sio.wait()

@sio.event
def connect():
    print('Connection established with server to send message data.')

def send_msg(msg):
    print("sending")
    sio.emit('message', msg)

@sio.event
def disconnect():
    print('Disconnected from websocket! Cannot send message data.')

# make a connection with server
sio.connect('http://localhost:3000')

# extract message from server
@sio.on('message')
def message_handler(msg):
    #<=========================================AREA TO RESOLVE =============================>
    # - can we extract msg outside the above function 
    # - To dipatch the message to user with-in user bot interface
#     dispatcher = CollectingDispatcher()
#     dispatcher.utter_message(text=msg["message"])
    #<======================================================================================>
    print(msg)

#<==========================================================================================>


class ActionHumanHandoff(Action):
    """
    human in the loop action
    """
    def name(self) -> Text:
        return "action_human_handoff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="Hello World!")
        # events.append(ConversationPaused())
        
        #<==============to send last message typed by user to the admin===============>
        msg = {
            "user": "User",
            "message": tracker.latest_message['text'] # tracker last message
        }

        sio.on('message', message_handler) 
        #<==============to run this send command in another custom action======================>
        # - Can we make a handoff policies such that it will keep on tracking and sending the last message
        # - whenever a user type any new message  this is the Actual challenge 
        # - currently it is able to send message only when human handoff is triggered
        # - I want it to send all message whenever a slot is true -----Working on it-----------
        send_msg(msg)
        #<=============================================================================>

        sio.on('message', message_handler)
        # for server to wait
        # sio.wait()      
         

        return []





