from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length = 1000, default='')
    status = models.BooleanField(default=False)
    
    def statusCheck(self):
        return self.status