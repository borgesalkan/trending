Rolling Window Tweets Application
==================================

The _trending_ repo contains all of the code to run the django server and also the web pages, to access the tweets.
User can provide a rolling window of time in minutes. The web page is designed to refresh every one minute to display
live sample tweets from Twitter in that rolling window. Tweets that fall before the rolling window time are currently
truncated, to save on disk space. So this design may not be the best one multiple users simultaneously.

Table of Contents
-----------------

[Getting Started](#getting-started)

Getting Started
---------------

### Prerequisites

- [virtualenv](http://www.virtualenv.org/en/latest/index.html)
It can be installed via easy_install, pip, or manually.

    pip install virtualenv

Other flavors of Linux install using the package manager of your choice.

### Initial Setup

- Clone the repository using the following command:
    git clone git@github.com:borgesalkan/trending.git
- Create a virtualenv drive and activate the source
    virtualenv --no-site-packages env.d
    source env.d/bin/activate
- Install the requirements
    pip install -r requirements.txt
- Run the syncdb and schemamigrations
    python manage.py syncdb
    python manage.py migrate

All set for next step.
    
### Running the Application

Once you have your installation ready, you can start the server.
Issuing the command

    python manage.py runserver 0.0.0.0:8000

will bring up a local development server on port 8000.

It also starts a background thread process to fetch twitter sample tweets, and stores to a SQLite3 DB.

Now just open your favorite browser and go to:
    http://localhost:8000/input/

Input a number indicating the minutes you want for a rolling window.
Sit back and keep track of trending Twitter tweets sample, every minute.



