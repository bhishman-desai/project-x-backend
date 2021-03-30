import pyrebase
from flask import *

from main import *

config = {
    "apiKey": "AIzaSyBS_7musN81z34BVJ6YEOXVPBkEuRTuvfE",
    "authDomain": "test-138bb.firebaseapp.com",
    "projectId": "test-138bb",
    "storageBucket": "test-138bb.appspot.com",
    "messagingSenderId": "946643021392",
    "appId": "1:946643021392:web:555f9aa290a91d52446b55",
    "measurementId": "G-ME6ES9RYG0",
    "databaseURL": "https://console.firebase.google.com/project/test-138bb/storage/test-138bb.appspot.com/files"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def basic():
    return "<h1>Welcome! This is homepage</h1>"


@application.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        return redirect(url_for('basic'))
    if True:
        link = storage.child('videos/new.mp4').get_url(None)
        return vid_proc(vid_convert(link))


if __name__ == '__main__':
    application.run(debug=True)
