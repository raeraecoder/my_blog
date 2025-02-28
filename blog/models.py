from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
# Create your models here.
from django.utils.translation import gettext_lazy as _
# for image
def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)
#class for category
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) :
        return self.name
#class for Post
class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
          
    options=(
        ('draft','Draft'),
        ('published','Published')
    )
    category=models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title=models.CharField(max_length=250)
    img = models.ImageField(
        _("Image"), upload_to=upload_to, default='posts/default.jpg')
    excerpt=models.TextField(null=True)
    content=models.TextField()
    img=models.ImageField(default='img1.png', blank=True)
    slug=models.SlugField(max_length=250,unique_for_date='published')
    published=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='blog_posts')
    status=models.CharField(max_length=10,choices=options,default='published')
    objects=models.Manager()#default manager
    postobjects=PostObjects()#custom manager

    class Meta:
         ordering = ('-published',)
    
    def __str__(self) :
        return self.title



