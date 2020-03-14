from django.shortcuts import redirect, render, HttpResponse
from patient import models
from utils import Pager, Datetime
from utils import base
import datetime
from django.forms import Form
from django.forms import fields, widgets
from django.core.validators import RegexValidator
from captcha.fields import CaptchaField


class LoginForm(Form):
    pTel = fields.CharField(
        label="手机",
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        # form 组件中用正则判断是否符合条件
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^1[35789]\d{9}$', '请输入正确手机号')],
        error_messages={
            "required": "手机号码不能为空",
        }
    )
    # 调用form组件内部方法创建一个长度不大于16且不小于8的密码文本框
    pPassword = fields.CharField(
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


class RegForms(Form):
    pName = fields.CharField(
        label="帐号",
        max_length=16,
        # 自定义类的属性
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "帐号不能为空"
        }
    )
    # 调用form组件内部方法创建一个长度不大于16且不小于8的密码文本框
    pPassword = fields.CharField(
        label="密码",
        max_length=16,
        min_length=8,
        # 定义为密码文本,render_value设置为验证不通过时不把密码刷新掉
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于8位数",
            "required": "密码不能为空"
           }
    )

    re_pwd = fields.CharField(
        label="确认密码",
        max_length=16,
        min_length=8,
        # 定义为密码文本,render_value设置为验证不通过时不把密码刷新掉
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
             "min_length": "密码不能少于8位数",
             "required": "密码不能为空"
           }
    )
    pEmail = fields.EmailField(
        label="邮箱",
        widget=widgets.EmailInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "邮箱地址不能为空",
            # invalid 是校验格式是否正确
            "invalid": "邮箱地址格式错误",
        }
    )
    pTel = fields.CharField(
        label="手机",
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        # form 组件中用正则判断是否符合条件
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^1[35789]\d{9}$', '请输入正确手机号')],
        error_messages={
            "required": "手机号码不能为空",
        }
    )

    # 单radio值为字符串
    pGender_id = fields.IntegerField(
        # choices=(models.gender.objects.all().values_list('sId','sex')),
        label="性别",
        initial=1,
        widget=widgets.RadioSelect(choices=(models.sexual.objects.all().values_list('sId', 'gender')))
        # widget=widgets.RadioSelect(choices=((1, "篮球"), (2, "足球"), (3, "双色球"),))
    )

    pIdCard = fields.CharField(
        label="身份证号",
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        # form 组件中用正则判断是否符合条件
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^\d{17}[\dxX]$', '请输入正确身份证号')],
        error_messages={
            "required": "手机号码不能为空",
        }
    )

    # # 单选Select
    # hobby = forms.fields.ChoiceField(
    #     choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     label="爱好",
    #     initial=3,
    #     widget=forms.widgets.Select()
    # )

    # # 多选Select
    # hobby = forms.fields.MultipleChoiceField(
    #     choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     label="爱好",
    #     initial=[1, 3],
    #     widget=forms.widgets.SelectMultiple()
    # )

    # # 单选checkbox
    # keep = forms.fields.ChoiceField(
    #     label="记住密码",
    #     initial="checked",
    #     widget=forms.widgets.CheckboxInput()
    # )

    # # 多选checkbox
    # hobby = forms.fields.MultipleChoiceField(
    #     choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     label="爱好",
    #     initial=[1, 3],
    #     widget=forms.widgets.CheckboxSelectMultiple()
    # )


class CommentForms(Form):
    content = fields.CharField(
        label="请输入评论：",
        # 自定义类的属性
        widget=widgets.Textarea(attrs={"class": "form-control"}),
        error_messages={
            "required": "评论不能为空",
        }
    )


