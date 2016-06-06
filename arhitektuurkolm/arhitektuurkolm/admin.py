from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.forms import BaseGenericInlineFormSet
from django.core.exceptions import ValidationError

from .models import *


class SubjectAttributeInlineFormset(BaseGenericInlineFormSet):
    def clean(self):
        for form in self.forms:
            try:
                if form.cleaned_data:
                    d = form.cleaned_data
                    if d['attribute_type'].data_type == SubjectAttribute.TEXT:
                        if any([d['value_date'] is not None, d['value_text'] == "",
                                d['value_number'] is not None]):
                            form.add_error('value_text', 'Please set TEXT and TEXT ONLY')
                    if d['attribute_type'].data_type == SubjectAttribute.NUMBER:
                        if any([d['value_date'] is not None, d['value_text'] is not "",
                                d['value_number'] is None]):
                            form.add_error('value_number', 'Please set NUMBER and NUMBER ONLY')
                    if d['attribute_type'].data_type == SubjectAttribute.DATE:
                        if any([d['value_date'] is None, d['value_text'] is not "",
                                d['value_number'] is not None]):
                            form.add_error('value_date', 'Please set DATE and DATE ONLY')
            except AttributeError:
                pass


class SubjectAttributeInline(GenericTabularInline):
    model = SubjectAttributeValue
    ct_field = 'owner_type'
    ct_fk_field = 'owner_fk'
    extra = 1
    formset = SubjectAttributeInlineFormset

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        print(qs)
        return qs


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        exclude = []


class EnterpriseAdmin(admin.ModelAdmin):
    inlines = (SubjectAttributeInline, )
    form = EnterpriseForm


class PersonAdmin(admin.ModelAdmin):
    inlines = (SubjectAttributeInline,)


class EmployeeAdmin(admin.ModelAdmin):
    inlines = (SubjectAttributeInline,)


admin.site.register(Address)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeRole)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(SubjectAttribute)
