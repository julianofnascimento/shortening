from django.db import models

class Urls(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=150, db_index=True)
    short_url_key = models.CharField(max_length=7, db_index=True)