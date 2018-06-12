from django.conf.urls import url
from localnegocio import views

urlpatterns = [
    url(r'^localnegocio/$', views.localnegocio_list),
    url(r'^localnegocio/(?P<pk>[0-9]+)/$', views.localnegocio_detail),
    url(r'^productos/', views.productos_list),
    url(r'^buscarproducto/(?P<nomproducto>\w+)/$', views.buscarproducto),
    url(r'^login/(?P<username>\w+)/(?P<password>\w+)/$', views.login),
    url(r'^user/register/$', views.register),
    url(r'^user/update/(?P<pk>[0-9]+)/$', views.login_update),
    url(r'^valid/(?P<username>\w+)/$', views.valid),
    url(r'^item/(?P<nomprod>\w+)/$', views.item),
    url(r'^listitem/$', views.listitem),
]