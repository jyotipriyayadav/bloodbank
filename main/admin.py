from django.contrib import admin

from .models import Register,BloodDonation,BloodRequest

admin.site.register(Register)

admin.site.register(BloodDonation)

admin.site.register(BloodRequest)