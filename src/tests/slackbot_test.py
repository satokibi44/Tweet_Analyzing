from bot.Slackbot import Slackbot


def test_success_send_message_to_slack():
    bot = Slackbot()
    bot.CHANNEL = "analysis_test"

    is_success = bot.send_slander_message_to_slack("test")
    assert is_success == True

def test_fail_send_message_to_slack():
    bot = Slackbot()
    bot.TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    bot.CHANNEL = "analysis_test"

    is_success = bot.send_slander_message_to_slack("test")
    assert is_success == False

def test_send_message_to_slander_api():
    bot = Slackbot()
    is_success = bot.send_message_to_slander_api("お前馬鹿かよ")
    assert is_success == [0.9252830743789673]

def test_get_measurement_result():
    bot = Slackbot()
    measurement_result_from_slander_api = [0.9252830743789673]
    is_slander = bot.get_measurement_result(measurement_result_from_slander_api)
    assert is_slander == "This is a Slander"