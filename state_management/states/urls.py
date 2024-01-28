from django.urls import path
from .views import StateListView, StateDetailView, StateCreateView, StateUpdateView, StateDeleteView

urlpatterns = [
    path('', StateListView.as_view(), name='state_list'),
    path('<int:pk>/', StateDetailView.as_view(), name='state_detail'),
    path('add/', StateCreateView.as_view(), name='state_add'),
    path('<int:pk>/edit/', StateUpdateView.as_view(), name='state_edit'),
    path('<int:pk>/delete/', StateDeleteView.as_view(), name='state_delete'),
]
