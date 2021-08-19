from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from.models import post,category  #从models里面导入两个表

admin.site.register(post)#在admin里面添加我们创建好的POST表
admin.site.register(category)#在admin里面添加我们创建好的分类表
