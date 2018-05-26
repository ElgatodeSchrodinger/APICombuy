from django.conf.urls import url
from localnegocio import views

urlpatterns = [
    url(r'^localnegocio/$', views.localnegocio_list),
    url(r'^localnegocio/(?P<pk>[0-9]+)/$', views.localnegocio_detail),
    url(r'^productoslocal/', views.localproductos_list),
]