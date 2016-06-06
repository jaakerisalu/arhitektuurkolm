from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import *


class SubjectAttributeInline(GenericTabularInline):
    model = SubjectAttributeValue
    ct_field = 'owner_type'
    ct_fk_field = 'owner_fk'
    extra = 1


class EnterpriseAdmin(admin.ModelAdmin):
    inlines = (SubjectAttributeInline, )

admin.site.register(Address)
admin.site.register(Employee)
admin.site.register(EmployeeRole)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Person)
admin.site.register(SubjectAttribute)
