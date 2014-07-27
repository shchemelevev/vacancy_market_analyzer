from django.contrib import admin
from vacancy.models import Vacancy

class VacancyAdmin(admin.ModelAdmin):
    list_display = ['url', 'title']

admin.site.register(Vacancy, VacancyAdmin)
