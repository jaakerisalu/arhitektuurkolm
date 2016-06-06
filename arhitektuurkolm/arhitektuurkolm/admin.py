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

    ''' EXAMPLES
        def clean(self):
            cleaned_data = super().clean()

            if cleaned_data['start_hour'] >= cleaned_data['end_hour']:
                raise ValidationError('We currently do not support tarifs that span midnight.')

            return cleaned_data

        def save(self, commit=True):
            tarif = super().save(commit)

            tarif.weekdays_bits = 0
            for i in range(1, 8):
                is_active = self.cleaned_data.get('weekday_%d' % i, False)
                tarif.weekdays_bits += 2**i if is_active else 0

            return tarif

        ÜHE VÄLJA CLEAN MEETOD
        def clean_displayed_units(self):
            family = self.cleaned_data['family']
            if self.cleaned_data['displayed_units'] and self.cleaned_data['displayed_units'] not in Metric.UNIT_CHOICES and self.cleaned_data['type'] == MetricsTypes.RealTimeMetric:
                raise ValidationError("You cannot add a non-real time unit to a real time metric")
            elif self.cleaned_data['displayed_units'] and self.cleaned_data['displayed_units'] not in family.get_units() and self.cleaned_data['type'] != MetricsTypes.RealTimeMetric:
                raise ValidationError("There are no sensors with selected unit in the family. Please select one of %s" % family.get_units_display())
            return self.cleaned_data["displayed_units"]

        NSM LISA PARAMEETRID NTX
        filter_horizontal = ['add', 'subtract'] # Add ja Subtract on ManyToMany väljad mudeli küljes

        def sensors_to_add(self, obj):
            return ", ".join([x.name for x in obj.add.all()])

        def sensors_to_subtract(self, obj):
            return ", ".join([x.name for x in obj.subtract.all()])

        list_display = ('name', 'sensors_to_add', 'sensors_to_subtract', 'visible')
    '''

admin.site.register(Address)
admin.site.register(Employee)
admin.site.register(EmployeeRole)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Person)
admin.site.register(SubjectAttribute)
