from django.contrib import admin
from .models import Project_Reports,Comment_Reports, Project

# Register your models here.
@admin.register(Project_Reports)
class Project_Reports_Admin(admin.ModelAdmin):
    list_display = (
        'report_id',
        'user',
        'project',
        'report',
        'project_actions',
    )
    readonly_fields = (
        'report_id',
        'user',
        'project',
        'report',
        'project_actions',
    )

# admin.site.register(Project)
@admin.register(Project)
class Project_Admin(admin.ModelAdmin):
    list_display = (
        'title',
        'total_target',
        'created_at',
        'creator',
        'is_featured'
    )
    readonly_fields = (
        'id',
        'title',
        'details',
        'total_target',
        'start_date',
        'end_date',
        'created_at',
        'creator',
        'category'
    )

    # def has_change_permission(self,request, obj=None):
    #     return True