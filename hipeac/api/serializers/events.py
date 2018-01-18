from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from hipeac.models import Event, Session
from .generic import MetadataListField
from .institutions import InstitutionRelatedField
from .projects import ProjectRelatedField


class SessionNestedSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='v1:session-detail', read_only=True)
    href = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Session
        exclude = ['created_at', 'updated_at', 'summary']


class SessionListSerializer(SessionNestedSerializer):
    application_areas = MetadataListField()
    topics = MetadataListField()


class EventNestedSerializer(serializers.ModelSerializer):
    coordinating_institution = InstitutionRelatedField()
    country = CountryField(country_dict=True)
    url = serializers.HyperlinkedIdentityField(view_name='v1:event-detail', read_only=True)
    href = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Event
        exclude = ()


class EventListSerializer(EventNestedSerializer):
    pass


class EventSerializer(EventNestedSerializer):
    sessions = SessionListSerializer(many=True)


class SessionSerializer(SessionListSerializer):
    event = EventNestedSerializer()
    projects = ProjectRelatedField(many=True)

    class Meta(SessionNestedSerializer.Meta):
        exclude = ['created_at', 'updated_at']
