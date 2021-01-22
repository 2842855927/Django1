from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
import datetime
# Create your views here.


def index(request):
    return HttpResponse('这是一个主页面,hi,django')


def test1(request,yy):
    #查看yy是什么类型的
    print(yy,type(yy))
    return HttpResponse('这是一个次级页面hi,my%s'%yy)


def test2(request,xx):
    return HttpResponse('hello! %s'%xx)
# redirect是重定向,reverse是将url的name解析成url本身的函数


def article(request,**kwargs):
    print(kwargs.get("test"))
    if kwargs.get("test")=='true':
        return redirect(reverse('index'))
    return HttpResponse("我就是个测试重定向")


def page(request):
    name1='斗笠'
    age=18
    book_name='hi,django'
    def hello():
        return 'hello.django'
    class name:
        def dj(self,sa):
            self.sa=sa
            return '%s name django'%self.sa
        def index(self):
            return 3.131415926
    # cl=name.sa("my")
    ls=[1,2,3,4,5,6]
    dc={"xxx":"pig","kw":"dog"}
    context={
        'name':name1,
        'age':age,
        'book_name':book_name,
        'he':hello,
        # 'cl':cl,
        'iy':name.index,
        'ls':ls,
        'dc':dc,

    }
    return render(request,'page.html',context=context)

def index_1(request):
    test='hi xiaoming'
    lt=[1,2,3,4,5]
    context={
        'test':test,
        'xx':'',
        'num1':1,
        'num2':2,
        'lt':lt,
        'now': datetime.datetime.now,
        'html':'<a>my is dgingo,wo xiaohong',
        'float':3.1415926
    }
    return render(request,'index_1.html',context=context)

def index_2(request,xx):
    context={
        'name':xx
    }
    return render(request,'index_2.html',context=context)
def index_3(request):
    context={
        "list1":[1,2,3,4,5,]
    }
    return render(request,'index_3.html',context=context)
def conut1(request):
    context={
        'str1': 'abcdefcaaa',
        'str2': 'abcdefghgklmnopqrst',
        'str3': 'ABCDEFGH'
    }
    return render(request,'Page/count1.html',context=context)

def result(request):
    # show_results最终呈现效果 自定义标签
    return render(request,'Page/count1.html')