def add_data(request):
    # 增加
    # models.userType.objects.create(title='一级用户')
    # models.userType.objects.create(title='二级用户')
    # models.userType.objects.create(title='三级用户')
    # models.userInfo.objects.create(name='张三',age=18,ut_id_id=1)
    # models.userInfo.objects.create(name='李四',age=18,ut_id_id=2)
    # models.userInfo.objects.create(name='王五',age=18,ut_id_id=3)
    # models.userInfo.objects.create(name='赵柳',age=18,ut_id_id=1)
    # models.userInfo.objects.create(name='黄芪',age=18,ut_id_id=2)
    # for i in range(50):
    #     name = '科室'+str(i)
    #     models.department.objects.create(departmentName=name)
    import random
    for i in range(100):
        name = 'doctor' + str(i) + '医生'
        IdCard = str(331082199809140000+i)
        Tel = str(13958590000+i)
        department_id = random.randint(1,10)
        registrationType_id = random.randint(1,2)
        models.doctor.objects.create(dName=name,dPassword=123456,
                                     dGender='男',dIdcard=IdCard,
                                     dBirthday='19890612',dTel=Tel,
                                     department_id=department_id,
                                     registrationType_id=registrationType_id,
                                     dIntroduce='医生，钻研学习医学科学技术，挽救生命以治病为业的人，一般指临床医生。按照卫生部、卫健委、医政部有关医疗卫生管理条例的法律法规，主持医患沟通，学术讨论，新技术推广、预后分析、公众教育、护理示教、康复培训、出院教育、执行卫生防疫、计生、大病早期识别干预等法律政治责任、承担部分课题研究等工作，预防出生缺陷提高人口素质，治病救人，履行病情如实告知、合理检查、合理开药、正确诊断，积极治疗的责任。',
                                     dSpecial='This utility animates the CSS transform property,meaning it will override any existing transforms on an element being animated!In this theme')
    # 查询 queryset = [obj1,obj2,...]  正向操作
    # result = models.userInfo.objects.all()
    # for obj in result:
    #     print(obj.name,obj.age,obj.ut_id_id,obj.ut_id.title)

    # 表明小写_set.all()反向操作
    # obj = models.userType.objects.all().first()
    # print(type(obj),obj.title,)
    # for row in obj.userinfo_set.all():
    #     print(row.id,row.name,row.age)
    # queryset  result = models.userInfo.objects.all()
    #            result = models.userInfo.objects.filter()
    # 字典result = models.userInfo.objects.all().values('id','name','ut_id__title')
    # 元祖result = models.userInfo.objects.all().values_list('id','name')
    #
    # from django.db.models import Count
    # v = models.userInfo.objects.values('ut_id_id').annotate(num=Count('id')).filter(num__gt=2)
    # models.userInfo.objects.filter(id__gt=1)
    # models.userInfo.objects.filter(id__lt=1)
    # models.userInfo.objects.filter(id__gte=1)
    # models.userInfo.objects.filter(id__lte=1)
    # models.userInfo.objects.filter(id__in=[1, 2, 3])
    # models.userInfo.objects.filter(id__range=[1, 4])
    # models.userInfo.objects.filter(name__startswith='xxx')
    # models.userInfo.objects.filter(name__endwith='xxx')
    # models.userInfo.objects.filter(name__contains='xxx')
    # models.userInfo.objects.exclude(id=1)
    # print(v)
    # print(v.query)

    # dict = {'pName': '李白', 'pPassword': 'qqqqqqqq', 'pEmail': '1170217264@qq.com',
    # 'pTel': '15168672222', 'pGender_id': 1,
    #  'pIdCard': '331082199809143488'}
    # models.patients.objects.create(**dict)
    # F 在跟新时取得原来的值
    # Q的作用
    # condition_dict = {
    #     'k1': [1, 2, 3, 4],
    #     'k2': [1, ],
    #     'k3': [1, 2, 3]
    # }
    # from django.db.models import Q
    # con = Q()
    # for k, v in condition_dict.items():
    #     q = Q()
    #     q.connector = 'OR'
    #     for i in v:
    #         q.children.append('id', i)
    #     con.add(q, 'AND')
    # models.doctor.objects.filter(con)
    return HttpResponse('...')


@base.checkLogin_p
def index_pat(request):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    news_list = models.news.objects.all().order_by('-publishTime')[:4]
    return render(request, 'patient/index_pat.html', {'obj': obj,
                                                      'news_list': news_list})


@base.checkLogin_p
def detail(request):
    n_id = request.GET.get('id')
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    if n_id:
        news = models.news.objects.get(nId=n_id)
    else:
        news = models.news.objects.get(nId=1)
    return render(request, 'patient/detail.html', {'obj': obj,
                                                   'news': news})


