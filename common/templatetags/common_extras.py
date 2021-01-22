# 自定义过滤器
from django import template
import datetime
register=template.Library()

def mycut(value,age):
    '''
    将指定字符替换为空
    :param value:
    :param age:
    :return:
    '''
    return value.replace(age,'')
register.filter('mycut',mycut)


@register.filter
def mysupper(value):
    '''
    将所有字母转化为大写
    :param value:
    :return:
    '''
    return value.upper()


@register.filter
def mylower(value):
    '''
    将所有字母转化为小写
    :param value:
    :return:
    '''
    return value.lower()

# 模板标签
@register.simple_tag
def gettime(format_string):
    '''
    定义一个显示当前时间的简单标签,需传入时间格式
    返回一个时间
    :param format_string:
    :return:
    '''
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag(takes_context=True)
def gettime1(context):
    return datetime.datetime.now().strftime('format_string')

@register.inclusion_tag('Page/results.html')
def show_results():
    li = ['python','java','django']
    return {'choices': li}
