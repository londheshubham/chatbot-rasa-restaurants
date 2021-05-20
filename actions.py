from random import randrange
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import operator
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#1
class ActionSearchProvider(Action):

    def name(self) -> Text:
        return "action_search_provider"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = ""
        for e in tracker.latest_message['entities']:
            if e['entity'] == "location":
                if e['value'] == None:
                    location = "at the above location"
                else:
                    location = e['value']
        rst_avail = ["Lemon Tree", "Sudha", "Supraja", "Desi Chinese"]
        dispatcher.utter_message(text=f"The resturant at {location} is {rst_avail[randrange(len(rst_avail))]}")

        return []
#2
class ActionSearchCuisine(Action):
    def name(self) -> Text:
        return "action_search_cuisine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rs = ""
        lm = tracker.latest_message['text']
        print(lm)
        cus_type = ["North Indian", "Chinese","Continental", "South Indian", "Punjabi", "Italian"]
        rst_avail = ["Lemon Tree","Sudha","Supraja","Desi Chinese"]
        for k in rst_avail:
            #if k not in lm:
            if not operator.contains(lm, k):
                rs = "above location"
            else:
                rs = k
            print(rs)
        dispatcher.utter_message(text=f"The cuisine available at the {rs} is {cus_type[randrange(len(cus_type))]}")

        return []

#3
