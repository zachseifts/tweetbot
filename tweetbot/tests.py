
from urllib2 import HTTPError
from nose.tools import raises

from tweetbot import *

def test_create_twitterbot():
    bot = TwitterBot(username='foo', password='bar')
    assert bot.username == 'foo'
    assert bot.password == 'bar'
    assert bot.bitly_api == None
    assert bot.bitly_api_user == None

@raises(TweetLengthExceeded)
def tests_check_tweet_length():
    bot = TwitterBot(username='foo', password='bar')
    bot.check_tweet_length('a'*150)
    bot.check_tweet_length('a'*100)

@raises(BitlyAPIKeyNeeded, BitlyException)
def test_bitly_services():
    bot = TwitterBot(username='foo', password='bar')
    bot.shorten_url('http://www.example.com/foo/bar/some/thing/else')

@raises(HTTPError)
def test_post_tweet():
    bot = TwitterBot(username='foo', password='bar')
    bot.tweet = 'a'*100
    bot.post()

