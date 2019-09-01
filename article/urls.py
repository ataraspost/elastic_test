from rest_framework.routers import SimpleRouter

from article import views


app_name = 'articles'

router = SimpleRouter()
router.register(
    prefix=r'',
    base_name='articles',
    viewset=views.ArticleViewSet
)
urlpatterns = router.urls