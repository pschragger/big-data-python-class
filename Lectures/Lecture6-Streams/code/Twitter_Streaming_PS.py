#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "492743206-D8quqZUqOP5JjpXa1OCKg3h3kxFg9SLDOtnIw5J1"
access_token_secret = "NjeGEB0P9sSQLwf4nONSn3aKAiRVab6HOCBQNJDOC3qWC"
consumer_key = "yXmaXwpl5fmAeJNNFsVF0rtPJ"
consumer_secret = "yrndvISaXmlsds2GPlBIpH1wdoWlnTFjG4vG0YFuVQXWTkA90l"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])