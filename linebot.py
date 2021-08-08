#!pip3 install line-bot-sdk

import json

file = open('info.json','r')
info = json.load(file)
#print(info)
#print(info['CHANNEL_ACCESS_TOKEN'])

from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)



def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text="Jbot作成中です！！\n テストしています。")
    line_bot_api.push_message(USER_ID, messages=messages)

if __name__ == "__main__":
    main()

#github action
