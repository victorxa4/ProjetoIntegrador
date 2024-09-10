from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    # auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #

    path('account/', Account_View.as_view(), name='account'),
    path('account/<int:pk>/', Account_RetrieveUpdateDestroy_View.as_view(), name='single_account'),

    path('luggage/', Luggage_View.as_view(), name='luggage'),
    path('luggage/<uuid:pk>/', Luggage_RetrieveUpdateDestroy_View.as_view(), name='single_luggage'),

    path('luggage_stage/', Luggage_Stage_View.as_view(), name='luggage_stage'),
    path('luggage_stage/<uuid:pk>/', Luggage_Stage_RetrieveUpdateDestroy_View.as_view(), name='single_luggage_stage'),


]
