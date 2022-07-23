import flask
import json
hooks = json.load(open("hooks.json"))

app = flask.Flask(__name__)

@app.route("/")
def indexView():
    return "hello world"

@app.route("/device/<device>")
def deviceView(device):
    if device in hooks.keys():
        return device
    return "404 device not found"

def main():
    app.run()

if __name__ == "__main__":
    main()