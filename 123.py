from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler,WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')
parser = linebot.WebhookParser('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    events = parser.parse(body, signature)
    print(events)
    json_line = request.get_json()
    tok=json_line['events'][0]['replyToken']
    textt=json_line['events'][0]['message']['text']
    print(json_line['events'][0]['replyToken'])
    print(json_line['events'][0]['message']['text'])
    #line_bot_api.reply_message(
     #   tok,
      #  TextSendMessage(text=textt))
    # handle webhook body
    try:
        handler.handle(body, signature)
        print('get handle')
    except InvalidSignatureError:
        print('not get handle')
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print('hello!2')
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()