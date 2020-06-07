from django.urls import path
from . import views
from .views import PostListView,PostDetailView,SignUpView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns






urlpatterns = [

path('signup/', SignUpView.as_view(), name='signup'),
path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'), 
path('', PostListView.as_view(), name='home'),
path('profile/', views.profile, name='profile'),
path('update/profile', views.updateprofile, name='update'),
path('post/new/', views.post_new, name='post_new'),
path('search/', views.search_results, name='search_results'),
path('vote/(?P<post_id>\d+)?', views.vote, name='vote'), 


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    