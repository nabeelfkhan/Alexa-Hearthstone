from flask import Flask
from flask_ask import Ask, statement, convert_errors
import logging
import pyautogui


app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('HunterIntent', mapping={'action': 'action'})
def hunter(action):

	if action == "hello":
		pyautogui.hotkey('F3')
	
	if action == "the opponent":
		pyautogui.hotkey('shift', '5')
		
	if action == "for the face":
		pyautogui.hotkey('shift', '4')
	
		
	return statement('For the horde')
	
if __name__ == '__main__':

	port = 5000 #the custom port you want

	app.run(host='0.0.0.0', port=port)
	
	