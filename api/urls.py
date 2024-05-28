from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(basename='notes',
                viewset=views.NoteViewSet,
                prefix='notes')
router.register(basename='users',
                viewset=views.UserViewSet,
                prefix='users')

urlpatterns = router.urls