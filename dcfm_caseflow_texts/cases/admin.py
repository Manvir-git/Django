# Original path: cases/admin.py


from django.contrib import admin
from .models import Case, Party
class PartyInline(admin.TabularInline):
    model = Party
    extra = 0
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('number','case_type','category','priority_score','state','next_hearing_date')
    search_fields = ('number',)
    inlines = [PartyInline]
admin.site.register(Party)
