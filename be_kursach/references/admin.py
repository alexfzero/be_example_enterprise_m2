from django.contrib import admin
from .models import Contract, FlowFunds, Storage, StorageOperation

admin.site.register(Contract)
admin.site.register(FlowFunds)
admin.site.register(Storage)
admin.site.register(StorageOperation)
