from django.contrib import admin
from accounts.admin import CustomUserAdmin as BaseUserAdmin
from accounts.models import User

from .models import *

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserAccountInline(admin.StackedInline):
    model = UserAccount
    can_delete = False
    verbose_name_plural = 'useraccount'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserAccountInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Address)
admin.site.register(AddressType)
admin.site.register(ContactType)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(EmployeeRole)
admin.site.register(EmployeeRoleType)
admin.site.register(EntPerRelationType)
admin.site.register(Enterprise)
admin.site.register(EnterprisePersonRelation)
admin.site.register(Person)
admin.site.register(StructUnit)
admin.site.register(SubjectAttribute)
admin.site.register(SubjectAttributeType)
admin.site.register(SubjectType)