def register(request):
    form_obj = RegForms()
    if request.method == 'POST':
        # 实例化form对象的同时传入从网页通过post方式提交过来的参数
        form_obj = RegForms(request.POST)
        # 调用form_obj校验数据的方法
        if form_obj.is_valid():
            # return HttpResponse("注册成功！")
            # print(form_obj.cleaned_data)
            # 去除字典中的re_pwd项
            del form_obj.cleaned_data["re_pwd"]
            print(form_obj.cleaned_data)
            models.patients.objects.create(**form_obj.cleaned_data)
            return redirect('/patient/login/')

    return render(request, "patient/register.html", {"form_obj": form_obj})


def login(request):
    error_msg = ""
    form_obj = LoginForm()
    if request.method == "POST":
        form_obj = LoginForm(request.POST)
        if form_obj.is_valid():
            p_tel = form_obj.cleaned_data.get("pTel")
            pwd = form_obj.cleaned_data.get("pPassword")
            print(form_obj.cleaned_data)
            try:
                obj = models.patients.objects.get(pTel=p_tel, pPassword=pwd)
                if obj:
                    request.session['pName'] = obj.pName
                    request.session['pId'] = obj.pId
                    return redirect('/patient/index_pat/')

                else:
                    error_msg = "用户名或密码错误"
            except Exception as e:
                print(e)
                error_msg = "用户名或密码错误"

    return render(request, "patient/login_pat.html", {"form_obj": form_obj, "error_msg": error_msg})


def logout(request):
    del request.session['pName']
    del request.session['pId']
    return redirect('/patient/login/')


@base.checkLogin_p
def edit_info(request):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    if request.method == 'GET':
        p_id = request.session.get('pId')
        # dic = models.patients.objects.filter(pId=pId).values('pName', 'pPassword','pEmail', 'pTel',
        # 'pGender_id','pIdCard')
        dic = models.patients.objects.get(pId=p_id)
        print('dic1', dic.pId)
        form_obj = RegForms(initial={
            'pName': dic.pName,
            'pPassword': dic.pPassword,
            'pEmail': dic.pEmail,
            'pTel': dic.pTel,
            'pGender_id': dic.pGender_id,
            'pIdCard': dic.pIdCard,
        })
        return render(request, 'patient/editInfo.html', {'form_obj': form_obj,
                                                         'obj': obj,
                                                         })
    else:
        form_obj = RegForms(request.POST)
        p_id = request.session.get('pId')
        if form_obj.is_valid():
            del form_obj.cleaned_data["re_pwd"]
            print(form_obj.cleaned_data)
            models.patients.objects.filter(pId=p_id).update(**form_obj.cleaned_data)
            return redirect('/patient/index_pat/')
        return render(request, 'patient/editInfo.html', {'form_obj': form_obj,
                                                         'obj': obj,
                                                         })


@base.checkLogin_p
def choose_type(request):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    li = '<li><a href="/patient/chooseType/">医生类型</a></li>'
    return render(request, 'patient/chooseType.html', {'li': li,
                                                       'obj': obj,
                                                       })


@base.checkLogin_p
def choose_dep(request, register_type):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    if request.method == "GET":
        li = '<li><a href="/patient/chooseType/">医生类型</a></li> ' \
             '<li><a href="/patient/chooseDep/'+register_type+'">部门</a></li>'
        page_count = models.department.objects.all().count()
        page_info = Pager.PageInfo(request.GET.get('page'), 8, page_count, 7, '/patient/chooseDep/'+register_type)
        dep_list = models.department.objects.all()[page_info.start(): page_info.end()]
        obj1 = render(request, 'patient/chooseDep.html', {'dep_list': dep_list,
                                                          'page_info': page_info,
                                                          'obj': obj,
                                                          'li': li})
        obj1.set_cookie('registerType', register_type, max_age=6000)
        return obj1
    else:
        require = request.POST.get('require')
        page_count = models.department.objects.filter(departmentName__contains=require).count()
        page_info = Pager.PageInfo(request.GET.get('page'), 9, page_count, 7, '/patient/chooseDep/'+register_type)
        dep_list = models.department.objects.filter(departmentName__contains=require)[page_info.start():page_info.end()]
        return render(request, 'patient/chooseDep.html', {'dep_list': dep_list,
                                                          'obj': obj,
                                                          'page_info': page_info})


