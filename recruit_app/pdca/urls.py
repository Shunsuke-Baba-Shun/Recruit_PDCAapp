from django.urls import path
from . import views

urlpatterns = [
    path('', views.PDCAIndexView, name='pdca-index'),
    path('pdca/', views.PDCAListView.as_view(), name='pdca-list'),
    path('pdca/<int:pk>/detail/', views.PDCADetailView.as_view(), name='pdca-detail'),
    path('pdca/create/', views.PDCACreateView.as_view(), name='pdca-create'),
    path('pdca/<int:pk>/delete/', views.PDCADeleteView.as_view(), name='pdca-delete'),
    path('pdca/<int:pk>/update/', views.PDCAUpdateView.as_view(), name='pdca-update'),
]