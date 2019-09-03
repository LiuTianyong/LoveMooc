from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
import json
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
from django.urls import reverse

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, ForgetForm, UploadImageForm
from .forms import RegisterForm, ModifyPwdForm, UploadInfoForm
from utils.email_send import send_register_email
from utils.minxin_utils import LoginRequiredMixin
from operation.models import UserCourse, UserFavorite, UserMessage
from organization.models import CourseOrg, Teacher
from courses.models import Course
from .models import Banner


# 主页
class IndexView(View):
    def get(self, request):
        all_banners = Banner.objects.all().order_by('index')
        courses = Course.objects.filter(is_banner=False)[:6]
        banner_courses = Course.objects.filter(is_banner=True)[:3]

        course_orgs = CourseOrg.objects.all()[:15]

        return render(request, 'index.html', {
            'all_banners': all_banners,
            'courses': courses,
            'banner_courses': banner_courses,
            'course_orgs': course_orgs,

        })


# 我的消息
class MymessageView(LoginRequiredMixin, View):
    def get(self, request):
        all_message = UserMessage.objects.filter(user=request.user.id)
        all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for unread_message in all_unread_messages:
            unread_message.has_read = True
            unread_message.save()

        # 对个人消息
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        per_page = 5
        p = Paginator(all_message, per_page, request=request)
        messages = p.page(page)

        return render(request, 'usercenter-message.html', {
            "messages": messages,

        })


# 我收藏的课程
class MyFavCourseView(LoginRequiredMixin, View):
    def get(self, request):
        fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=1)
        course_list = []
        for fav_course in fav_teachers:
            course_id = fav_course.fav_id
            course = Course.objects.get(id=course_id)
            course_list.append(course)
        return render(request, 'usercenter-fav-course.html', {
            'course_list': course_list,

        })


# 我收藏的课程机构
class MyFavTeacherView(LoginRequiredMixin, View):
    def get(self, request):
        fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
        teacher_list = []
        for fav_teacher in fav_teachers:
            teacher_id = fav_teacher.fav_id
            teacher = Teacher.objects.get(id=teacher_id)
            teacher_list.append(teacher)
        return render(request, 'usercenter-fav-teacher.html', {
            'teacher_list': teacher_list,

        })


# 我收藏的课程机构
class MyFavOrgView(LoginRequiredMixin, View):
    def get(self, request):
        fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
        org_list = []
        for fav_org in fav_orgs:
            org_id = fav_org.fav_id
            org = CourseOrg.objects.get(id=org_id)
            org_list.append(org)
        return render(request, 'usercenter-fav-org.html', {
            'org_list': org_list,

        })


# 我的课程
class MyCourseView(LoginRequiredMixin, View):
    def get(self, request):
        user_courses = UserCourse.objects.filter(user=request.user)

        return render(request, 'usercenter-mycourse.html', {
            'user_courses': user_courses,

        })


# 修改个人邮箱
class UpdateEmailView(LoginRequiredMixin, View):
    def post(self, request):
        email = request.POST.get("email", "")
        code = request.POST.get("code", "")
        exfsted_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type="update_email")
        if exfsted_records:
            user = request.user
            user.email = email
            user.save()

            result = {'status': 'success'}
            return HttpResponse(json.dumps(result),
                                content_type='application/json')
        else:
            result = {'status': '验证码出错'}
            return HttpResponse(json.dumps(result),
                                content_type='application/json')


# 发送验证码
class SendEmailCodeView(LoginRequiredMixin, View):
    def get(self, request):
        email = request.GET.get("email", "")
        if UserProfile.objects.filter(email=email):
            result = {'email': '邮箱已经存在'}
            return HttpResponse(json.dumps(result),
                                content_type='application/json')
        send_register_email(email, "update_email")
        result = {'email': 'success'}
        return HttpResponse(json.dumps(result),
                            content_type='application/json')


# 个人中心修改密码
class UpdatePwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                result = {'status': 'fail', 'msg': '密码不一致'}
                return HttpResponse(json.dumps(result),
                                    content_type='application/json')
            user = request.user
            user.password = make_password(pwd1)
            user.save()

            result = {'status': 'success'}
            return HttpResponse(json.dumps(result),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors),
                                content_type='application/json')


# 上传头像
class UploadImageView(LoginRequiredMixin, View):
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            # image = image_form.changed_data['image']
            # request.user.image = image
            # request.user.save()
            result = {'status': 'success'}
            return HttpResponse(json.dumps(result),
                                content_type='application/json')
        else:
            result = {'status': 'fail'}
            return HttpResponse(json.dumps(result),
                                content_type='application/json')


'''用户个人信息'''


class UserInfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'usercenter-info.html', {})

    def post(self, request):
        user_info_form = UploadInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            result = {'status': 'success'}
            return HttpResponse(json.dumps(result),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


# 处理重置密码
class ResetView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email": email})

        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


# 提交修改后密码请求处理
class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"msg": "密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd1)
            user.save()

            return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email": email})


# 忘记密码
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, "send_success.html")
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


# 激活用户账户
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


# 继承并重写authenticate方法（重写登陆校验方法）
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 查找得到该对象
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # 由于Django存储密码 加密不可逆，所以对输入的进行加密验证
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 注册
class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # 提取账户
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已经存在"})
            # 提取密码
            pass_word = request.POST.get("password", "")
            # 实例化一个对象
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            # 加密保存
            user_profile.password = make_password(pass_word)
            # 保存到数据库
            user_profile.save()

            # 发送注册消息
            user_message = UserMessage()
            user_message.user = user_profile
            user_message.message = "欢迎注册LoveMooc网"
            user_message.save()

            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


# 登陆
class LoginView(View):

    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        # 实例化 以字典形式传入参数
        login_form = LoginForm(request.POST)
        # 验证是否有错

        if login_form.is_valid():
            # 提取账户
            user_name = request.POST.get("username", "")
            # 提取密码
            pass_word = request.POST.get("password", "")
            # 使用Django自带authenticate校验账户密码合法性
            # 若校验成功返回对象，否则返回None
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = user_name
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, "login.html", {"msg": "用户名未激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form": login_form})


# 登出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


# 404
def page_not_found(request, exception=404):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

# 500
def page_error(request, exception=500):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response

# Create your views here.
# def user_login(request):
#     # 判断请求方式
#     if request.method == "POST":
#         # 提取账户
#         user_name = request.POST.get("username", "")
#         # 提取密码
#         password = request.POST.get("password", "")
#         # 使用Django自带authenticate校验账户密码合法性
#         # 若校验成功返回对象，否则返回None
#         user = authenticate(username=user_name, password=password)
#         if user is not None:
#             login(request, user)
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", {"msg": "用户名或密码错误"})
#     # 若为GET则返回该请求
#     elif request.method == "GET":
#         return render(request, "login.html", {})
