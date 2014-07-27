from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import urlresolvers
from django.db.models import Count
from twitter.models import Tweets
from datetime import datetime, timedelta
import pytz
from mysite.settings import DB_RLOCK
from named_tuples import TweetTuple

MAX_MINUTES = 180   # 3 Hrs maximum

db_lock = DB_RLOCK   # Lock to gain db access

def get_retweets(minutes):
    """ Returns tweets in rolling window of time in last "minutes". """
    current_time = datetime.now(pytz.utc)
    start_time = current_time - timedelta(minutes=minutes)
    db_lock.acquire()
    retweets = Tweets.objects.filter(timestamp__range=(start_time, current_time)).values('text').annotate(count=Count('text')).order_by('-count', 'text')[:10]
    retweets = [TweetTuple(t['text'], t['count']) for t in retweets]
    Tweets.objects.filter(timestamp__lt=start_time).delete()
    db_lock.release()
    return retweets
        
def get_sample_tweets(request, *args, **kwargs):
    """ Fetches tweets in rolling window of time and renders an HTML page. """
    global MAX_MINUTES

    minutes = int(kwargs.get('minutes', 0))   # Fetch minutes if present in the request object
    if minutes > MAX_MINUTES:
        minutes = MAX_MINUTES
    retweets = get_retweets(minutes)    # Get rolling window tweets
    context = {'retweets': retweets}
    context['minutes'] = minutes
    return render(request, 'index.html', context)

def post_minutes(request, *args, **kwargs):
    """ View function for Input form to get user input for minutes. """
    if request.method == 'GET':
        return render(request, 'input.html')
    elif request.method == 'POST':
        minutes = int(request.POST.get('minutes', 0))
        if minutes > MAX_MINUTES:
            minutes = MAX_MINUTES
        return HttpResponseRedirect('../sample_tweets/{}/'.format(minutes))

