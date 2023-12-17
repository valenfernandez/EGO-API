from rest_framework import routers
from cars_api import views
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

#endpoint for the api

router = routers.DefaultRouter()
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'features', views.FeatureViewSet)
router.register(r'concessionaires', views.ConcessionaireViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'accesories', views.AccesoryViewSet)
router.register(r'activities', views.ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='Ego API Documentation')),
    path('vehicles_summary/', views.VehicleSummaryViewSet.as_view(), name='vehicle-summary'),
    path('vehicles/<int:id>/add-feature/', views.AddFeatureToVehicleView.as_view(), 
    name='add-feature-to-vehicle'),
    path('vehicle_detail/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicle_features/<int:id>/', views.VehicleFeaturesViewSet.as_view(), name='vehicle-features'),
    path('vehicle_key_features/<int:id>/', views.VehicleKeyFeaturesViewSet.as_view(), name='vehicle-key-features'),
    path('request_test_drive/<int:id>/', views.RequestVehicleTestDriveView.as_view(), name='request-test-drive'),
    path('approve_test_drive/<int:id>/', views.ApproveTestDrive.as_view(), name='approve-test-drive'),
    path('test_drive_requests_list/', views.TestDriveRequests.as_view(), name='test-drive-requests-list'),
    path('make_review/<int:id>/', views.MakeReviewView.as_view(), name='make-review'),
    path('reviews_list/', views.VehicleReviewsView.as_view(), name='reviews-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