@base.checkLogin_p
def choose_doc(request, dep_id):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    day1 = request.GET.get('day')
    register_type = request.COOKIES.get('registerType')
    print(type(day1))
    day_list = Datetime.myDate()
    day_dic = {}
    for index, day in enumerate(day_list):
        day_dic[day] = index
    li = '<li><a href="/patient/chooseType/">医生类型</a></li> ' \
         '<li><a href="/patient/chooseDep/' + register_type + '">部门</a></li> ' \
         '<li><a href="/patient/chooseDoc/' + dep_id + '">医生</a></li>'
    if day1:
        day1 = int(day1)
        user_list = []
        obj_list = models.scheduling.objects.filter(sTime=day_list[day1])
        for obj in obj_list:
            user_list.append(obj.doctor)
        print(obj_list)
        return render(request, 'patient/chooseDoc.html', {'user_list': user_list,
                                                          'day_dic': day_dic,
                                                          'li': li,
                                                          'obj': obj,
                                                          'depId': dep_id,
                                                          })
    else:
        page_count = models.doctor.objects.filter(department_id=dep_id, registrationType_id=register_type).count()
        page_info = Pager.PageInfo(request.GET.get('page'), 9, page_count, 5, '/patient/chooseDoc/'+dep_id)
        user_list = models.doctor.objects.filter(department_id=dep_id,
                                                 registrationType_id=register_type)[page_info.start():page_info.end()]
        obj1 = render(request, 'patient/chooseDoc.html', {'user_list': user_list,
                                                          'page_info': page_info,
                                                          'day_dic': day_dic,
                                                          'li': li,
                                                          'obj': obj,
                                                          'depId': dep_id,
                                                          })
        obj1.set_cookie('depId', dep_id, max_age=6000)
        return obj1


@base.checkLogin_p
def choose_day(request, doc_id):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    register_type = request.COOKIES.get('registerType')
    dep_id = request.COOKIES.get('depId')
    li = '<li><a href="/patient/chooseType/">医生类型</a></li> ' \
         '<li><a href="/patient/chooseDep/' + register_type + '">部门</a></li> ' \
         '<li><a href="/patient/chooseDoc/' + dep_id + '">医生</a></li>' \
         '<li><a href="/patient/chooseDay/' + doc_id + '">日期</a></li>'
    day_list = Datetime.myDate()
    user_list_a = models.scheduling.objects.filter(doctor_id=doc_id, ap=1)
    user_list_p = models.scheduling.objects.filter(doctor_id=doc_id, ap=0)
    num_list_a = [0, 0, 0, 0, 0, 0, 0]
    num_list_p = [0, 0, 0, 0, 0, 0, 0]
    for obj in user_list_a:
        for index, day in enumerate(day_list):
            if obj.sTime == day:
                num_list_a[index] = obj

    for obj in user_list_p:
        for index, day in enumerate(day_list):
            if obj.sTime == day:
                num_list_p[index] = obj
    doc = models.doctor.objects.get(dId=doc_id)
    comment_list = models.comment.objects.filter(doctor_id=doc_id)
    obj1 = render(request, 'patient/chooseDay.html', {
        'day_list': day_list,
        'user_list_a': num_list_a,
        'user_list_p': num_list_p,
        'comment_list': comment_list,
        'obj': obj,
        'doc': doc,
        'li': li})
    obj1.set_cookie('docId', doc_id, max_age=6000)
    return obj1


@base.checkLogin_p
def choose_time(request, s_id):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    register_type = request.COOKIES.get('registerType')
    doc_id = request.COOKIES.get('docId')
    dep_id = request.COOKIES.get('depId')
    li = '<li><a href="/patient/chooseType/">医生类型</a></li> ' \
         '<li><a href="/patient/chooseDep/' + register_type + '">部门</a></li> ' \
         '<li><a href="/patient/chooseDoc/' + dep_id + '">医生</a></li>' \
         '<li><a href="/patient/chooseDay/' + doc_id + '">日期</a></li>' \
         '<li><a href="/patient/chooseTime/' + s_id + '">时间</a></li>'
    obj_sch = models.scheduling.objects.get(sId=s_id)
    print(obj_sch.ap)
    if obj_sch.ap:
        print('a')
        obj_dic = models.contreteTime_a.objects.filter(scheduling_a=s_id).values('a_8_00', 'a_8_30', 'a_9_00', 'a_9_30',
                                                                                 'a_10_00', 'a_10_30', 'a_11_00',
                                                                                 'a_11_30').first()
        obj_time = models.contreteTime_a.objects.get(scheduling_a=s_id)
        obj1 = render(request, 'patient/chooseTime.html', {'obj_dic': obj_dic,
                                                           'obj_sch': obj_sch,
                                                           'obj': obj,
                                                           'li': li})
        obj1.set_cookie('ctId', obj_time.ctId, max_age=60000)
        return obj1
    else:
        print('p')
        obj_dic = models.contreteTime_p.objects.filter(scheduling_p=s_id).values('p_13_30', 'p_14_00', 'p_14_30',
                                                                                 'p_15_00', 'p_15_30', 'p_16_00',
                                                                                 'p_16_30',).first()

        obj_time = models.contreteTime_p.objects.get(scheduling_p=s_id)
        obj1 = render(request, 'patient/chooseTime.html', {'obj_dic': obj_dic,
                                                           'obj_sch': obj_sch,
                                                           'obj': obj,
                                                           'li': li})
        obj1.set_cookie('ctId', obj_time.ctId, max_age=60000)
        return obj1


