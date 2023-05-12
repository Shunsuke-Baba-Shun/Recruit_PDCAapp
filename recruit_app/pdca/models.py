from django.db import models

Category = (('It', 'IT業界'), ('backend','バックエンド'), ('other', 'その他'))

# Create your models here.
class reflection(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    Category = models.CharField(
                max_length = 100,
                choices = Category
                )
    description = models.TextField()
    Plan = models.TextField()
    Do = models.TextField()
    Check = models.TextField()
    Action = models.TextField()
    def __str__(self):
        return self.title