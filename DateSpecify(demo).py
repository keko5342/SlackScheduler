import SlackModule
import json, requests, re

# Setup API Token
url = ["https://slack.com/api/channels.list", "https://slack.com/api/channels.history"]
goourl = "https://labs.goo.ne.jp/api/chrono"
token = "xoxp-494038745009-494540232547-494886917717-dbbbdd37b278a8407b1d9bee618b45f6"
gootoken = "cf7a57c089138137000856ea8b8637c250782aeeb5d434769b8b3128bb5a20e0"

# さて、ここではテキストから日時情報を抜き出す処理を行おう。
# まず、定量化から始めたほうが表現に差が生まれなくてよいと思う。
# というわけで、まずはひらがな、カタカナ、漢字表現、全角英数表現を半角英数表現に置き換えよう。
# 完成形(afterText)は、'2018-12-11 13:28:36.000600':飲み会。date:text
# これもしかしなくても自然言語処理やな、うんち

#12/20 試しにgooLabの時間情報正規化APIを利用してみたが、毎日、来週といった時間情報は取得できない模様。難しい
#自分で時間情報の正規化を行ったほうがよさそうだ
class DateChanger:
    def __init__(self, url, token, date, text):
        self.url = url
        self.token = token
        self.date = date
        self.beforeText = text
        self.tempText = []
        self.afterText = []

    def MMDDtoMonthDay(self):
        # step1. MM月DD日orMM/DDを抽出
        dateRegexp = '\d+月\d+日'

        # step2. 
        if re.match(dateRegexp, '12月12日'):
            print("OK")
        else:
            print("No")
        if re.match(dateRegexp, '1月12日'):
            print("OK")
        else:
            print("No")
        if re.match(dateRegexp, '１２月１２日'):
            print("OK")
        else:
            print("No")
    
    def sendRequest(self):
        request = {"app_id":self.token, "sentence":self.beforeText}
        json.dumps(request)
        print(request)

        return_post = requests.post(self.url, json=request)
        print(type(return_post))
        print(return_post.json())

    def sayDate(self):
        print("Date is : {}".format(self.date))

    def sayBeforeText(self):
        print("There are beforeText: {}".format(self.beforeText))
    
    def sayAfterText(self):
        print("There are afterText: {}".format(self.afterText))

def main():
    Channel_Data = SlackModule.ChannelData(url, token)
    Channel_Data.setChannel()
    Channel_Data.setAll()
    #Channel_Data.sayAll()

    Date_Changer = DateChanger(goourl, gootoken, Channel_Data.getDate(), Channel_Data.getText())
    #Date_Changer.sayDate()
    #Date_Changer.sayBeforeText()
    #Date_Changer.sendRequest()
    Date_Changer.MMDDtoMonthDay()
    #Date_Changer.sayAfterText()

if __name__ == '__main__':
    main()