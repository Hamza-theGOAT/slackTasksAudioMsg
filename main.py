from slack_sdk import WebClient
import os
from dotenv import load_dotenv


def getCredz():
    load_dotenv()
    userToken = os.getenv('userToken')
    botToken = os.getenv('botToken')
    channelID = os.getenv('channelID')

    return userToken, botToken, channelID


def postAudio(userToken, channelID):
    pass


def main():
    userToken, botToken, channelID = getCredz()
    postAudio(userToken, channelID)


if __name__ == '__main__':
    main()
