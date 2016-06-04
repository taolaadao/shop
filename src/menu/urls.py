from django.conf.urls import url
from django.contrib import admin
from .views import  (
	
	product_list,
	detail,
	edit,
	delete,
	create,
)

urlpatterns = [
	url(r'^$', product_list,name='list'),
	url(r'^detail/(?P<id>\d+)/$',detail, name='detail'),
    url(r'^$', product_list),
    
    url(r'^create$', create),
    url(r'^$edit', edit),
    url(r'^$delete', delete),
    
]