@base.checkLogin_p
def confirm(request, s_id):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    if request.method == "GET":
        doc_id = request.COOKIES.get('docId')
        dep_id = request.COOKIES.get('depId')
        p_id = request.session.get('pId')
        register_type = request.COOKIES.get('registerType')
        time1 = request.GET.get('time')
        li = '<li><a href="/patient/chooseType/">医生类型</a></li> ' \
             '<li><a href="/patient/chooseDep/' + register_type + '">部门</a></li> ' \
             '<li><a href="/patient/chooseDoc/' + dep_id + '">医生</a></li>' \
             '<li><a href="/patient/chooseDay/' + doc_id + '">时间</a></li>' \
             '<li class="active">确认</li>'
        doc = models.doctor.objects.get(dId=doc_id)
        dep = models.department.objects.get(departmentId=dep_id)
        pat = models.patients.objects.get(pId=p_id)
        register_type = models.registrationType.objects.get(tId=register_type)
        scheduling = models.scheduling.objects.get(sId=s_id)
        # if scheduling.ap:
        #     ct = models.contreteTime_a.objects.get(ctId=ctId)
        # else:
        #     ct = models.contreteTime_p.objects.get(ctId=ctId)
        return render(request, 'patient/confirm.html', {'doc': doc,
                                                        'dep': dep,
                                                        'pat': pat,
                                                        'obj': obj,
                                                        'registerType': register_type,
                                                        'scheduling': scheduling,
                                                        'time1': time1,
                                                        'li': li})
    else:
        re_info = request.POST.get('reInfo')
        re_info_list = re_info.split('+')
        ct_id = request.COOKIES.get('ctId')
        # doc dep reg sch time 1 1 1 6 time
        sch = models.scheduling.objects.filter(sId=re_info_list[3])
        obj = models.scheduling.objects.get(sId=re_info_list[3])
        p_id = request.session.get('pId')
        models.registration.objects.create(patients_id=p_id, doctor_id=re_info_list[0], ap=obj.ap,
                                           type_id=re_info_list[2], department_id=re_info_list[1],
                                           subTime=datetime.datetime.now(), regTime=obj.sTime)
        sch.update(remainNumber=obj.remainNumber-1)
        if re_info_list[4] == 'a_8_00':
            models.contreteTime_a.objects.filter(ctId=ct_id).update(a_8_00=False)
        elif re_info_list[4] == 'a_8_30':
            models.contreteTime_a.objects.filter(ctId=ct_id).update(a_8_30=False)
        elif re_info_list[4] == 'a_9_00':
            models.contreteTime_a.objects.filter(ctId=ct_id).update(a_9_00=False)
        elif re_info_list[4] == 'a_9_30':
            models.contreteTime_a.objects.filter(ctId=ct_id).update(a_9_30=False)
        elif re_info_list[4] == 'a_10_00':
            models.contreteTime_a.objects.filter(ctId=ct_id).update(a_10_00=False)
        elif re_info_list[4] == 'a_10_30':
            models.contreteTime_a.objects.filter(ctId=ct_id).update(a_10_30=False)
        elif re_info_list[4] == 'a_11_00':
            models.contreteTime_a.objects.filter(ctId=ct_id).update(a_11_00=False)
        elif re_info_list[4] == 'a_11_30':
            models.contreteTime_a.objects.filter(ctId=ct_id).update(a_11_30=False)
        elif re_info_list[4] == 'p_13_30':
            models.contreteTime_p.objects.filter(ctId=ct_id).update(p_13_30=False)
        elif re_info_list[4] == 'p_14_00':
            models.contreteTime_p.objects.filter(ctId=ct_id).update(p_14_00=False)
        elif re_info_list[4] == 'p_14_30':
            models.contreteTime_p.objects.filter(ctId=ct_id).update(p_14_30=False)
        elif re_info_list[4] == 'p_15_00':
            models.contreteTime_p.objects.filter(ctId=ct_id).update(p_15_00=False)
        elif re_info_list[4] == 'p_15_30':
            models.contreteTime_p.objects.filter(ctId=ct_id).update(p_15_30=False)
        elif re_info_list[4] == 'p_16_00':
            models.contreteTime_p.objects.filter(ctId=ct_id).update(p_16_00=False)
        elif re_info_list[4] == 'p_16_30':
            models.contreteTime_p.objects.filter(ctId=ct_id).update(p_16_30=False)

        return redirect('/patient/index_pat/')


