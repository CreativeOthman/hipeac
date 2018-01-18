from rest_framework.routers import DefaultRouter

from hipeac.api import views


class Router(DefaultRouter):
    def __init__(self, version='v1'):
        super().__init__()

        self.schema_title = 'HiPEAC API {0}'.format(version)

        self.register(r'events/events', views.EventViewSet, base_name='event')
        self.register(r'events/sessions', views.SessionViewSet, base_name='session')
        self.register(r'jobs', views.JobViewSet, base_name='job')
        self.register(r'press/clippings', views.ClippingViewSet, base_name='clipping')
        self.register(r'press/quotes', views.QuoteViewSet, base_name='quote')
        # self.register(r'press/releases', views.QuoteViewSet, base_name='press_release')
        # self.register(r'press/videos', views.QuoteViewSet, base_name='video')
        self.register(r'metadata', views.MetadataViewSet, base_name='metadata')
        self.register(r'network/institutions', views.InstitutionViewSet, base_name='institution')
        self.register(r'network/members', views.MemberViewSet, base_name='member')
        self.register(r'network/projects', views.ProjectViewSet, base_name='project')
        # self.register(r'news', views.QuoteViewSet, base_name='post')
        self.register(r'users', views.UserViewSet, base_name='user')
        self.register(r'vision', views.VisionViewSet, base_name='vision')
