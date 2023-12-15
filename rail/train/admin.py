from django.contrib import admin
from .models import *

admin.site.register(Train)
admin.site.register(Station)
admin.site.register(TrainRoute)
admin.site.register(TrainStationRoute)
admin.site.register(Ticket)
admin.site.register(Customer)
admin.site.register(Payment)
