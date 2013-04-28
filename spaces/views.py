from django.views.generic import ListView

from spaces.models import Space

class ListSpaceView(ListView):

    model = Space # list all spaces in the db
    template_name = 'space_list.html'
