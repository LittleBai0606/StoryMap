"""StoryMap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
import main_platform.views as mp_view
import users.views as u_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^login/$', u_view.UserLoginView.as_view(), name='login'),
    url(r'^logout/$', u_view.UserLogoutView.as_view(), name='logout'),
    url(r'^register/$', u_view.RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', u_view.ActiveUserView.as_view(), name="user_active"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', mp_view.IndexView.as_view(), name='index'),
    url(r'^share/$', mp_view.StoryShareView.as_view(), name='share'),
    url(r'^add_story/$', mp_view.StoryShareView.as_view(), name='add_story'),
    url(r'^story_list/$', mp_view.StoryListView.as_view(), name='story_list'),
    url(r'^story/(?P<story_id>\d+)', mp_view.StoryDetailView.as_view(), name='story_detail'),
    url(r'^gallery/$', mp_view.GalleryView.as_view(), name='gallery'),
    url(r'^story/upload/$', mp_view.WangEditor_uploadView.as_view(), name='upload_img'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
