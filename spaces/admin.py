from django.contrib import admin

from spaces.models import Space, PendingSpace

admin.site.register(Space)
admin.site.register(PendingSpace)
