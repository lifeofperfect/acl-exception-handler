from django.urls import path
from .views import create_alert, branch_unreact, branch_alertPending, branch_alertClosed_user

urlpatterns = [
    path('branch_create/', create_alert, name='branch_create'),

    path('branch_list', branch_unreact, name='branch_unreact'),
    path('branch_pending', branch_alertPending, name='branch_pending'),
    path('branch_closed', branch_alertClosed_user, name='branch_closed'),

]
