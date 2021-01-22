from django import forms
class AddForm(forms.Form):
    first=forms.IntegerField()
    secont=forms.IntegerField()
class RegisterFrom(forms.Form):
    username = forms.CharField(max_length=20,min_length=6)
    password = forms.CharField(max_length=8,min_length=6,
                               widget=forms.PasswordInput(     #widget  负责渲染网页上HTML 表单的输入元素和提取提交的原始数据
                                   attrs={'placeholder':'请输入密码'}),
                               error_messages={'min_length': '密码长度小于6',  #报错信息
                                               'max_length': '密码长度超过8了'})

    password_repeat = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
