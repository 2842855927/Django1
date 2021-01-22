from django.contrib import admin
from .models import Dapartment,Student,Usel,UserModels
# Register your models here.
admin.site.site_title='MyDjano'
admin.site.site_header='星煞站台管理'
#将数据库添加到后台管理
admin.site.register(Dapartment)
admin.site.register(Student)
admin.site.register(Usel)
admin.site.register(UserModels)
