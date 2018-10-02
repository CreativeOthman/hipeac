from django_countries.serializer_fields import CountryField
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from hipeac.models import Event, Registration, Poster, Roadshow, Session, Project
from .generic import LinkSerializer, MetadataListField
from .institutions import InstitutionNestedSerializer
from .users import UserPublicListSerializer


class PosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poster
        fields = ('id', 'title', 'authors', 'type')


class RegistrationListSerializer(serializers.ModelSerializer):
    user = UserPublicListSerializer()

    class Meta:
        model = Registration
        fields = ('created_at', 'user')


class AuthRegistrationSerializer(WritableNestedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='v1:auth-registration-detail', read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    posters = PosterSerializer(many=True)

    class Meta:
        model = Registration
        exclude = ('user',)
        write_only_fields = ('event',)
        read_only_fields = ('fee', 'saldo', 'invoice_sent', 'visa_sent')


class SessionNestedSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='v1:session-detail', read_only=True)
    href = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Session
        exclude = ('summary', 'max_attendees', 'extra_attendees_fee', 'created_at', 'updated_at')


class SessionListSerializer(SessionNestedSerializer):
    application_areas = MetadataListField()
    topics = MetadataListField()


class SessionSerializer(SessionListSerializer):
    event = serializers.HyperlinkedIdentityField(view_name='v1:event-detail', read_only=True)
    date = serializers.DateField(read_only=True)
    projects = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), many=True, allow_null=True)
    editor_href = serializers.CharField(source='get_editor_url', read_only=True)

    class Meta(SessionNestedSerializer.Meta):
        exclude = ('created_at', 'updated_at')


class EventNestedSerializer(serializers.ModelSerializer):
    coordinating_institution = InstitutionNestedSerializer()
    country = CountryField(country_dict=True)
    url = serializers.HyperlinkedIdentityField(view_name='v1:event-detail', read_only=True)
    url_articles = serializers.HyperlinkedIdentityField(view_name='v1:event-articles')
    url_registrations = serializers.HyperlinkedIdentityField(view_name='v1:event-registrations')
    href = serializers.CharField(source='get_absolute_url', read_only=True)
    name = serializers.CharField(read_only=True)
    links = LinkSerializer(many=True)
    images = serializers.DictField(read_only=True)

    class Meta:
        model = Event
        exclude = ()


class EventListSerializer(EventNestedSerializer):
    pass


class EventSerializer(EventNestedSerializer):
    sessions = SessionListSerializer(many=True)


class RoadshowNestedSerializer(serializers.ModelSerializer):
    country = CountryField(country_dict=True)
    institutions = InstitutionNestedSerializer(many=True)
    href = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Roadshow
        exclude = ()


class RoadshowListSerializer(RoadshowNestedSerializer):
    pass


class RoadshowSerializer(RoadshowNestedSerializer):
    pass
