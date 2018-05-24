# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import File, Info, version

# Register your models here.
admin.site.register(File)
admin.site.register(Info)
admin.site.register(version)