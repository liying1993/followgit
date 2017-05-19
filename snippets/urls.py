from django.conf.urls import url,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
#
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'products',views.ProductViewSet)
router.register(r'album',views.AlbumViewSet)
router.register(r'track',views.TrackViewSet)
router.register(r'account',views.AccountViewSet)
router.register(r'accountteam',views.AccountTeamViewSet)
# urlpatterns = [
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

#
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
# urlpatterns = format_suffix_patterns([
#     # url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^$', views.api_root),
#     url(r'^snippets/$',views.SnippetList.as_view(),name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view(),name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',views.SnippetHighlight.as_view(),name='snippet-highlight'),
#     url(r'^users/$',views.UserList.as_view(),name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name='user-detail'),
# ])

# Login and logout views for the browsable API
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)