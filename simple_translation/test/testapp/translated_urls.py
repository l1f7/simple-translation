from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)

for langcode in dict(settings.LANGUAGES).keys():
	urlpatterns += url(r'^%s/' % langcode,
		include('simple_translation.test.testapp.urls',
		namespace=langcode, app_name='testapp')
	)