@base.checkLogin_p
def reg_rec(request):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    day1 = request.GET.get('day')
    p_id = request.session.get('pId')
    print(type(day1))
    day_list = Datetime.myDate()
    day_dic = {}
    for index, day in enumerate(day_list):
        day_dic[day] = index
    if day1:
        day1 = int(day1)
        print(day_list[day1])
        reg_list = models.registration.objects.filter(patients__pId=p_id, regTime=day_list[day1])
        print(reg_list)
        return render(request, 'patient/regRec.html', {'reg_list': reg_list,
                                                       'day_dic': day_dic,
                                                       'obj': obj,
                                                       })
    else:
        reg_list = models.registration.objects.filter(patients__pId=p_id)
        return render(request, 'patient/regRec.html', {'reg_list': reg_list,
                                                       'day_dic': day_dic,
                                                       'obj': obj,
                                                       })


@base.checkLogin_p
def withdraw_num(request):
    reg_id = request.POST.get('regId')
    try:
        models.registration.objects.filter(rId=reg_id).update(regState=False)
    except Exception as e:
        print(e)
        return redirect('/patient/regRec/')
    return redirect('/patient/regRec/')


@base.checkLogin_p
def historical_inquiry(request):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    his_list = models.registration.objects.filter(patients_id=p_id, visitState=True)
    print(his_list)
    return render(request, 'patient/historicalInquiry.html', {'obj': obj,
                                                              'his_list': his_list,
                                                              })


@base.checkLogin_p
def evaluate(request):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    if request.method == 'GET':
        r_id = request.GET.get('id')
        form_obj = CommentForms()
        temp = render(request, "patient/evaluate.html", {"form_obj": form_obj,
                                                         "obj": obj,
                                                         })
        temp.set_cookie('comment_id', r_id, max_age=6000)
        return temp
    else:
        form_obj = CommentForms(request.POST)
        now_time = datetime.datetime.now()
        r_id = request.COOKIES.get('comment_id')
        print(r_id)
        reg = models.registration.objects.get(rId=r_id)
        if form_obj.is_valid():
            content = form_obj.cleaned_data.get("content")
            models.comment.objects.create(content=content, cTime=now_time, registration_id=reg.rId,
                                          doctor_id=reg.doctor_id, patients_id=reg.patients_id)
            models.registration.objects.filter(rId=r_id).update(evaluateState=True)
            return redirect('/patient/myEval/')
        return render(request, "patient/evaluate.html", {"form_obj": form_obj,
                                                         "obj": obj,
                                                         })


def my_eval(request):
    p_id = request.session.get('pId')
    obj = models.patients.objects.get(pId=p_id)
    page_count = models.comment.objects.filter(patients_id=p_id).count()
    page_info = Pager.PageInfo(request.GET.get('page'), 8, page_count, 7, '/patient/myEval/')
    comment_list = models.comment.objects.filter(patients_id=p_id)[page_info.start(): page_info.end()]
    obj1 = render(request, 'patient/my_eval.html', {'comment_list': comment_list,
                                                    'page_info': page_info,
                                                    'obj': obj,
                                                    })
    return obj1


def eval_doctor(request):
    pass