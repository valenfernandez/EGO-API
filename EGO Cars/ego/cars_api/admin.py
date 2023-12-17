from django.contrib import admin
from .models import Vehicle, Feature, Review, Concessionaire, TestDrivePetition, Service, Accesory, Activity

# Register your models here.

admin.site.register(Vehicle)
admin.site.register(Feature)
admin.site.register(Review)
admin.site.register(Concessionaire)
admin.site.register(TestDrivePetition)
admin.site.register(Service)
admin.site.register(Accesory)
admin.site.register(Activity)
