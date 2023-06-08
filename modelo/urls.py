
from modelo import views
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^direccion$',views.listApi),
    url(r'^direccion/([0-9]+)$',views.listApi)

]
