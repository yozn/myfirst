# encoding: utf-8
import json
import requests


def slack_send(text):

    # HTTP POST Request
    s_url = 'https://hooks.slack.com/services/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'

    dict_headers = {'Content-type': 'application/json'}

    dict_payload = {
        "text": text}
    json_payload = json.dumps(dict_payload)
    rtn = requests.post(s_url, data=json_payload, headers=dict_headers)
    return None
