#123
from flask import Flask, request, abort
from linebot import SignatureValidator
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
# parser = linebot.WebhookParser('YOUR_CHANNEL_SECRET')
def my(bodyy):
    import base64
    import hashlib
    import hmac

    channel_secret ='YOUR_CHANNEL_SECRET'
    body =bodyy # Request body string
    hash = hmac.new(channel_secret.encode('utf-8'),
                    body.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(hash)
    return signature
    # Compare X-Line-Signature request header and the signature
@app.route("/callback", methods=['POST'])
def callback():

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # signature = request.headers
    print("1:"+signature)
    print(type(signature))

    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    b=my(bodyy=body)
    print(b)
    print(type(b))
    # events = parser.parse(body, signature)
    # print(events)
    json_line = request.get_json()
    tok=json_line['events'][0]['replyToken']
    textt=json_line['events'][0]['message']['text']
    # print(json_line['events'][0]['replyToken'])
    # print(json_line['events'][0]['message']['text'])
    # SignatureValidator.validate(self=handler,body=body,signature=signature)
    #
    # line_bot_api.reply_message(
    #   tok,
    #  TextSendMessage(text=textt))


    try:
        handler.handle(body=body, signature=signature)
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