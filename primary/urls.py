from rest_framework_nested  import routers
from . import views
from django.urls import path,include


router=routers.DefaultRouter()
router.register('post',views.PostViewset,basename='post')
router.register('me-post',views.UserPostViewset,basename='me_post')


post_router=routers.NestedDefaultRouter(router,'post',lookup='post')
post_router.register('images',views.PostImageViewSet,basename='post_image')
post_router.register('reviews',views.ReviewViewSet,basename='post_review')

user_post_router=routers.NestedDefaultRouter(router,'me-post',lookup='post')
user_post_router.register('images',views.PostImageViewSet,basename='user_post_image')
user_post_router.register('reviews',views.ReviewViewSet,basename='user_post_review')

reply_router=routers.NestedDefaultRouter(post_router,'reviews',lookup='review_reply')
reply_router.register('reply',views.ReplyViewSet, basename='reply')

user_reply_router=routers.NestedDefaultRouter(user_post_router,'reviews',lookup='review_reply')
user_reply_router.register('reply',views.ReplyViewSet, basename='reply')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(post_router.urls)),
    path('', include(user_post_router.urls)),
    path('', include(reply_router.urls)),
    path('', include(user_reply_router.urls)),
]

# urlpatterns = router.urls+post_router.urls+user_post_routers.urls
