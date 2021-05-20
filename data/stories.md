## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## story 1 greet+search_provider+search_cuisine+goodbye
* greet
  - utter_greet
* search_provider{"location":"Solapur"}
  - action_search_provider
* search_cuisine{"cuisine_type":"cuisine"}
  - action_search_cuisine
* goodbye
  - utter_goodbye


## story 2 greet+search_provider+search_cuisine+goodbye
* greet
  - utter_greet
* search_provider{"location":"Baner"}
  - action_search_provider
* search_cuisine{"cuisine_type":"cuisine"}
  - action_search_cuisine	
* goodbye
  - utter_goodbye

## story 3 greet+search_provider+search_cuisine+goodbye
* greet
  - utter_greet
* search_provider{"location":"Maharshtra"}
  - action_search_provider
* search_cuisine{"cuisine_type":"cuisine"}
  - action_search_cuisine	
* goodbye
  - utter_goodbye

## story 5 greet+search_provider+search_cuisine+goodbye
* greet
  - utter_greet
* search_provider{"location":"Pune"}
  - action_search_provider
* search_cuisine{"cuisine_type":"cuisine"}
  - action_search_cuisine	
* goodbye
  - utter_goodbye

## story 6 greet+search_provider+search_cuisine+goodbye
* greet
  - utter_greet
* search_provider{"location":"Shiavajinagar"}
  - action_search_provider
* search_cuisine{"cuisine_type":"cuisine"}
  - action_search_cuisine	
* goodbye
  - utter_goodbye
	
## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
