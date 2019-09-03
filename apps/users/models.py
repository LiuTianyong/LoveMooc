from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# 继承Django原有字段  User 表
class UserProfile(AbstractUser):
    # 昵称 ——> 最大长度50  默认值为 空
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    # 生日
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    # 性别
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="female")
    # 地址
    address = models.CharField(max_length=100, default="")
    # 手机号
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 头像文件
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def get_unread_nums(self):
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id).count()

    def __str__(self):
        return self.username


# 发送验证码
class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name="验证码")
    # 邮箱
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    # 发送类型 ——> 注册 / 找回密码
    send_type = models.CharField(verbose_name="验证类型",
                                 choices=(("register", "注册"), ("forget", "找回密码"), ("update_email", "修改邮箱")),
                                 max_length=15)
    #  发送时间 datetime.now()括号必须取掉 若有括号是编译时的时间 无则是实例化的时间
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0} {1}".format(self.email, self.code)


# 轮播图
class Banner(models.Model):
    # 标题
    title = models.CharField(max_length=100, verbose_name="标题")
    # 图片
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100)
    # 跳转url
    url = models.URLField(max_length=200, verbose_name="访问地址")
    # 轮播顺序
    index = models.IntegerField(default=100, verbose_name="顺序")
    # 生成时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
