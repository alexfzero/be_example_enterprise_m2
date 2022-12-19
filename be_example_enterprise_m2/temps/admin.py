from django.contrib import admin
from .models import Position, Status, OperationType, Department

admin.site.register(Position)
admin.site.register(Status)
admin.site.register(OperationType)
admin.site.register(Department)
