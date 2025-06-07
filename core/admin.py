from django.contrib import admin
from .models import AboutPageContent, TeamMember, ContactMessage # Import your models

@admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the AboutPageContent model.
    Ensures only one instance can be created.
    """
    list_display = (
        'page_title',
        'mission_title',
        'vision_title',
        'value1_title',
        'value2_title',
        'value3_title',
    )
    fieldsets = (
        (None, {
            'fields': ('page_title', 'page_description'),
        }),
        ('Misyon Bilgileri', {
            'fields': ('mission_title', 'mission_text'),
        }),
        ('Vizyon Bilgileri', {
            'fields': ('vision_title', 'vision_text'),
        }),
        ('Değerlerimiz', {
            'fields': (
                ('value1_icon', 'value1_title'),
                'value1_description',
                ('value2_icon', 'value2_title'),
                'value2_description',
                ('value3_icon', 'value3_title'),
                'value3_description',
            ),
        }),
    )

    # Restrict to only one instance of AboutPageContent
    def has_add_permission(self, request):
        """Prevents adding more than one AboutPageContent object."""
        return not AboutPageContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevents deleting the single AboutPageContent object."""
        return False # Or set to True if you want to allow deletion

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    """
    Admin configuration for the TeamMember model.
    """
    list_display = ('name', 'title', 'profile_picture_preview')
    search_fields = ('name', 'title', 'description')
    list_filter = ('title',)
    readonly_fields = ('profile_picture_preview',)

    def profile_picture_preview(self, obj):
        """Displays a preview of the profile picture in the admin list."""
        if obj.profile_picture:
            return f'<img src="{obj.profile_picture.url}" style="max-height: 50px; max-width: 50px; border-radius: 50%;" />'
        return '(Resim Yok)'
    profile_picture_preview.allow_tags = True
    profile_picture_preview.short_description = 'Profil Resmi'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ContactMessage model.
    """
    list_display = ('subject', 'name', 'email', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'sent_at') # Messages are read-only in admin

    def has_add_permission(self, request):
        """Contact messages are added via form, not directly in admin."""
        return False