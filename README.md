# chatbot-rasa-restaurants
A chatbot implemented in rasa framework which lists various restaurants and its cuisines.
![chatbot_sc](https://user-images.githubusercontent.com/17952054/119011370-a1838380-b9b2-11eb-902d-33563414bea9.png)

To run use the following commands in two two different windosws
- $ rasa run actions #to run the actions.py file to monitor the actions
- $ rasa shell --endpoints endpoints.yml #it will activate the the rasa shell for conversations

If any changes made
- $ rasa train #retrains the models with recent changes

To validate the YAML files
- $ rasa data validate


