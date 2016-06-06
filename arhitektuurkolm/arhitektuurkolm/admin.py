from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import messages
from django.contrib.contenttypes.forms import BaseGenericInlineFormSet
from django.core.exceptions import ValidationError

from .models import *


class SubjectAttributeInlineFormset(BaseGenericInlineFormSet):
    def clean(self):
        for form in self.forms:
            try:
                if form.cleaned_data:
                    d = form.cleaned_data
                    attr_type = d['attribute_type']
                    correct_owner = attr_type.belongs_to_type
                    # I apologize to the gods of Python for __class__.__name__ And everything else
                    parent_class_name = self.instance.__class__.__name__.lower()
                    # Validate the attribute type
                    attribute_type_wrong = False

                    if (parent_class_name == "enterprise" and
                            correct_owner != SubjectAttribute.ENTERPRISE)\
                        or (parent_class_name == "person" and
                            correct_owner != SubjectAttribute.PERSON)\
                        or (parent_class_name == "employee" and
                            correct_owner != SubjectAttribute.EMPLOYEE)\
                        or (parent_class_name == "customer" and
                            correct_owner != SubjectAttribute.CUSTOMER):
                        form.add_error('attribute_type', 'That attribute cannot be used with the current parent object')
                        attribute_type_wrong = True

                    # Validate on the data types
                    if not attribute_type_wrong:
                        if attr_type.data_type == SubjectAttribute.TEXT:
                            if any([d['value_date'] is not None, d['value_text'] == "",
                                    d['value_number'] is not None]):
                                form.add_error('value_text', 'Please set TEXT and TEXT ONLY')
                        if attr_type.data_type == SubjectAttribute.NUMBER:
                            if any([d['value_date'] is not None, d['value_text'] is not "",
                                    d['value_number'] is None]):
                                form.add_error('value_number', 'Please set NUMBER and NUMBER ONLY')
                        if attr_type.data_type == SubjectAttribute.DATE:
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


class PersonAdmin(admin.ModelAdmin):
    inlines = (SubjectAttributeInline,)
    
    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        if (obj.enterprise is not None):
            self.message_user(request, "Cannot delete: this person is tied to an enterprise " + str(obj.enterprise), level=messages.ERROR)
            return
        obj.delete()

    def has_delete_permission(self, request, obj=None):
        if (obj and obj.enterprise is not None):
            self.message_user(request, "This person is tied to an enterprise " + str(obj.enterprise) + " and therefore cannot be deleted", level=messages.WARNING)
            return False
        return True



class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        exclude = []


class EnterpriseAdmin(admin.ModelAdmin):
    inlines = (SubjectAttributeInline, )
    form = EnterpriseForm


class EmployeeAdmin(admin.ModelAdmin):
    inlines = (SubjectAttributeInline,)


admin.site.register(Address)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeRole)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(SubjectAttribute)
