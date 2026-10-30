from products.viewsets import ProductViewSets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product-abc',ProductViewSets,basename="products")
print(router.urls)

urlpatterns = router.urls