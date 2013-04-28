from django.conf import settings # for getting settings vars
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, DetailView

from spaces.models import PendingSpace, Space

class ListSpaceView(ListView):

    model = Space # list all spaces in the db
    template_name = 'space_list.html'

class CreateSpaceView(CreateView):

    model = PendingSpace
    template_name = 'edit_space.html'

    def get_success_url(self):
        return reverse('spaces-list')

class SpaceView(DetailView):

    model = Space
    template_name = 'space.html'

    def get_context_data(self, **kwargs):

        context = super(SpaceView, self).get_context_data(**kwargs)
        context['gmaps_key'] = settings.GOOGLE_MAPS_API_KEY

        return context
