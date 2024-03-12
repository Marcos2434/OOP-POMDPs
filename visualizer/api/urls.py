from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiIndex, name="api-index"),
    path('createModel', views.createModel, name="create-model")
    # path('filter/<str:filter_>&<str:value>', views.apiFilter, name="api-filter"),
]