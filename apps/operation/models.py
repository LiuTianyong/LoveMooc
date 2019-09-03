from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course


# Create your models here.

# 用户咨询模块
class UserAsk(models.Model):
    # 咨询用户姓名
    name = models.CharField(max_length=20, verbose_name="姓名")
    # 手机号码
    mobile = models.CharField(max_length=11, verbose_name="手机")
    # 课程名称
    course_name = models.CharField(max_length=50, verbose_name="课程名")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


# 用户评论
class CourseComments(models.Model):
    # 外键 ——> 用户
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    # 外键 ——> 课程
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    # 评论
    comments = models.CharField(max_length=200, verbose_name="评论")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


# 用户收藏
class UserFavorite(models.Model):
    # 外键 ——> 用户
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    # 收藏数据ID
    fav_id = models.IntegerField(default=0, verbose_name="数据ID")
    # 收藏类型
    fav_type = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), default=1, verbose_name="收藏类型")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


# 用户消息
class UserMessage(models.Model):
    # 用户 ——> 当0 说明系统发给所有用户  否则记录接受用户id
    user = models.IntegerField(default=0, verbose_name="接受用户")
    # 消息
    message = models.CharField(max_length=500, verbose_name="消息内容")
    # 是否已读
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


# 用户课程
class UserCourse(models.Model):
    # 外键 ——> 用户
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    # 外键 ——> 课程
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    # 学习时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username + "  " + self.course.name
