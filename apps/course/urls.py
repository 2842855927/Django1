from django.urls import path,re_path
from . import views
urlpatterns = [
    path('base/',views.base),
    path('course/',views.course),
    path('doc/',views.doc),
    path('ind/',views.ind),
    path('news_detail/',views.news_detail),
    path('search/',views.search),
]