# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.contrib.auth import views
from django.urls import path
from .views import (
    ArticleListView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView
)

app_name = 'account'
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    # path("password_change/done/",views.PasswordChangeDoneView.as_view(),name="password_change_done",),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done",),
    # path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm",),
    # path("reset/done/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete",),
]

urlpatterns += [
    path("", ArticleListView.as_view(), name='home'),
    path('blog/create/', ArticleCreateView.as_view(), name='blog-create'),
    path('blog/update/<int:pk>', ArticleUpdateView.as_view(), name='blog-update'),
    path('blog/delete/<int:pk>', ArticleDeleteView.as_view(), name='blog-delete'),

]
