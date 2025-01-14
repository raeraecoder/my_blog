from django.urls import path
from .views import PostList
from rest_framework.routers import DefaultRouter
from .views import PostList,PostListDetailfilter
app_name='blog_api'
router=DefaultRouter()
router.register('',PostList,basename='user')

urlpatterns=[
      path('search/', PostListDetailfilter.as_view(), name='postsearch'),
     *router.urls
]
