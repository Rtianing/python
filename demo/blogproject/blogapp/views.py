from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from.models import post
def index(request):
   # return HttpResponse("欢迎你来到我的博客！")
   #return render(request,'blogapp/index.html',context={'title':'博客'})#内容

   post_list = post.objects.all()  # 数据库里面取数据
   return render(request, 'blogapp/index.html', context={'title': '博客', 'post_list': 'post_list'})  # 渲染数据

