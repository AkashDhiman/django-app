from django.db import models

class Post(models.Model):
    postTypeId = models.IntegerField()
    acceptedAnswerId = models.IntegerField(null=True)
    parentId = models.IntegerField(null=True)
    ownerUserId = models.IntegerField(null=True)
    score = models.IntegerField()
    viewCount = models.IntegerField(null=True)
    lastEditorUserId = models.IntegerField(null=True)
    answerCount = models.IntegerField(null=True)
    commentCount = models.IntegerField(default=0)
    favoriteCount = models.IntegerField(null=True)
    body = models.TextField()
    ownerDisplayName = models.CharField(max_length=50, null=True)
    title = models.CharField(null=True, max_length=250)
    tags = models.TextField(null=True)
    creationDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    closedDate = models.DateTimeField(
        null=True, auto_now=False, auto_now_add=False)
    lastEditDate = models.DateTimeField(
        null=True, auto_now=False, auto_now_add=False)
    lastActivityDate = models.DateTimeField(auto_now=False, auto_now_add=False)
