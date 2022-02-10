import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'prod.env')
load_dotenv(dotenv_path)


class Slackbot():
    TOKEN = os.getenv("TOKEN")
    CHANNEL = os.getenv("CHANNEL")

    # Get mssage from Slack
    def get_message(self):
        url = "https://slack.com/api/conversations.history"
        token = "aaaaaa"
        header = {
            "Authorization": "Bearer {}".format(token)
        }
        payload = {
            "channel": "AAAAAAAA"
            # "channel": self.CHANNEL
        }
        message = requests.get(url, headers=header, params=payload)
        return "message"

    # Send message and get slander level score from slander level api
    def send_message_to_slander_api(self, message):
        url = 'http://3.143.237.69/kusorep/score/'
        message = message
        param = {'msg': message}
        res = requests.get(url, params=param)
        slander = res.json()["body"]["kusoripu_score"]
        return slander

    # Get measurement result from slander level api and check whether it is a slander
    def get_measurement_result(self):

        # get slander level from slander level api
        message = self.get_message()
        measurement_result_from_slander_api = self.send_message_to_slander_api(message)
        measurement_result = measurement_result_from_slander_api[0]
        # print(measurement_result)

        # Check wether the message is a slander (> 0.6 is a slander)
        if measurement_result > 0.6:
            print("This is a Slander")
            return "This is a Slander"
        else:
            print(None)
            return None
        
        # # Send warning massage to Slack by using slack-bot
        # warning_message = "This is a Slander"
        # payload = '{"text":"%s"}' % warning_message
        # response = requests.post('https://hooks.slack.com/services/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', data=payload)
        # print(response.text)

    # Send slander message to Slack by using slack-bot
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
