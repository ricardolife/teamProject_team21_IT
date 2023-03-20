from django.contrib import admin
from rater.models import UserProfile,Book,Review
# Register your models here.

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(UserProfile)

