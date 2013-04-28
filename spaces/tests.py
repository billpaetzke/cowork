from django.test import TestCase
from django.test.client import RequestFactory

from spaces.models import Space
from spaces.views import ListSpaceView


class SpaceTests(TestCase):
    """Space model tests."""
    
    def test_str(self):
        
        space = Space(name='WeWork Hollywood')

        self.assertEquals(str(space), 'WeWork Hollywood')

class SpaceListViewTests(TestCase):
    """Space list view tests."""

    def test_spaces_in_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = ListSpaceView.as_view()(request)

        self.assertEquals(list(response.context_data['object_list']), [])

        Space.objects.create(name='WeWork Hollywood')
        response = ListSpaceView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
