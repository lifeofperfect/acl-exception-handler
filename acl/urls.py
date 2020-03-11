from django.urls import path
from .views import alertUnreactedView, alertPending, alertClosed_user,alertClosed_staff, acl_update, registerPage, loginPage, logoutUser
from django.contrib.auth import views as auth_views 
from . import views


urlpatterns = [
    path('search/', views.SearchListView.as_view(), name='search'),
    path('<int:id>/false', views.falseUpdate, name='falseUpdate'),
    path('<int:id>/true', views.truePositive, name='trueUpdate'),
    path('', alertUnreactedView, name='unreacted'),
    path('register/', registerPage, name='register'),
    path('login1/', loginPage, name='login1'),
    path('logout/', logoutUser, name='logout'),
    #path('api/update/<str:pk>/', views.ApiTrueUpdate, name='trueUpdate'),
    path('pending/', alertPending, name='pending'),
    path('regularised/', alertClosed_user, name='regularised'),
    path('regularised-staff/', alertClosed_staff, name='regularised_staff'),
    path('<int:id>/update', acl_update, name='response'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]