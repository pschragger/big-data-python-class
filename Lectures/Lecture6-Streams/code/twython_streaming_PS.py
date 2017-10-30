import twython
from twython import TwythonStreamer

OAUTH_TOKEN = "492743206-D8quqZUqOP5JjpXa1OCKg3h3kxFg9SLDOtnIw5J1"
OAUTH_TOKEN_SECRET = "NjeGEB0P9sSQLwf4nONSn3aKAiRVab6HOCBQNJDOC3qWC"
APP_KEY = "0ZcQT2K6iOyw4c343eBDH3e3r"
APP_SECRET = "XMup6GGtdM3BgSLPkZvDBQzwMRC0lZHZDFBk6sfgI3oUrAzhVA"

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