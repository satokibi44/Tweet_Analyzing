import sys
import requests
import getopt


# Send measurement result to #analysis channal by using slack-bot
def get_measurement_result():
    # get slander level from slander level api
    message = "お前馬鹿かよ" 
    measurement_result_from_slander_api = requests.get('http://3.143.237.69/kusorep/score/?msg=%s' % message)
    measurement_result_json = measurement_result_from_slander_api.json()
    measurement_result = (measurement_result_json['body']['kusoripu_score'])[0]
    print(measurement_result)

    # Check wether the message is a slander (> 0.6 is a slander)
    if measurement_result > 0.6:
        
        print("This is a Slander")
        return "This is a Slander"
    else:
        print(None)
        return None

    # Send final_measurement_result to Slack by using slack-bot
    # payload = '{"text":"%s"}' % measurement_result
    # response = requests.post('https://hooks.slack.com/services/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', data=payload)
    # print(response.text)


get_measurement_result()