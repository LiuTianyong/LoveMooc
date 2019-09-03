__author__ = 'LiuTianyong'
__date__ = '2019/8/17 20:08'

import re
from django import forms

from operation.models import UserAsk


# 利用ModelForm继承关系进行表单验证
class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        """
        验证手机号码是否合法
        """
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")