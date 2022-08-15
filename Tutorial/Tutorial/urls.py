from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Hello.urls")),
    path('contact/',include("Hello.urls")),
    path('login/',include("Hello.urls")),
    path('signup/',include("Hello.urls")),
    path('logout/',include("Hello.urls")),
    path('profile/',include("Hello.urls")),
    path('edit_profile/',include("Hello.urls")),
    path('change_password/',include("Hello.urls")),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

admin.site.site_header = "Web Knowlege 4k"
admin.site.site_title = "Admin"
admin.site.index_title = "Admin Panel"
