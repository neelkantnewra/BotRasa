# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_human_handoff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I am a Neelkant. what do you want from me.")

        return []

# import os
# from slack import WebClient
# from slack.errors import SlackApiError
 
# client_slack = WebClient(token=os.environ["xapp-1-A022S38V41Y-2101312718932-afe7bf4247c509c71c4620881ee4d62ec3460893c4f6bd4024f449c8256c31c8"], run_async=True)
# SLACK_SUPPORT_CHANNEL = os.environ["chatbot"]
 
 
# class ActionHumanHandoff(Action):
#    def name(self):
#        return "action_human_handoff"
 
#    async def run(
#        self, dispatcher, tracker, domain, reason: Text = None,
#    ):
#        events = []
#        text = f"Help needed for user {tracker.sender_id}"
#        try:
#            response = await client_slack.chat_postMessage(
#                channel=SLACK_SUPPORT_CHANNEL, text=text
#            )
#            if response.get("ok"):
#                dispatcher.utter_message(template="utter_handover_to_support")
#                events.append()
#        except SlackApiError as e:
#            dispatcher.utter_message(
#                template="utter_technical_issue", extra_message=e.response["error"],
#            )
#        return events

