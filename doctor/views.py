from django.shortcuts import render
from patient import models
# Create your views here.
from django.shortcuts import redirect, render,HttpResponse
import pymysql
from patient import models
from utils import Pager, Datetime
import json
from utils import base
import random
import datetime
from django.forms import Form
from django.forms import fields,widgets
from django.core.validators import RegexValidator
from captcha.fields import CaptchaField

class LoginForm(Form):
    dTel = fields.CharField(
        label="手机",
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        # form 组件中用正则判断是否符合条件
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^1[35789]\d{9}$', '请输入正确手机号')],
        error_messages={
            "required": "手机号码不能为空",
        }
    )
    # 调用form组件内部方法创建一个长度不大于16且不小于8的密码文本框
    dPassword = fields.CharField(
        label="密码",
        max_length=16,
        min_length=6,
        # 定义为密码文本,render_value设置为验证不通过时不把密码刷新掉
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位数",
            "required": "密码不能为空"
        }
    )

    captcha = CaptchaField(
        label='验证码',
        error_messages={
            'invalid': '验证码输入错误',
        }
    )

def login(request):
    error_msg = ""
    form_obj = LoginForm()
    if request.method == "POST":
        form_obj = LoginForm(request.POST)
        if form_obj.is_valid():
            dTel = form_obj.cleaned_data.get("dTel")
            pwd = form_obj.cleaned_data.get("dPassword")
            print(form_obj.cleaned_data)
            try:
                obj = models.doctor.objects.get(dTel=dTel,dPassword=pwd)
                if obj:
                    request.session['dName'] = obj.dName
                    request.session['dId'] = obj.dId
                    return redirect('/doctor/index_doc')
                else:
                    error_msg = "用户名或密码错误"
            except:
                error_msg = "用户名或密码错误"
    return render(request, "doctor/login_doc.html", {"form_obj": form_obj, "error_msg": error_msg})

@base.checkLogin_d
def index_doc(request):
    return render(request, 'doctor/mother_doc.html')