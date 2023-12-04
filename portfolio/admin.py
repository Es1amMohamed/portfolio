from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class BlogSummernote(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = "__all__"


admin.site.register(Portfolio)
admin.site.register(Skills)
admin.site.register(Tools)
admin.site.register(Projects, BlogSummernote)
admin.site.register(Blogs, BlogSummernote)
admin.site.register(Colleagues)
admin.site.register(Category)
admin.site.register(Courses, BlogSummernote)
admin.site.register(Contact)
admin.site.register(AboutMe)
admin.site.register(ProjectsImages)
