from django.db import models
import pymysql

# Create your models here.

# 继承制models
# 数据库类型和表的关系
# 属性和表字段的对应关系

class Usel(models.Model):
    # id=models.AutoField(primary_key=True) #主键可以省略，django会给我们自动加上
    name=models.CharField(max_length=100) #设置字符串长度
    age=models.IntegerField()
    gender=models.BooleanField()
    def __str__(self):    #这个__str__方法作用在我们查询时看到
        return self.name

# 创建学院表，学生表，课程表
class Dapartment(models.Model):
    # id可以不写
    name=models.CharField('学院',max_length=100,unique=True) #unique=True 唯一
    def __str__(self):
        return self.name
class Student(models.Model):
    name=models.CharField('姓名',max_length=100,unique=True)
    age=models.IntegerField('年龄',max_length=20)
    gender=models.BooleanField(default=True)
    #外键关联
    dapartment=models.ForeignKey('Dapartment',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class UserModels(models.Model):
    username=models.CharField(max_length=20,unique=True)
    Password=models.CharField(max_length=20,)
    email=models.EmailField()
    class Meta:
        db_table='UserModels'
    def __str__(self):
        return self.username
