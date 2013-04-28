from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView

from spaces.models import PendingSpace, Space

class ListSpaceView(ListView):

    model = Space # list all spaces in the db
    template_name = 'space_list.html'

class CreateSpaceView(CreateView):

    model = PendingSpace
    template_name = 'edit_space.html'

    def get_success_url(self):
        return reverse('spaces-list')
