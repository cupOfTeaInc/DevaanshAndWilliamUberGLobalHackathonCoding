import flask
import json
import requests
import controller

hooks = json.load(open("hooks.json"))

app = flask.Flask(__name__)

@app.route("/")
def indexView():
    devices = []
    for device in hooks["devices"].keys():
        d = {"view":"/device/"+device, "name":device}
        devices.append(d)
    return flask.render_template("indexView.html", devices=devices)

@app.route("/about")
def aboutView():
    devices = []
    for device in hooks["devices"].keys():
        d = {"view":"/device/"+device, "name":device}
        devices.append(d)
    return flask.render_template("aboutView.html", devices=devices)

@app.route("/device/<device>")
def deviceView(device):
    if device in hooks["devices"].keys():
        d = {"name":device, "functions":list(hooks["devices"][device].keys())}
        return flask.render_template("deviceView.html", device=d)
    return "404 device not found"

@app.route("/device/<device>/<action>", methods=["POST"])
def actionView(device, action):
    try:
        requests.post(hooks["hook_base"]+hooks["devices"][device][action])
        return action

    except Exception as e:
        #print(e)
        return "Action Failed"

@app.route("/execute")
def execute():
    controller.run()
    print('clicked')

    return flask.redirect("/")


def main():
    app.run()

if __name__ == "__main__":
    main()