from django.db import models
from datetime import datetime


# Create your models here.


# 城市
class CityDict(models.Model):
    #  城市
    name = models.CharField(max_length=20, verbose_name="城市")
    # 城市描述
    desc = models.CharField(max_length=200, verbose_name="描述")
    # 添加时间
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 机构
class CourseOrg(models.Model):
    # 机构名称
    name = models.CharField(max_length=50, verbose_name="机构名称")
    # 机构描述
    desc = models.TextField(verbose_name="机构描述")
    # 标签
    tag = models.CharField(default="全国知名", max_length=20, verbose_name="机构标签")
    # 机构类别
    category = models.CharField(verbose_name="机构类别",default="pxjg",max_length=20,choices=(("pxjg","培训结构"),("gr","个人"),("gx","高校")))
    # 点击数
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    # 收藏数
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    # 封面
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="封面图", max_length=100)
    # 机构地址
    address = models.CharField(max_length=150, verbose_name="地址")
    # 学习人数
    students = models.IntegerField(default=0,verbose_name="学习人数")
    # 课程数
    course_nums = models.IntegerField(default=0,verbose_name="课程数")
    # 外键
    city = models.ForeignKey(CityDict, verbose_name="所在城市", on_delete=models.CASCADE)
    # 添加时间
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        return self.teacher_set.all().count()

    def __str__(self):
        return self.name


# 授课老师
class Teacher(models.Model):
    # 设置外键 ——>机构
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)
    # 教师名
    name = models.CharField(max_length=50, verbose_name="教师名")
    # 头像
    image = models.ImageField(default="",upload_to="teacher/%Y/%m",verbose_name="头像",max_length=100)
    # 年龄
    age = models.IntegerField(default=18, verbose_name="年龄")
    # 工作年限
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    # 就职公司
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    # 工作职位
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    # 教学特点
    points = models.CharField(max_length=50, verbose_name="教学特点")
    # 点击数
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    # 收藏数
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    # 添加时间
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "授课教师"
        verbose_name_plural = verbose_name

    def get_course_nums(self):
        return self.course_set.all().count()

    def __str__(self):
        return self.name