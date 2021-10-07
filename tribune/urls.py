from django.conf.urls import url,include
from django.contrib import admin

from news import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/',include('news.urls')),
]