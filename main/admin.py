from django.contrib import admin
from .models import Account, Luggage, Luggage_Stage, Ticket

admin.site.register(Account)
admin.site.register(Luggage)
admin.site.register(Luggage_Stage)
admin.site.register(Ticket)