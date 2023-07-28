from flask import Flask, render_template
from flask_socketio import send, SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def manage_msgs(msg):
    send(msg, broadcast=True)


@app.route("/")
def homrpage():
    return render_template("homepage.html")


if __name__ == "__main__":
    socketio.run(app, host="localhost")
