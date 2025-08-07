from django.contrib import admin
from django.urls import path
from user.views import *
from business.views import *
from event.views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('afghan/user', UserView)
router.register(r'afghan/business',BusinessViewSet )
router.register('afghan/category', CategoryViewSet)
router.register('afghan/province', ProvinceViewSet)
router.register('afghan/event', EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/auth/login/', CustomTokenView.as_view()),
    path('user/auth/refresh/', TokenRefreshView.as_view()),
    path('user/profile/', UserProfileView.as_view()),  

]

urlpatterns += router.urls
