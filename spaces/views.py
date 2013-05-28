from django.conf import settings # for getting settings vars
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, DetailView

from spaces.models import PendingSpace, Space

import urllib, urllib2, json # lat, lng
from django.utils.encoding import smart_str # lat, lng

import math # to calculate bounding box for a given latlng

class ListSpaceView(ListView):

    template_name = 'space_list.html'

    def get_queryset(self):
        loc =  self.request.GET.get('q')
        lat, lng =  get_lat_lng(loc)
        radius_km = 32.19
        lng_max, lng_min, lat_max, lat_min = bounding_box(lat, lng, radius_km)
        spaces = Space.objects.filter(
            lat__lte=lat_max,
            lat__gte=lat_min,
            lon__lte=lng_max,
            lon__gte=lng_min
        )
        return spaces

    def get_context_data(self, **kwargs):

        context = super(ListSpaceView, self).get_context_data(**kwargs)
        context['loc'] = self.request.GET.get('q')

        return context

class CreateSpaceView(CreateView):

    model = PendingSpace
    template_name = 'edit_space.html'

    def get_success_url(self):
        return reverse('spaces-home')

class SpaceView(DetailView):

    model = Space
    template_name = 'space.html'

    def get_context_data(self, **kwargs):

        context = super(SpaceView, self).get_context_data(**kwargs)
        context['gmaps_key'] = settings.GOOGLE_MAPS_API_KEY

        return context

class HomeView(ListView):

    model = Space # to do: list top ten cities
    template_name = 'home.html'


def get_lat_lng(location):
    
    # https://gist.github.com/mhulse/1027898
    # http://djangosnippets.org/snippets/293/
    # http://code.google.com/p/gmaps-samples/source/browse/trunk/geocoder/python/SimpleParser.py?r=2476
    # http://stackoverflow.com/questions/2846321/best-and-simple-way-to-handle-json-in-django
    # http://djangosnippets.org/snippets/2399/
    
    location = urllib.quote_plus(smart_str(location))
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
    response = urllib2.urlopen(url).read() 
    result = json.loads(response)
    if result['status'] == 'OK':
       lat = result['results'][0]['geometry']['location']['lat']
       lng = result['results'][0]['geometry']['location']['lng']
       return (lat, lng)
    else:
        return (0.0, 0.0)

#####
#http://stackoverflow.com/questions/15214992/it-is-necessary-to-use-geodjango-to-query-distances-in-django
#####

# earth_radius = 3960.0  # for miles
earth_radius = 6371.0  # for kms
degrees_to_radians = math.pi/180.0
radians_to_degrees = 180.0/math.pi

def change_in_latitude(distance):
    "Given a distance north, return the change in latitude."
    return (distance/earth_radius)*radians_to_degrees

def change_in_longitude(latitude, distance):
    "Given a latitude and a distance west, return the change in longitude."
    # Find the radius of a circle around the earth at given latitude.
    r = earth_radius*math.cos(latitude*degrees_to_radians)
    return (distance/r)*radians_to_degrees

def bounding_box(latitude, longitude, distance):
    lat_change = change_in_latitude(distance)
    lat_max = latitude + lat_change
    lat_min = latitude - lat_change
    lon_change = change_in_longitude(latitude, distance)
    lon_max = longitude + lon_change
    lon_min = longitude - lon_change
    return (lon_max, lon_min, lat_max, lat_min)
