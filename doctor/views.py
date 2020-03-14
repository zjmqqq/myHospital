from django.shortcuts import redirect, render
from patient import models
from utils import Datetime
from utils import base
import datetime
from django.forms import Form
from django.forms import fields, widgets
from django.core.validators import RegexValidator
from captcha.fields import CaptchaField
from utils import Pager


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
            d_tel = form_obj.cleaned_data.get("dTel")
            pwd = form_obj.cleaned_data.get("dPassword")
            print(form_obj.cleaned_data)
            try:
                obj = models.doctor.objects.get(dTel=d_tel, dPassword=pwd)
                if obj:
                    request.session['dName'] = obj.dName
                    request.session['dId'] = obj.dId
                    return redirect('/doctor/index_doc')
                else:
                    error_msg = "用户名或密码错误"
            except Exception as e:
                print(e)
                error_msg = "用户名或密码错误"
    return render(request, "doctor/login_doc.html", {"form_obj": form_obj, "error_msg": error_msg})


@base.checkLogin_d
def index_doc(request):
    d_id = request.session.get('dId')
    doc = models.doctor.objects.get(dId=d_id)
    return render(request, 'doctor/index_doc.html', {'doc': doc})


def logout(request):
    del request.session['dName']
    del request.session['dId']
    return redirect('/doctor/login/')


@base.checkLogin_d
def scheduling(request):
    doc_id = request.session.get('dId')
    day_list = Datetime.myDate()
    sch_a = models.scheduling.objects.filter(doctor_id=doc_id, ap=1)
    sch_p = models.scheduling.objects.filter(doctor_id=doc_id, ap=0)
    num_list_a = [0, 0, 0, 0, 0, 0, 0]
    num_list_p = [0, 0, 0, 0, 0, 0, 0]
    for obj in sch_a:
        for index, day in enumerate(day_list):
            if obj.sTime == day:
                num_list_a[index] = obj

    for obj in sch_p:
        for index, day in enumerate(day_list):
            if obj.sTime == day:
                num_list_p[index] = obj
    doc = models.doctor.objects.get(dId=doc_id)
    obj = render(request, 'doctor/scheduling_doc.html', {
        'day_list': day_list,
        'sch_a': num_list_a,
        'sch_p': num_list_p,
        'doc': doc,
        })
    return obj


@base.checkLogin_d
def check_reg(request):
    d_id = request.session.get('dId')
    today = datetime.date.today()
    doc = models.doctor.objects.get(dId=d_id)
    day1 = request.GET.get('day')
    day_list = Datetime.myDate()
    day_dic = {}
    for index, day in enumerate(day_list):
        day_dic[day] = index
    if day1:
        day1 = int(day1)
        print(day1)
        print(day_list[day1])
        # pat_list = []
        reg_list = models.registration.objects.filter(doctor_id=d_id, regTime=day_list[day1])
        print(reg_list)
        # for obj in obj_list:
        #     user_list.append(obj.doctor)
        # print(obj_list)
        return render(request, 'doctor/checkReg.html', {'reg_list': reg_list,
                                                        'day_dic': day_dic,
                                                        'doc': doc,
                                                        })
    else:
        print(today)
        reg_list = models.registration.objects.filter(doctor_id=d_id, regTime__gte=today)
        print(reg_list)
        return render(request, 'doctor/checkReg.html', {'reg_list': reg_list,
                                                        'day_dic': day_dic,
                                                        'doc': doc})


@base.checkLogin_d
def check_info(request):
    today = datetime.date.today()
    doc_id = request.session.get('dId')
    doc = models.doctor.objects.get(dId=doc_id)
    reg_list = models.registration.objects.filter(doctor_id=doc_id, regTime__gte=today)
    return render(request, 'doctor/check_info.html', {'doc': doc,
                                                      'reg_list': reg_list,
                                                      })


@base.checkLogin_d
def visit(request, reg_id):
    models.registration.objects.filter(rId=reg_id).update(visitState=1)
    return redirect('/doctor/checkReg/')


@base.checkLogin_d
def view_comment(request):
    doc_id = request.session.get('dId')
    doc = models.doctor.objects.get(dId=doc_id)
    page_count = models.comment.objects.filter(doctor_id=doc_id).count()
    page_info = Pager.PageInfo(request.GET.get('page'), 8, page_count, 7, '/doctor/view_comment/')
    comment_list = models.comment.objects.filter(doctor_id=doc_id)[page_info.start(): page_info.end()]
    obj1 = render(request, 'doctor/view_comment.html', {'comment_list': comment_list,
                                                    'page_info': page_info,
                                                    'doc': doc,
                                                    })
    return obj1