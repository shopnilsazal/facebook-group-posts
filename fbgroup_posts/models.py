from django.db import models

# Create your models here.


class Post(models.Model):
    post_id = models.CharField('ID', max_length=80)
    created_time = models.DateTimeField('Created Time')
    from_name = models.CharField('Name', max_length=80)
    permalink = models.URLField('Post URL', max_length=255)
    message = models.TextField()
    likes = models.IntegerField()
    comments = models.IntegerField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-likes', 'from_name']

    def __str__(self):
        return self.from_name

