from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *


admin.site.register(QualityStandard)
admin.site.register(QualityInspection)
admin.site.register(QualityResult)
admin.site.register(QualityGrade)