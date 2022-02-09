import sys
import requests
import getopt


# Send measurement result to #analysis channal by using slack-bot
def get_measurement_result():
    # get slander level from slander level api
    ploads = "お前馬鹿かよ" 
    # ploads = "\"お前馬鹿かよ\""
    measurement_result_from_slander_api = requests.get('http://3.143.237.69/kusorep/score/?msg=%s' % ploads)
    measurement_result_json = measurement_result_from_slander_api.json()
    measurement_result = (measurement_result_json['body']['kusoripu_score'])[0]
    print(measurement_result)
    # print(type(measurement_result))
    # print(measurement_result > 1)

    # Send final_measurement_result to Slack by using slack-bot
    payload = '{"text":"%s"}' % measurement_result
    response = requests.post('https://hooks.slack.com/services/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', data=payload)
    print(response.text)


get_measurement_result()