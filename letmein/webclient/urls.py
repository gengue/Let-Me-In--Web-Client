from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('webclient.views',
	url(r'^$','index_view', name='vista_index'),
	url(r'^registro/$','registro_view', name='vista_registro'),
	)