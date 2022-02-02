import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'prod.env')
load_dotenv(dotenv_path)


class Slackbot():
    TOKEN = os.getenv("TOKEN")
    CHANNEL = os.getenv("CHANNEL")

    def get_message():
        # please complete
        return "message"


    def send_message_to_slander_api():

        return "slander"

    def send_slander_message_to_slack(self, message):
        url = "https://slack.com/api/chat.postMessage"
        headers = {"Authorization": "Bearer "+ self.TOKEN}
        data  = {
            'channel': self.CHANNEL,
            'text': 'テストです。'
        }
        r = requests.post(url, headers=headers, data=data)
        print("return ", r.json())

        return "slander"
