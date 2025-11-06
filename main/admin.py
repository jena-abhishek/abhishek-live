from django.contrib import admin
from .models import Profile, Skill, SkillTag, Education, Project, ProjectTag, Contact


# ---------- PROFILE ----------
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'email')
    search_fields = ('name', 'email')


# ---------- SKILLS ----------
@admin.register(SkillTag)
class SkillTagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type', 'proficiency', 'is_featured')
    list_filter = ('skill_type', 'is_featured')
    search_fields = ('name', 'description')
    filter_horizontal = ('tags',)


admin.site.register(Skill, SkillAdmin)


# ---------- EDUCATION ----------
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current',)
    search_fields = ('degree', 'institution')


# ---------- PROJECTS ----------
@admin.register(ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description', 'technologies')
    filter_horizontal = ('tags',)


# ---------- CONTACT ----------
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)
