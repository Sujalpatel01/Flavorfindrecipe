from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Role)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(UserDetail)
admin.site.register(UserAddress)
admin.site.register(GadgetCategory)
admin.site.register(FeedbackDetails)
admin.site.register(ComplaintDetails)
