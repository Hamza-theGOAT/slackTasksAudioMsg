from slack_sdk import WebClient
import os
from dotenv import load_dotenv


def getCredz():
    load_dotenv()
    userToken = os.getenv('userToken')
    botToken = os.getenv('botToken')

    client = WebClient(token=botToken)
    channelID = os.getenv('channelID')
    audioPath = os.getenv('audioPath')

    return client, channelID, audioPath


def postAudio(userToken, channelID, audioPath):
    pass


def main():
    client, channelID, audioPath = getCredz()
    postAudio(client, channelID, audioPath)


if __name__ == '__main__':
    main()
