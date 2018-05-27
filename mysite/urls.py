from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
]
