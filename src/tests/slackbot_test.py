from bot.slackbot import Slackbot


def test_success_send_message_to_slack():
    bot = Slackbot()
    bot.CHANNEL = "analysis_test"

    is_success = bot.send_slander_message_to_slack("test", "This is Slander!")
    assert is_success == True

def test_fail_send_message_to_slack():
    bot = Slackbot()
    bot.TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    bot.CHANNEL = "analysis_test"

    is_success = bot.send_slander_message_to_slack("test", "This is Slander")
    assert is_success == False

def test_send_message_to_slander_api():
    bot = Slackbot()
    is_success = bot.send_message_to_slander_api("お前馬鹿かよ")
    assert is_success == [0.9252830743789673]

