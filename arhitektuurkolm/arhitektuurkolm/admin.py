from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import messages

from .models import *


class SubjectAttributeInline(GenericTabularInline):
    model = SubjectAttributeValue
    ct_field = 'owner_type'
    ct_fk_field = 'owner_fk'
    extra = 1

class EnterpriseAdmin(admin.ModelAdmin):
    inlines = (SubjectAttributeInline, )

class PersonAdmin(admin.ModelAdmin):
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
    
    
admin.site.register(Address)
admin.site.register(Employee)
admin.site.register(EmployeeRole)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(SubjectAttribute)
