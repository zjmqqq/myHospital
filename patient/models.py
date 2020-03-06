from django.db import models


class pGender(models.Model):
    sId = models.AutoField(primary_key=True, verbose_name='性别ID')
    gender = models.CharField(max_length=10,verbose_name='性别',null=True,default='')


class patients (models.Model):
    pId = models.AutoField(primary_key=True, verbose_name='用户ID')
    pName = models.CharField(max_length=200, verbose_name='用户姓名')
    pPassword = models.CharField(max_length=200, verbose_name='用户密码')
    pGender = models.ForeignKey('pGender',verbose_name='用户性别',default=1)
    pIdCard = models.CharField(max_length=200, verbose_name='用户身份证号')
    pTel = models.CharField(max_length=200, unique=True, verbose_name='用户手机号码')
    balance = models.IntegerField(default=0, verbose_name='余额')
    pEmail = models.EmailField(default='',verbose_name='邮箱号')
    def __str__(self):
        return self.pName


class doctor (models.Model):
    dId = models.AutoField(primary_key=True, verbose_name='医生ID')
    dName = models.CharField(max_length=200, verbose_name='医生姓名')
    dPassword = models.CharField(max_length=200, verbose_name='医生密码')
    dGender = models.CharField(max_length=200, verbose_name='医生性别')
    dIdcard = models.CharField(max_length=200, verbose_name='医生身份证号')
    dBirthday = models.CharField(max_length=200, verbose_name='医生生日')
    dTel = models.CharField(max_length=200, unique=True, verbose_name='医生手机号码')
    department = models.ForeignKey('department',on_delete=models.CASCADE, verbose_name='部门名称')
    registrationType = models.ForeignKey('registrationType',on_delete=models.CASCADE, verbose_name='是否专家')
    dIntroduce = models.CharField(max_length=200,verbose_name='医生介绍')
    dSpecial = models.CharField(max_length=200,verbose_name='医生特长')
    charge = models.IntegerField(verbose_name='挂号费用',default=12)

    def __str__(self):
        return self.dName


class department(models.Model):
    departmentId = models.AutoField(primary_key=True, verbose_name='部门ID')
    departmentName = models.CharField(max_length=200, verbose_name='部门名字')
    icon = models.CharField(max_length=200,verbose_name='图片',default='fa fa-hospital-o')
    introduce = models.CharField(max_length=200,verbose_name='部门介绍',default='')
    def __str__(self):
        return self.departmentName


class registrationType(models.Model):
    tId = models.AutoField(primary_key=True, verbose_name='')
    type = models.CharField(max_length=20, verbose_name='医生类型')
    def __str__(self):
        return self.type


class registration(models.Model):
    rId = models.AutoField(primary_key=True, verbose_name='预约ID')
    subTime = models.DateTimeField(verbose_name='提交时间')
    regTime = models.DateField(verbose_name='预约时间')
    ap = models.BooleanField(default=True, verbose_name='上午/下午')
    patients = models.ForeignKey('patients', on_delete=models.CASCADE, verbose_name='病人名字')
    doctor = models.ForeignKey('doctor', on_delete=models.CASCADE, verbose_name='医生姓名')
    type = models.ForeignKey('registrationType', on_delete=models.CASCADE, verbose_name='医生类型')
    department = models.ForeignKey('department', on_delete=models.CASCADE, verbose_name='部门名称')
    regState = models.BooleanField(default=True,verbose_name='预约状态')
    visitState = models.BooleanField(default=False,verbose_name='就诊状态')


class scheduling(models.Model):
    sId = models.AutoField(primary_key=True, verbose_name='排班ID')
    doctor = models.ForeignKey('doctor', on_delete=models.CASCADE, verbose_name='医生名字')
    sTime = models.DateField(verbose_name='排班日期')
    remainNumber = models.IntegerField(verbose_name='剩余号码')
    ap = models.BooleanField(default=True,verbose_name='上午/下午')

    def __str__(self):
        return str(self.sId)


class comment(models.Model):
    cId = models.AutoField(primary_key=True, verbose_name='评论ID')
    content = models.CharField(max_length=200,verbose_name='评论内容')
    doctor = models.ForeignKey('doctor',on_delete=models.CASCADE, verbose_name='医生名称')
    patients = models.ForeignKey('patients',on_delete=models.CASCADE, verbose_name='用户名称')
    cTime = models.DateTimeField(verbose_name='评论时间')


class contreteTime_a(models.Model):
    ctId = models.AutoField(primary_key=True)
    a_8_00 = models.BooleanField(default=True,verbose_name='8:00')
    a_8_30 = models.BooleanField(default=True,verbose_name='8:30')
    a_9_00 = models.BooleanField(default=True,verbose_name='9:00')
    a_9_30 = models.BooleanField(default=True,verbose_name='9:30')
    a_10_00 = models.BooleanField(default=True,verbose_name='10:00')
    a_10_30 = models.BooleanField(default=True,verbose_name='10:30')
    a_11_00 = models.BooleanField(default=True,verbose_name='11:00')
    a_11_30 = models.BooleanField(default=True,verbose_name='11:30')
    scheduling_a = models.OneToOneField('scheduling',verbose_name='排班ID')


class contreteTime_p(models.Model):
    ctId = models.AutoField(primary_key=True)
    p_13_30 = models.BooleanField(default=True,verbose_name='13:30')
    p_14_00 = models.BooleanField(default=True,verbose_name='14:00')
    p_14_30 = models.BooleanField(default=True,verbose_name='14:30')
    p_15_00 = models.BooleanField(default=True,verbose_name='15:00')
    p_15_30 = models.BooleanField(default=True,verbose_name='15:30')
    p_16_00 = models.BooleanField(default=True,verbose_name='16:00')
    p_16_30 = models.BooleanField(default=True,verbose_name='16:30')
    scheduling_p = models.OneToOneField('scheduling',verbose_name='排班ID')




