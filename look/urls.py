from . import views
from django.urls import path
urlpatterns = [
    path('ss/',views.ss,name='ss'),
    path('indexxx/',views.indexxx,name='indexxx'),
    path('add1/',views.add1,name='add1'),
    path('add_book/',views.add_book,name='add_book'),
    path('get1/',views.get1,name='get1'),
    path('update1/',views.update1,name='update1'),
    path('del1/',views.del1,name='del1'),
    path('pa/',views.pa,name='pa'),
    #一对多数据库
    path('Dapartment_add/',views.Dapartment_add,name='Dapartment_add'),
    path('Student_add/',views.Student_add,name='Student_add'),
    path('age_gt/',views.age_gt,name='age_gt'),
    path('age_lte/',views.age_lte,name='age_lte'),
    path('ds/',views.ds,name='ds'),
    #aggregate查询
    path('test_info/',views.test_info),
    #F查询
    path('test_info1/',views.text_info1),
    #Q查询
    path('qname/',views.qname),
    path('aname/',views.aname),
    path('method1/',views.method1),
    #状态登录
    path('home/',views.home,name='ts_home'),
    path('login/',views.login_1,name='login'),
    path('logout/',views.logout_1,name='logout'),
    path('add_form/',views.add_form),
    path('set_ck/',views.set_ck),
    path('delete_ck/',views.delete_ck),
    path('get_ck/',views.get_ck),
    path('register/',views.register),
    path('upload/',views.upload),
]
