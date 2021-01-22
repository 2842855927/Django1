import os

from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# 导出模型类
from .models import Usel,Dapartment,Student
# 数据库自增长
from django.db.models import F,Q,Avg,Max,Min,Count,Sum
from .forms import AddForm,RegisterFrom
from .models import UserModels
from tanzhong.settings import MEDIA_ROOT
#auth登录模块
from django.contrib.auth import login,logout,authenticate
#auth自带的模型类
from django.contrib.auth.models import User,Permission,Group
# Create your views here.
def ss(request):
    return render(request,'ss.html')
def indexxx(request):
    return render(request,'indexxx.html')


# 数据库操作
# 添加
def add1(request):
    book=Usel.objects.update_or_create(name='xiaoming',age='18',gender=False)
    return HttpResponse('添加成功')
def add_book(request):
    add_usel=Usel(name='xiaobai',age='20',gender=True)
    add_usel.save()
    return HttpResponse('添加成功')
# 查看
def get1(request):
    # get_book=Usel.objects.all()
    get_book=Usel.objects.get(id=2)
    print(get_book)
    return HttpResponse('查询成功')
# 修改
def update1(request):
    Usel.objects.filter(name='xiaobai').update(name='星煞')
    return HttpResponse('修改成功')
# 删除
def del1(request):
    Usel.objects.filter(id=2).delete()
    return HttpResponse('删除成功')
# 自增减1
def pa(request):
    v= Usel.objects.filter(name='星煞')
    v.update(age=F('age')-1)
    return HttpResponse('自增减一')
#一对多
def Dapartment_add(request):
    Dapartment.objects.update_or_create(name='python学院')
    Dapartment.objects.update_or_create(name='java学院')
    Dapartment.objects.update_or_create(name='django学院')
    return HttpResponse('学院添加成功')
def Student_add(request):
    Student.objects.update_or_create(name='小花',age=18,gender=True,dapartment_id=2)
    Student.objects.update_or_create(name='小明',age=20,gender=False,dapartment_id=1)
    Student.objects.update_or_create(name='小黑',age=17,gender=False,dapartment_id=3)
    Student.objects.update_or_create(name='小白', age=20, gender=True, dapartment_id=2)
    Student.objects.update_or_create(name='小红', age=18, gender=True, dapartment_id=1)
    return HttpResponse('学员选校成功')
def age_gt(request):
    gt=Student.objects.filter(age__gt=18)
    print(gt)
    return HttpResponse('大于查询成功')
def age_lte(request):
    lte=Student.objects.filter(age__lte=18)
    print(lte)
    return HttpResponse("小于等于查询成功")
def ds(request):
    P=Student.objects.filter(dapartment__id=1)
    print(P)
    return HttpResponse('多表查询成功')
def test_info(request):
    p1=Student.objects.all().aggregate(Avg('age'))
    p2=Student.objects.all().aggregate(Sum('age'),Count('age'),Max('age'),Min('age'))
    print(p2)
    print(p1)
    return HttpResponse('查询成功')
# F查询: 针对两个字段的值的比较
def text_info1(request):
    rs=Student.objects.filter(dapartment_id=F('id'))
    print(rs)
    return HttpResponse("F查询成功")
#Q聚合查询
def qname(request):
    rs=Student.objects.filter(Q(name='小花')|Q(name='小白'))
    print(rs)
    return HttpResponse('Q查询成功')
def aname(request):
    rs=Student.objects.filter(Q(name='小明')&~Q(age=17))
    print(rs)
    return HttpResponse('Q查询成功')
def method1(request):
    return render(request,'Page/method.html')
#设置cookies
def set_ck(request):
    response=HttpResponse('设置cookies')
    response.delete_cookie()
    response.set_cookie('name','take') #默认关闭浏览器过期
    return response
def get_ck(request):
    cookies=request.COOKIES
    print(cookies)
    return HttpResponse('获取cookies')
def delete_ck(request):
    response=HttpResponse('删除cookies')
    response.delete_cookie('name')
    return response
#session状态保持
def home(request):
    username=request.session.get('username','未登录')
    context={
        'username':username,
    }
    return render(request,'ts22/home.html',context=context)
def login_1(request):
    if request.method=='GET':
        return render(request,'ts22/login.html')
    elif request.method=='POST':
        #重定向
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        #做session状态
        # request.session['username']=username
        # request.session.set_expiry(None) #设置过期时间
        # User.objects.create_user(username=name, password=pwd)
        # user = authenticate(username=name, password=pwd,email=email)
        # print(user)
        print(name)
        if name:
            login(request, name)  # session写操作
            return redirect(reverse('ts_home'))
        #重定向
        return HttpResponse('cuuuuuu')
def logout_1(request):
    #退出登录逻辑
    # request.session.flush()
    logout(request)
    return redirect(reverse('ts_home'))
#文件上传
def upload(request):
    if request.method=='GET':
        return render(request,'ts22/upload.html')
    elif request.method=='POST':
        #file是从html页面中的name元素穿过来的
        f1=request.FILES['file']
        f1_name=os.path.join(MEDIA_ROOT,f1.name)
        with open(f1_name,'wb')as f :
            for i in f1.chunks():
                f.write(i)
        return HttpResponse('11111')
    else:
        return HttpResponse('ERROR')


def add_form(request):
    if request.method=='POST': #提交post请求
        form=AddForm(request.POST) #from表单包含提交的数据
        if form.is_valid(): #验证数据是否合法
            a=form.changed_data['a']
            b=form.changed_data['b']
            print(a,b)
            return HttpResponse(str(int(a))+str(int(b)))
        else:
           form=AddForm()
    return render(request,'ts22/add_form.html')

def register(request):
    if request.method == 'GET': #如果是get请求则返回
        form = RegisterFrom()
        return render(request,'ts22/add_form.html',
                      context={'form':form})
    elif request.method == 'POST': #如果是post请求
        form = RegisterFrom(request.POST)
        if form.is_valid(): #判断验证数据是否合法
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            email = form.cleaned_data.get('email')
            if password == password_repeat:
                user = UserModels.objects.create(username=username, password=password,email=email) #添加数据
                return HttpResponse('注册成功!')
            else:
                return HttpResponse('注册失败!')
        else:
            return HttpResponse('注册失败!')
