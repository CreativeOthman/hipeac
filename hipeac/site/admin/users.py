from django.contrib import admin
from django.forms import ModelForm

from hipeac.forms import ApplicationAreasChoiceField, TopicsChoiceField, MembershipTagsChoiceField
from hipeac.models import Profile
from .generic import HideDeleteActionMixin


class ProfileAdminForm(ModelForm):
    application_areas = ApplicationAreasChoiceField(required=False)
    topics = TopicsChoiceField(required=False)
    membership_tags = MembershipTagsChoiceField(required=False)


@admin.register(Profile)
class ProfileAdmin(HideDeleteActionMixin, admin.ModelAdmin):
    form = ProfileAdminForm
    exclude = ('is_bouncing',)

    list_display = ('user_id', 'username', 'name', 'email', 'membership_tags')

    autocomplete_fields = ('institution', 'second_institution', 'projects')
    readonly_fields = ('user',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    fieldsets = (
        (None, {
            'fields': ('user', 'country', 'bio', 'meal_preference'),
        }),
        ('AFFILIATION', {
            'fields': ('position', 'institution', 'department', 'second_institution'),
        }),
        ('MEMBERSHIP', {
            'fields': (('membership_date', 'membership_revocation_date'), 'advisor', 'membership_tags'),
        }),
        ('METADATA', {
            'classes': ('collapse',),
            'fields': ('application_areas', 'topics'),
        }),
        ('PRIVACY', {
            'classes': ('collapse',),
            'fields': ('is_subscribed', 'is_public'),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')

    def email(self, obj) -> str:
        return obj.user.email
