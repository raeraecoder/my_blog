from rest_framework import serializers
from blog.models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Post
#         fields=('id','title','author','excerpt','content','status')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id', 'title','img','slug', 'author',
                  'excerpt', 'content', 'status')