from rest_framework import generics
from blog.models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.permissions import SAFE_METHODS,IsAdminUser,IsAuthenticated,BasePermission,DjangoModelPermissions,IsAuthenticatedOrReadOnly,AllowAny
#create class for custom permission
class PostUserWritePermission(BasePermission):
    message='Editing posts is restricted to the author only'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author ==request.user
class PostList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()



class PostListDetailfilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']
    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.

    