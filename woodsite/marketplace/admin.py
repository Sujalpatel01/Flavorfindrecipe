from django.contrib import admin
from .models import *

admin.site.register(Role)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(UserDetail)
admin.site.register(UserAddress)
admin.site.register(FurnitureCategory)
admin.site.register(FeedbackDetails)
admin.site.register(ComplaintDetails)

admin.site.register(Brand)
admin.site.register(NewFurniture)
admin.site.register(OldFurniture)
admin.site.register(RentFurniture)
admin.site.register(NewFurnitureBuying)
admin.site.register(OldFurnitureBuying)
admin.site.register(RentFurnitureOrder)