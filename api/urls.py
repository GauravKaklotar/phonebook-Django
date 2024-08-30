from django.urls import path
from . import views
from .views import CustomAuthToken

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', CustomAuthToken.as_view(), name='login'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('contacts', views.ContactListView.as_view(), name='contacts'),
    path('contacts/<int:pk>', views.ContactDetailView.as_view(), name='contact-detail'),
    path('spam', views.SpamView.as_view(), name='spam'),
    path('search', views.SearchView.as_view(), name='search'),
]
