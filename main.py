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


def postAudio(client, channelID, audioPath):
    response = client.files_upload_v2(
        channel=channelID,
        file=audioPath,
        title="Temp Audio.mp3",
        initial_comment="Test run for Temp Audio Message..."
    )

    if not response['ok']:
        print("Failed to send Audio")
        print(f"{response.status_code}: {response['error']}")
    else:
        print("Audio Message sent successfully!!!")


def main():
    client, channelID, audioPath = getCredz()
    postAudio(client, channelID, audioPath)


if __name__ == '__main__':
    main()
