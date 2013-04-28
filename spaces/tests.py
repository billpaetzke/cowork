from django.test import TestCase

from spaces.models import Space


class SpaceTests(TestCase):
    """Space model tests."""
    
    def test_str(self):
        
        space = Space(name='WeWork Hollywood')

        self.assertEquals(str(space), 'WeWork Hollywood')
