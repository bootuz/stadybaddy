from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('edit-profile/', user_views.edit_profile, name='edit_profile'),
    path('activate/<slug:uidb64>/<slug:token>/', user_views.activate, name='activate'),
    path('change-password/', user_views.change_password, name='change_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'),
         name='password-reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/reset_password_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<slug:uidb64>/<slug:token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/reset_password_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/reset_password_complete.html'),
         name='password_reset_complete')
]
