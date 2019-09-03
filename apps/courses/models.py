from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField
from organization.models import CourseOrg, Teacher



# Create your models here.

# 课程信息
class Course(models.Model):
    # 课程机构
    course_org = models.ForeignKey(CourseOrg, verbose_name="课程机构", null=True, blank=True, on_delete=models.CASCADE)
    # 课程名称
    name = models.CharField(max_length=50, verbose_name="课程名称")
    # 课程类别
    category = models.CharField(default="后端开发", max_length=20, verbose_name="课程类别")
    # 课程描述
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    # 轮播
    is_banner = models.BooleanField(default=False, verbose_name="是否轮播")
    # 课程讲师
    teacher = models.ForeignKey(Teacher, verbose_name="课程讲师", null=True, blank=True, on_delete=models.CASCADE)
    # 课程须知
    youneed_know = models.CharField(default="", max_length=300, verbose_name="课程须知")
    # 老师告诉你
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="老师告诉你")
    # 课程详细
    detail = UEditorField(u'课程详情', width=600, height=300, toolbars="full", imagePath="course/ueditor/", filePath="course/ueditor/",default="")
    # 课程难度
    degree = models.CharField(verbose_name="学习难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    # 学习时长 单位分钟
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    # 学习人数
    students = models.IntegerField(default=0, verbose_name="学习人数")
    # 收藏人数
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    # 封面图
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)
    # 点击数
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    # 课程标签
    tag = models.CharField(default="", verbose_name="课程标签", max_length=10)
    # 增加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def get_lesson_nums(self):
        all_lessons = self.lesson_set.all()
        return all_lessons.count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        return self.lesson_set.all()

    def __str__(self):
        return self.name


# 章节
class Lesson(models.Model):
    # 外键 ——>指向课程
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    # 章节名称
    name = models.CharField(max_length=100, verbose_name="章节名")
    # 增加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


# 视频 (小节）
class Video(models.Model):
    # 外键 ——> 指向课程
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    # 视频名称
    name = models.CharField(max_length=100, verbose_name="视频名称")
    # 学习时长 单位分钟
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    # 视频url
    url = models.CharField(max_length=200, default="", verbose_name="访问地址")
    # 视频地址
    video_path = models.FileField(default="", upload_to="course/video/%Y/%m", verbose_name="视频文件", max_length=100)
    # 增加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 章节资源
class CourseResource(models.Model):
    # 外键 ——>指向课程
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    # 资源名称
    name = models.CharField(max_length=100, verbose_name="名称")
    # 资源文件
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件", max_length=100)
    # 增加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
