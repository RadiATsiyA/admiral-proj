from django.contrib import admin

from .models import ObjectAd, ObjectImage, ObjectFeedback, ApplicationToView, Category

# Register your models here.
admin.site.register(ObjectAd)
admin.site.register(ObjectImage)
admin.site.register(ObjectFeedback)
admin.site.register(ApplicationToView)
admin.site.register(Category)
