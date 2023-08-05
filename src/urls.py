from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from django.views.generic.base import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from bhealthapp.views import UserCreate, LabView, LabListView, LabServiceListView, ResultListView, \
    UpcomingAppointmentsLabView, UpcomingAppointmentsUserView, PastAppointmentsLabView, \
    PastAppointmentsUserView, ProfileView, PatientsView, ResultView, RequestsView, LabAddView, \
    LabRemoveView, UserLogin, LabCreate, RatingAddView, ResultAddView, UserUpdateView, LabUpdateView, \
    AppointmentAddView, AppointmentView, NotificationListView, AppointmentUpdateView, NotificationConfirmView, \
    AppointmentCancelView, DownloadResult, CanceledAppointmentsView, WeRecommendView

schema_view = get_schema_view(
    openapi.Info(title="Pastebin API", default_version='v1'),
    public=True,
)

router = DefaultRouter()

urlpatterns = [
                  # admin panel
                  path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
                  path('admin/', admin.site.urls),
                  url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
                  # summernote editor
                  path('summernote/', include('django_summernote.urls')),
                  # api
                  url(r'api/v1/register_user', UserCreate.as_view(), name='account_create'),
                  url(r'api/v1/register_lab', LabCreate.as_view(), name='lab_account_create'),
                  url(r'api/v1/login', UserLogin.as_view(), name='login'),
                  url(r'^api/v1/labs', LabListView.as_view(), name='labs'),
                  url(r'^api/v1/notifications', NotificationListView.as_view(), name='notifications'),
                  url(r'^api/v1/confirm_notification', NotificationConfirmView.as_view(), name='confirm_notification'),
                  url(r'^api/v1/lab_services', LabServiceListView.as_view(), name='lab_services'),
                  url(r'^api/v1/edit_profile_user', UserUpdateView.as_view(), name='edit_profile_user'),
                  url(r'^api/v1/edit_profile_lab', LabUpdateView.as_view(), name='edit_profile_lab'),
                  url(r'^api/v1/add_appointment', AppointmentAddView.as_view(), name='add_appointment'),
                  url(r'^api/v1/update_appointment', AppointmentUpdateView.as_view(), name='update_appointment'),
                  url(r'^api/v1/cancel_appointment', AppointmentCancelView.as_view(), name='cancel_appointment'),
                  url(r'^api/v1/results', ResultListView.as_view(), name='results'),
                  url(r'^api/v1/download_result', DownloadResult.as_view(), name='download_result'),
                  url(r'^api/v1/appointment', AppointmentView.as_view(), name='get_appointment'),
                  url(r'^api/v1/canceled_appointments', CanceledAppointmentsView.as_view(), name='canceled_appointments'),
                  url(r'^api/v1/upcoming_appointments', UpcomingAppointmentsUserView.as_view(),
                      name='user_upcoming_appointments'),
                  url(r'^api/v1/past_appointments', PastAppointmentsUserView.as_view(), name='user_past_appointments'),
                  url(r'^api/v1/u_appointments', UpcomingAppointmentsLabView.as_view(),
                      name='lab_upcoming_appointments'),
                  url(r'^api/v1/p_appointments', PastAppointmentsLabView.as_view(),
                      name='lab_past_appointments'),
                  url(r'^api/v1/requests', RequestsView.as_view(), name='requests'),
                  url(r'^api/v1/patients', PatientsView.as_view(), name='patients'),
                  url('api/v1/lab', LabView.as_view(), name='get_lab'),
                  url(r'^api/v1/add_lab', LabAddView.as_view(), name='add_lab'),
                  url(r'^api/v1/remove_lab', LabRemoveView.as_view(), name='remove_lab'),
                  url('api/v1/we_recommend', WeRecommendView.as_view(), name='top_labs'),
                  url('api/v1/result', ResultView.as_view(), name='get_result'),
                  url('api/v1/profile', ProfileView.as_view(), name='get_profile'),
                  url('api/v1/add_rating', RatingAddView.as_view(), name='add_rating'),
                  url('api/v1/add_result', ResultAddView.as_view(), name='add_result'),
                  url(r'^api/v1/password_reset/',
                      include('django_rest_passwordreset.urls', namespace='password_reset')),
                  # auth
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  # social login
                  url('', include('social_django.urls', namespace='social')),

                  # swagger docs
                  url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                      name='schema-json'),
                  url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  url(r'^health/', include('health_check.urls')),
                  # the 'api-root' from django rest-frameworks default router
                  re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
