import logging
from pyrogram import idle
from os import makedirs, path
from config import Config
from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the Flask app
@app.route('/')
def home():
    return jsonify({"message": "Flask server is running!"})

# Define more routes if needed
@app.route('/status')
def status():
    return jsonify({"status": "active"})

if __name__ == "__main__":
    logging.info(" >> Checking download location...")
    if not path.isdir(Config.DOWNLOAD_LOCATION):
        makedirs(Config.DOWNLOAD_LOCATION)

    logging.info(" >> Applying custom methods...")
    from .client import init_patch
    init_patch()

    logging.info(" >> Starting client...")
    from unzipper import unzip_client
    from unzipper.modules import *
    unzip_client.start()

    logging.info(" >> Checking Log Channel...")
    from .helpers_nexa.checks import check_log_channel
    check_log_channel()

    logging.info("Bot is active Now! Join @NexaBotsUpdates")

    # Run Flask in a separate thread
    from threading import Thread
    def run_flask():
        app.run(host='0.0.0.0', port=5000, debug=True)

    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Start the Pyrogram client
    idle()
