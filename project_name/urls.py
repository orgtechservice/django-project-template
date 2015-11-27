# -*- coding: utf-8 -*-

# Внимание! Это глобальный urls.py проекта. Добавлять свои URL-ки лучше в urls.py приложения «portal».

# Django
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

# Наш проект
from portal import urls as portal_urls

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^captcha/', include('captcha.urls')),
	url(r'', include(portal_urls)),

	# Чисто отладочная строка
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
