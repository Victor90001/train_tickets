from django.contrib import admin
from .models import *

admin.site.register(Train)
admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Ticket)
admin.site.register(Customer)
admin.site.register(Payment)
