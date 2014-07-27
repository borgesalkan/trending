from threading import Thread
from mysite.settings import (DB_RLOCK, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
from twitter.models import Tweets
from TwitterAPI import TwitterAPI
from decorators import retry_if_fails
import dateutil.parser

db_lock = DB_RLOCK

@retry_if_fails
def twitter_thread(*args, **kwargs):
    """ Thread process to add twitter text to db. """
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token_key = ACCESS_TOKEN_KEY
    access_token_secret = ACCESS_TOKEN_SECRET

    # Get api object to Twitter using the OAuth
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    t = api.request('statuses/sample')

    for item in t.get_iterator():
        text = item.get('text', '')
        if not text:
            continue
        dt_str = item.get('created_at')
        dt = dateutil.parser.parse(dt_str) if dt_str else None
        t = Tweets(text=text, timestamp=dt)
        db_lock.acquire()
        t.save()
        db_lock.release()
    return False

# Fork the thread
print "Starting thread to fetch statuses/sample from twitter.."
th = Thread(target=twitter_thread)
th.start()
print "Thread running..."
