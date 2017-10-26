from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    post_topic = models.ForeignKey('Topic', on_delete = models.CASCADE)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Topic(models.Model):
    topic_title = models.CharField(max_length = 40, primary_key = True, default='Miscellaneous')
    number_followers = models.IntegerField(default=0)

    def __str__(self):
        return self.topic_title

class Subscribe(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    topic_title = models.ForeignKey('Topic', on_delete = models.CASCADE)

    class Meta:
    	unique_together = ('username', 'topic_title')
        
