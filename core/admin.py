from django.contrib import admin

from core.models.auth import *
from core.models.cars import *
from core.models.monitoring import *


admin.site.register(User)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Arenda)
admin.site.register(Card)
admin.site.register(Monitoring)
admin.site.register(Car)