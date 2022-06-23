
from django.contrib import admin
from django.urls import path
from organization.views import home, about, blog, blog_detail,contactus,service
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home_url"),
    path('about/', about, name="about_url"),
    path('blog/', blog, name="blog_url"),
    path('blog-s/<int:id>/', blog_detail, name="blog_detail_url"),
    path('contact/',contactus, name="contact_url"),
    path('service/',service, name="service_url")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
