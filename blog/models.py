from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home', args=(str(self.id)))

CHOICE_LIST = (
    ('News', 'News'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Celebrity Gist', 'Celebrity Gist'), ('Recipe', 'Recipe'), ('Lifestyle', 'Lifestyle'), ('Featured', 'Featured'), ('Random', 'Random'),
    )

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="blog_posts")
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=200, choices=CHOICE_LIST, default='Test')
    likes = models.ManyToManyField(get_user_model(), related_name='blog_likes')
    images = models.ImageField(null=True, blank=True, upload_to="images/")
    # Count the number of likes
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home', args=(str(self.id)))

    def get_absolute_url(self):
        return reverse('post_detail', args={self.pk})

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    bio = models.TextField(default="This is author's bio")
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    twitter_url = models.CharField(max_length=250)
    facebook_url = models.CharField(max_length=250)
    instagram_url = models.CharField(max_length=250)
    linkedin_url = models.CharField(max_length=250)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)