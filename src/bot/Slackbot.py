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
        url = "https://slack.com/api/conversations.history"
        token = "xoxb-2920457641283-3055852838307-VZY2Cejjr4htrbNybtwcsnCc"
        header = {
            "Authorization": "Bearer {}".format(token)
        }
        payload = {
            "channel": "C030LTJ6QAX"
        }
        message = requests.get(url, headers=header, params=payload)
        return "message"

    def send_message_to_slander_api(self,message):
        url = 'http://3.143.237.69/kusorep/score/'
        message = message
        param = {'msg': message}
        res = requests.get(url, params=param)
        slander = res.json()["body"]["kusoripu_score"]
        return slander

    def send_slander_message_to_slack(self, message):
        url = "https://slack.com/api/chat.postMessage"
        headers = {"Authorization": "Bearer " + self.TOKEN}
        data = {
            'channel': self.CHANNEL,
            'text': 'テストです。'
        }
        for i in range(5):
            r = requests.post(url, headers=headers, data=data)
            if r.json()["ok"]:
                return True

        return False
