from django.urls import path
from .views import LinkListView, profile_view, LinkDeleteView,LinkCreateView, LinkUpdateView

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('add/', LinkCreateView.as_view(), name='list-create'),
    path('update/<int:pk>/', LinkUpdateView.as_view(), name='list-update'),
    path('delete/<int:pk>/', LinkDeleteView.as_view(), name='list-delete'),
    path('<slug:profile_slug>/', profile_view, name="profile"),

]