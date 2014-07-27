from django.db import models
import pytz
from datetime import datetime

class Tweets(models.Model):
    class Meta:
        db_table = 'tweets'
    id = models.AutoField(primary_key=True)
    text = models.TextField(db_index=True)
    timestamp = models.DateTimeField(db_index=True)

    def save(self, *args, **kwargs):
        if self.timestamp is None:
            self.timestamp = datetime.now(pytz.utc)
        return super(Tweets, self).save(*args, **kwargs)
