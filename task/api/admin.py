from django.contrib import admin
from api.models import Company, Review, Reviewer

admin.site.register(Company)
admin.site.register(Reviewer)
admin.site.register(Review)
