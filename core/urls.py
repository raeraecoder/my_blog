"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
# from rest_framework.documentation import include_docs_urls
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#  for image.url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    path('api/',include('blog_api.urls',namespace='blog_api')),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('docs/', include_docs_urls(title='BlogAPI')),
    path('schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0"
    ), name='openapi-schema'),
  
    # for the registeration path
    path('api/user/',include('users.urls',namespace='users'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
