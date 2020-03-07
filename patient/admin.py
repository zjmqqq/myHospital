from django.contrib import admin
from .models import patients,doctor,department,registrationType,registration,scheduling,\
    comment,pGender,contreteTime_a,contreteTime_p,news
class patientsAdmin(admin.ModelAdmin):
    list_display = ('pId', 'pName', 'pPassword','pGender','pIdCard','pTel','pEmail')
    search_fields = ('pId', 'pName', 'pPassword','pGender','pIdCard','pTel','pEmail')
    # list_display = ('pId', 'pName', 'pPassword', 'pIdCard', 'pTel', 'pEmail')
    # search_fields = ('pId', 'pName', 'pPassword', 'pIdCard', 'pTel', 'pEmail')
    ordering = ('pId', )

class doctorAdmin(admin.ModelAdmin):
    list_display = ('dId', 'dName', 'dPassword','dGender','dIdcard','dBirthday','dTel','department','registrationType','dIntroduce','dSpecial')
    search_fields = ('dId', 'dName', 'dPassword','dGender','dIdcard','dBirthday','dTel','department','registrationType','dIntroduce','dSpecial')
    ordering = ('dId',)

class departmentAdmin(admin.ModelAdmin):
    list_display = ('departmentId', 'departmentName','icon','introduce')
    search_fields = ('departmentId', 'departmentName','icon','introduce')
    ordering = ('departmentId',)

class registrationTypeAdmin(admin.ModelAdmin):
    list_display = ('tId', 'type')
    search_fields = ('tId', 'job')
    ordering = ('tId',)

class registrationAdmin(admin.ModelAdmin):
    list_display = ('rId', 'subTime','regTime','ap', 'patients', 'doctor', 'type', 'department')
    search_fields = ('rId', 'subTime','regTime','ap', 'patients', 'doctor', 'type', 'department')
    ordering = ('rId',)

class schedulingAdmin(admin.ModelAdmin):
    list_display = ('sId', 'doctor', 'sTime','remainNumber','ap')
    search_fields = ('sId', 'doctor', 'sTime','remainNumber','ap')
    ordering = ('sId',)

class commentAdmin(admin.ModelAdmin):
    list_display = ('cId', 'doctor', 'patients','content','cTime')
    search_fields = ('cId', 'doctor', 'patients','content','cTime')
    ordering = ('cId',)

class pGenderAdmin(admin.ModelAdmin):
    list_display = ('sId', 'gender')
    search_fields = ('sId', 'gender')
    ordering = ('sId',)

class contreteTime_aAdmin(admin.ModelAdmin):
    list_display = ('ctId', 'a_8_00','a_8_30', 'a_9_00','a_9_30', 'a_10_00','a_10_30', 'a_11_00','a_11_30','scheduling_a')
    search_fields = ('ctId', 'a_8_00','a_8_30', 'a_9_00','a_9_30', 'a_10_00','a_10_30', 'a_11_00','a_11_30','scheduling_a')
    ordering = ('ctId',)

class contreteTime_pAdmin(admin.ModelAdmin):
    list_display = ('ctId', 'p_13_30','p_14_00', 'p_14_30','p_15_00', 'p_15_30','p_16_00', 'p_16_30','scheduling_p')
    search_fields = ('ctId', 'p_13_30','p_14_00', 'p_14_30','p_15_00', 'p_15_30','p_16_00', 'p_16_30','scheduling_p')
    ordering = ('ctId',)


class newsAdmin(admin.ModelAdmin):
    list_display = ('nId', 'pic','title', 'content','publishTime')
    search_fields = ('nId', 'pic','title', 'content','publishTime')
    ordering = ('nId',)

admin.site.register(patients,patientsAdmin)
admin.site.register(doctor,doctorAdmin)
admin.site.register(department,departmentAdmin)
admin.site.register(registrationType,registrationTypeAdmin)
admin.site.register(registration,registrationAdmin)
admin.site.register(scheduling,schedulingAdmin)
admin.site.register(comment,commentAdmin)
admin.site.register(pGender,pGenderAdmin)
admin.site.register(contreteTime_a,contreteTime_aAdmin)
admin.site.register(contreteTime_p,contreteTime_pAdmin)
admin.site.register(news,newsAdmin)

