import os
from flask import Flask
from slack_sdk import WebClient
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)


slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)
slack_web_client = WebClient(token=os.environ.get("SLACKBOT_TOKEN"))

MESSAGE_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": ""
    }
}

@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
