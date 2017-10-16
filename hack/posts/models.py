from django.db import models
from django.core.urlresolvers import reverse #when someone posts, where to send 'em
from django.conf import settings

import misaka

from group.models import Group

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name = 'posts')
    created_at = models.DateTimeField(auto_now = True)#it'll autogenerate it
    message = models.TextField()
    message_html = models.TextField(editable = False)
    
