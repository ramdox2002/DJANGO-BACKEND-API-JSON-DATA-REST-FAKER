from django.db import models

class GenerateDataAnalitycs(models.Model):
    views = models.IntegerField()
    json_generated = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)