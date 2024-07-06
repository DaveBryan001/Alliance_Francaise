from django.urls import path, include
from django.contrib.auth import views as auth_views
# from .views import register, home
from .views import CourseViewSet, EventViewSet, ResourceViewSet
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, EventViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterAPI, SearchAPIView


router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'events', EventViewSet)
router.register(r'resources', ResourceViewSet)

urlpatterns = [
    path('api/search/', SearchAPIView.as_view(), name='search_results'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    # path('course-autocomplete/', CourseAutocomplete.as_view(), name='course-autocomplete'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', RegisterAPI.as_view(), name='register'),
    path('api/auth/', include('dj_rest_auth.urls')),

]
