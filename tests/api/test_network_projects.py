import pytest

from django.urls import reverse
from model_bakery import baker
from rest_framework import status

from hipeac.models import Permission
from .generic import UserMixin


@pytest.mark.django_db
class TestForAnonymous:
    list_url = reverse("v1:project-list")
    project = None

    @pytest.fixture(autouse=True)
    def setup_project(self, db):
        if not self.project:
            self.project = baker.make_recipe("hipeac.project")

    def get_detail_url(self, project_id):
        return reverse("v1:project-detail", args=[project_id])

    def test_list(self, api_client):
        assert api_client.get(self.list_url).status_code == status.HTTP_200_OK

    def test_create(self, api_client):
        assert api_client.post(self.list_url).status_code == status.HTTP_403_FORBIDDEN

    def test_read(self, api_client):
        assert api_client.get(self.get_detail_url(self.project.id)).status_code == status.HTTP_200_OK

    def test_update(self, api_client):
        detail_url = self.get_detail_url(self.project.id)
        assert api_client.patch(detail_url).status_code == status.HTTP_403_FORBIDDEN
        assert api_client.post(detail_url).status_code == status.HTTP_403_FORBIDDEN
        assert api_client.put(detail_url).status_code == status.HTTP_403_FORBIDDEN

    def test_delete(self, api_client):
        assert api_client.delete(self.get_detail_url(self.project.id)).status_code == status.HTTP_403_FORBIDDEN


class TestForAuthenticated(UserMixin, TestForAnonymous):
    def test_create(self, api_client):
        api_client.force_authenticate(user=self.user)
        assert api_client.post(self.list_url).status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_delete(self, api_client):
        api_client.force_authenticate(user=self.user)
        assert api_client.delete(self.get_detail_url(self.project.id)).status_code == status.HTTP_405_METHOD_NOT_ALLOWED


class TestForAdministrator(TestForAuthenticated):
    project = None
    user_admin = None

    @pytest.fixture(autouse=True)
    def setup_project(self, db):
        if not self.project:
            self.user_admin = baker.make_recipe("hipeac.user")
            self.project = baker.make_recipe("hipeac.project")
            Permission(content_object=self.project, user=self.user_admin, level=Permission.ADMIN).save()

    def test_update(self, api_client):
        api_client.force_authenticate(user=self.user_admin)
        detail_url = self.get_detail_url(self.project.id)
        assert api_client.patch(detail_url, {"name": "name"}).status_code == status.HTTP_200_OK
        assert api_client.post(detail_url).status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        # assert api_client.put(self.list_url, {'name': 'name'}).status_code == status.HTTP_202_ACCEPTED
