import twython
from twython import TwythonStreamer

OAUTH_TOKEN = "YOUR_ACCESS_TOKEN"
OAUTH_TOKEN_SECRET = "YOUR_TOKEN_SECRET"
APP_KEY = "YOUR_CONSUMER_KEY"
APP_SECRET = "YOUR_CONSUMER_SECRET"

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()

if __name__ == "__main__":
    stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=['python', 'javascript', 'ruby'])