from django.db import models

# Create your models here.
#定义一个类就是定义一个数据库的表
class UserInfo(models.Model):
    username = models.CharField(max_length=18)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    def __repr__(self):
        return self.username


