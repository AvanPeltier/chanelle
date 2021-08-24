from flask import Flask
from slack_sdk import WebClient

app = Flask(__name__)
token = "xoxb-2398498782434-2383786040871-fw14DgYqmkUNBVM5deA8awXN"

slack_events_adapter = SlackEventAdapter()
slack_web_client = WebClient(token=token)

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
