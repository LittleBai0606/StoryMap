from django.shortcuts import render
from django.views.generic import View
from .models import Story, Gallery, Comment
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from utils.email_send import send_register_email
from django.contrib.auth.hashers import make_password
from django.contrib import auth
import os, base64, datetime, json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


class IndexView(View):
    """
    首页
    """

    def get(self, request):
        story_list = Story.objects.all()
        return render(request, 'index.html', context={'story_list': story_list})

    def post(self, request):
        return render(request, 'index.html')


class GalleryView(View):
    """
    照片墙
    """

    def get(self, request):
        gallery_list = Gallery.objects.all()
        return render(request, 'gallery.html', context={'gallery_list': gallery_list})

    def post(self, request):
        return render(request, 'index.html')


class StoryShareView(View):
    """
    故事分享
    """

    def get(self, request):
        return render(request, 'story_share.html')

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            story = Story()
            title = request.POST.get('title' , '')
            content = request.POST.get('content', '')
            longitude = float(request.POST.get('y', '0'))
            latitude = float(request.POST.get('x', '0'))
            story.title = title
            story.content = content
            story.longitude = longitude
            story.latitude = latitude
            story.user_belong = user
            story.save()
            return HttpResponse('{"status": "success", "msg": "分享成功"}', content_type='application/json')
        return HttpResponse('{"status": "fail", "msg": "尚未登录"}', content_type='application/json')


class StoryListView(View):
    """
    故事列表
    """

    def get(self, request):
        story_list = Story.objects.all()
        return render(request, 'story_list.html', context={'story_list': story_list})

    def post(self, request):
        return render(request, 'story_post.html')


class StoryDetailView(View):

    def get(self, request, story_id):
        story = Story.objects.get(id = story_id)
        story.click_num += 1
        story.save()
        hot_list = Story.objects.all().order_by('-click_num')[0:2]
        comment_list = Comment.objects.filter(story_belong = story)
        return render(request, 'story_detail.html', context={'story': story,
                                                             'hot_list': hot_list,
                                                             'comment_list': comment_list})

    def post(self, request, story_id):
        user = request.user
        if user.is_authenticated:
            story = Story.objects.get(id=story_id)
            if story:
                comment = Comment()
                comment.content = request.POST.get('message', '')
                comment.user_belong = request.user
                comment.story_belong = story
                comment.save()
                return HttpResponse('{"status": "success", "msg": "评论成功"}', content_type='application/json')

            else:
                return HttpResponse('{"status": "fail", "msg": "未找到所属故事"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "尚未登录"}', content_type='application/json')

class WangEditor_uploadView(View):
    """
    富文本编辑器图片上传
    """
    def post(self,request):
        gallery = Gallery()
        user = request.user
        user_name = str(user)
        files = request.FILES.get('images')  # 得到文件对象
        file_dir = settings.STATICFILES_DIRS[0] + '/story_image/'
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_path = file_dir + '%s_' %(user_name) + files.name
        open(file_path, 'wb+').write(files.read())  # 上传文件
        upload_info = {"errno":0, "data":[settings.STATIC_URL + '/story_image/' + '%s_' %(user_name) + files.name]}
        upload_info = json.dumps(upload_info)   #wangeditor返回值json格式比较特殊，需要按照上面配置
        gallery.photo_name = '%s_' %(user_name) + files.name
        gallery.photo_url = 'story_image/' + '%s_' %(user_name) + files.name
        gallery.user_belong = user
        gallery.save()
        return HttpResponse(upload_info, content_type="application/json")



