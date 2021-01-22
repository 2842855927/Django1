from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def base(request):
    return render(request, 'base/base.html')
def course(request):
    return render(request,'course/course_detail.html')
def doc(request):
    return render(request,'doc/docDownload.html')
def ind(request):
    return render(request,'news/index.html')
def news_detail(request):
    return render(request,'news/news_detail.html')
def search(request):
    return render(request,'news/search.html')