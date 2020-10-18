from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^profile/add$', views.new_profile, name='new-profile'),
    url(r'^new/post$',views.home, name='newpost'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^user-profile/(\d+)',views.profile,name='user-profile'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)