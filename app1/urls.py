from django.urls import path, include
from app1.views import *
from rest_framework.routers import DefaultRouter

router1=DefaultRouter()
router1.register('snippetgenericviewset',SnippetModelViewSet,
                basename='snippetgenericviewset')
router2=DefaultRouter()
router2.register('snippetmodelviewset',SnippetViewSet,
                basename='snippetmodelviewset')
router3=DefaultRouter()
router3.register('snippetgenericview',GenericSnippetView,
                basename='snippetgenericview')
router4=DefaultRouter()
router4.register('snippetclassview',SnippetView,
                basename='snippetclassview')

router5=DefaultRouter()
router5.register('SnippetView',SnippetView.as_view(),
                basename='SnippetView')




urlpatterns = [

path('',include(router1.urls)),
# path('',include(router2.urls)),
# path('',include(router3.urls)),
# path('',include(router4.urls)),
# path('SnippetView/',include(router5.urls)),

# path('<int:pk>/', views.snippet_list, name='snippet_list'),
# path('',SnippetView.as_view()),
# path('detail_view/<int:id>/',SnippetDetialView.as_view()),
# path('generic_view/<int:id>/',GenericSnippetView.as_view()),
# path('<int:pk>/',SnippetView.as_view()),
]
