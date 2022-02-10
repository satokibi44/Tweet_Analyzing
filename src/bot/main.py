from Slackbot import Slackbot

def main():
    bot = Slackbot()
    message = bot.get_message()
    result_from_slander_api = bot.send_message_to_slander_api(message)
    slander = bot.get_measurement_result(result_from_slander_api)
    bot.send_slander_message_to_slack(message, slander)

if __name__ == "__main__":
    main()