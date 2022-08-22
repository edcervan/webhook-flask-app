
from flask import Flask, make_response, request
import requests
import json

app = Flask(__name__)

#Temp store of webhooks, gets restarted everytime server restarts
recent_webhooks = []

#CAPI response variables
fbid = '103522469122428'
access_token = 'EAAGSn8RQLXkBAFA0I1nakmmxss6OsJFOTF4hdfFNrXZCtDntMJFQs0DMTzchO99xbc5SVpHKJi1UWUr0MhHOZBpvabLumUZCwa2cXnZBOeWRVcgMlLCyPK8XyFkAwRmHFJZBBPj2LMT8vf9LDJrwZC0O6GQZBOis9c0PGEZBSAQiPNZBDGfNMu6si2NZAdBEnuGkWfLAg2UF5Se1dv3k1FVSIP'

@app.route("/")
def home_view():
        return "<h1>HELLO WORLD</h1>"

@app.route("/get_webhook", methods=["GET"])
def webhooks():
    if request.method == "GET":
        resp = make_response(json.dumps(recent_webhooks), 200)
        return resp

@app.route("/webhook", methods=["GET", "POST", "PUT", "DELETE"])
def incoming_webhook():
    global recent_webhooks
    if request.method == "POST":
        data = request.get_json()
        recent_webhooks.append(data)
        #------------------------Send Response START-------------------------
        '''
        if 'messages' in data:
            url = 'https://graph.facebook.com/v14.0/{0}/messages?access_token={1}'.format(fbid, access_token)
            payload = json.dumps({
                        "messaging_product": "whatsapp",
                        "recipient_type": "individual",
                        "to": data['messages'][0]['from'],
                        "type": "image",
                        "image": {
                            "link": "https://i.imgur.com/XMmzRmi.png"
                        }
                    })
            headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
            r = requests.post(url, data=payload, headers=headers)
            print(r)
            print(r.content)
        '''
        #------------------------Send Response END-------------------------
        resp = make_response('Webhook received', 200)
        return resp
    if request.method == "GET":
        #Callback to link Webhook with CAPI setup
        recent_webhooks.append(request.args)
        challenge = request.args.get("hub.challenge")
        resp = make_response(challenge, 200)
        return resp
