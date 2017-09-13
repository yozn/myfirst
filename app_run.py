from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(S3j1ofb/xSO5XBQy75+xooa4WXdES3td/4yBkjFLp0Yjt6USZbyI+zeiWzoNTfaC3JcTUHGZar6LI2zgSRF3NPpkOnEjxzJk/3Sp30wCsYq29uZfjgWa1WAw7uJCoaKQ7d7Ho+Vgm28S4xz06R1AWQdB04t89/1O/w1cDnyilFU=)
handler = WebhookHandler(ba8f47f94af476f1a1220939e9ca5429)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()