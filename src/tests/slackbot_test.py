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

