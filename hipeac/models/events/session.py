from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from hipeac.models import Permission


def validate_date(date, event) -> None:
    if date < event.start_date or date > event.end_date:
        raise ValidationError('Date is not valid for this event.')


class Session(models.Model):
    event = models.ForeignKey('hipeac.Event', on_delete=models.CASCADE, related_name='sessions')
    is_private = models.BooleanField(default=False)

    date = models.DateField()
    start_at = models.TimeField(null=True, blank=True)
    end_at = models.TimeField(null=True, blank=True)
    title = models.CharField(max_length=250)
    summary = models.TextField(null=True, blank=True)

    max_attendees = models.PositiveSmallIntegerField(default=0, help_text='Leave on `0` for non limiting.')
    extra_attendees_fee = models.PositiveSmallIntegerField(default=0)

    application_areas = models.CharField(max_length=250, default='', validators=[validate_comma_separated_integer_list])
    topics = models.CharField(max_length=250, default='', validators=[validate_comma_separated_integer_list])
    acl = GenericRelation('hipeac.Permission')
    projects = models.ManyToManyField('hipeac.Project', related_name='sessions')
    links = GenericRelation('hipeac.Link')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['event', 'date']),
            # models.Index(fields=['conference', 'track']),
        ]
        ordering = ['date', 'start_at', 'end_at']

    def can_be_managed_by(self, user) -> bool:
        return self.acl.filter(user_id=user.id, level__gte=Permission.ADMIN).exists()

    def clean(self) -> None:
        validate_date(self.date, self.event)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('project', args=[self.id, self.slug])

    @property
    def slug(self) -> str:
        return slugify(self.title)
