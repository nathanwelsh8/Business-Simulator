from django.contrib import admin
from .models import *


# Register your models here.
# If app not registered then
# it will not appear on the
# back of site admin panel!

admin.site.register(YES)
admin.site.register(School)
admin.site.register(Team)