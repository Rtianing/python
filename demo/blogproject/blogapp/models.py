

# Create your models here.


from django.db import models

# Create your models here.
from django.contrib.auth.models import User  #在models里面导入user表
from six import python_2_unicode_compatible  #为了兼容python2.7的，导入一个python装饰器

@python_2_unicode_compatible
class category(models.Model): #分类表，继承models.Model
    name = models.CharField(max_length=100) #名字规定一个大小，不浪费存储空间

@python_2_unicode_compatible #写一个装饰器，用法就是写一个@符号
class post(models.Model):  #文章表post，继承models。model这个类
    title = models.CharField(max_length=100) #标题是字符串类型，规定一个最大字符
    body = models.TextField() #正文字符肯定很多，所以用文本类型数据TextField
    create_time = models.DateTimeField() #创建时间，时间数据类型为DateTimeField
    modified_time = models.DateTimeField() #修改文章时间，多个单词用下划线隔开，是一种命名规范
    category = models.ForeignKey(category,on_delete=models.CASCADE) #分类表，外键关联（models.ForeignKey）关联category表， Django2.0以上版本一定要加上on_delete，意思是：当删除文章所属的分类时，这篇文章也会被删除，级联删除
    author = models.ForeignKey(User,on_delete=models.CASCADE) #作者外键关联Django里面的user表
