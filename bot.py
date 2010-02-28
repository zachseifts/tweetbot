#!/usr/bin/env python

import twitter
import urllib

__all__ = ['TweetLengthExceeded', 'TwitterBot', 'BitlyAPIKeyNeeded',
           'BitlyException']

class TweetLengthExceeded(Exception): pass
class BitlyAPIKeyNeeded(Exception): pass
class BitlyException(Exception): pass

class TwitterBot(object):
    ''' A twitter bot.

    >>> class MyBot(TwitterBot):
    ...
    ...     def __init__(self, username, password):
    ...         self.do_something()
    ...         super(MyBot, self).__init__(username=username,
    ...                                     password=password)
    ...
    ...     def do_something(self):
    ...         tweet = 'test tweet'
    ...         self.check_tweet_length(tweet)
    ...         self.tweet = tweet
    ...
    >>> mb = MyBot(username='username', password='password')
    >>> print mb.tweet
    test tweet

    '''
    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        self.bitly_api = kwargs.get('bitly_api', None)
        self.bitly_api_user = kwargs.get('bitly_api_user', None)
        self._authenticate()

    def _authenticate(self):
        self.api = twitter.Api(username=self.username,
                               password=self.password)

    def post(self, tweet):
        self.check_tweet_length(tweet)
        self.api.PostUpdate(tweet)

    def check_tweet_length(self, tweet):
        ''' Makes sure the tweet is less than 140 characters.
        '''
        if len(tweet) > 140:
            raise TweetLengthExceeded

    def shorten_url(self, long_url):
        ''' Shortens the url using bit.ly's service.

        adapted from:
            http://tux-log.blogspot.com/2009/05/url-shortening-with-pyhton-and-bitly.html
        '''
        if ( self.bitly_api and self.bitly_api_user ):
            try:
                lng_url = urllib.urlencode(dict(longUrl=long_url))
                login = urllib.urlencode(dict(login=self.bitly_api_user))
                api_key = urllib.urlencode(dict(apiKey=self.bitly_api))
                encodedurl="http://api.bit.ly/shorten?version=2.0.1&%s&%s&%s" % (lng_url, login, api_key)
                request = urllib.urlopen(encodedurl)
                responde = request.read()
                request.close()
                responde_dict = eval(responde)
                short_url = responde_dict["results"][long_url]["shortUrl"]
                return short_url
            except IOError, e:
                    raise BitlyException('%s' % (e,))
        else:
            raise BitlyAPIKeyNeeded


if __name__ == '__main__':
    import doctest
    doctest.testmod()


