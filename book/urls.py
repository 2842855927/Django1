from django.conf import urls
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('index/', views.index, name='index1'),
    #给个int值,使用尖括号(<>)从url中捕获值
    path('test1/<int:yy>/',views.test1,name='test1'),
    #re_path和re正则的用法一样
    re_path('^test2/(?P<xx>[a-z]+)/',views.test2,name='test2'),
    path('article/<kwargs>/',views.article,name='article'),
    path('page/',views.page,name='page'),
    path('index_1/',views.index_1,name='index_1'),
    path('index_2/<xx>',views.index_2,name='index_2'),
    path('index_3/',views.index_3,name='index_3'),
    path('conut1/',views.conut1,name='conut1'),
    # 自定义标签
    path('result/',views.result,name='result')

]
