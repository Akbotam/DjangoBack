from django.contrib import admin
from api.models import Company, Review, Reviewer

admin.site.register(Reviewer)
admin.site.register(Review)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', )
