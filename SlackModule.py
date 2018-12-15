import requests
import json
from datetime import datetime

# Setup API Token
url = ["https://slack.com/api/channels.list", "https://slack.com/api/channels.history"]

class ChannelData:
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.channel = []
        self.text = []
        self.timestamp = []
        self.date = []

    def setChannel(self):
        # Get Parameters
        url = self.url
        token = self.token

        # Send requests to Slack API
        payload = {
            "token": token
            }
        response = requests.get(url[0], params=payload)

        # Fetch channel_id by json
        json_data = response.json()
        channel_id_lists = [json_data['channels'][i]['id'] for i in range(len(json_data['channels']))]
        self.channel = channel_id_lists
        #print("There are channel_ids: {}".format(channel_id_lists))
    
    def setAll(self):
        # Get Parameters
        url = self.url
        token = self.token
        channel = self.channel

        # Send requests channel history
        for i in range(len(channel)):
            payload = {
                "token": token, "channel": channel[i]
            }
            response = requests.get(url[1], params=payload)

            # Fetch channel_text by json
            def to_float(str):
                return float(str)
            json_data = response.json()
            #print(json_data)
            channel_text_lists = [json_data['messages'][i]['text'] for i in range(len(json_data['messages'])) if 'subtype' not in json_data['messages'][i]]
            channel_ts_lists = [float(json_data['messages'][i]['ts']) for i in range(len(json_data['messages'])) if 'subtype' not in json_data['messages'][i]]
            channel_date_lists = [str(datetime.fromtimestamp(float(json_data['messages'][i]['ts']))) for i in range(len(json_data['messages'])) if 'subtype' not in json_data['messages'][i]]
            self.text.append(channel_text_lists)
            self.timestamp.append(channel_ts_lists)
            self.date.append(channel_date_lists)
    
    def getText(self):
        return self.text
    
    def getDate(self):
        return self.date

    def sayAll(self):
        for i in range(len(self.channel)): print("There are channel_texts in {}: {}:".format(self.channel[i], self.text[i]))
        for i in range(len(self.channel)): print("There are channel_texts in {}: {}:".format(self.channel[i], self.timestamp[i]))
        for i in range(len(self.channel)): print("There are channel_texts in {}: {}:".format(self.channel[i], self.date[i]))

def main():
    with open('./API_OAuth_Token.txt') as f:
        token = f.read()

    Channel_Data = ChannelData(url, token)
    Channel_Data.setChannel()
    Channel_Data.setAll()
    Channel_Data.sayAll()

if __name__ == '__main__':
    main()