from django.urls import path, include
from app1.views import *
from rest_framework.routers import DefaultRouter

router1=DefaultRouter() #SimpleRouter() not for json
router1.register('snippetmodelviewset',SnippetModelViewSet,
                basename='snippetmodelviewset')

router1.register('snippetgenericviewset',SnippetViewSet,
                basename='snippetgenericviewset')

#only viewset class working with routers
# we don't need multiple routers instance
#add all class to single routers instance,
# specific class  can call by using basename

print("all urls",router1.urls)

# router3=DefaultRouter()
# router1.register('snippetgenericview',GenericSnippetView,
#                 basename='snippetgenericview')
# router4=DefaultRouter()
# router4.register('snippetclassview',SnippetView,
#                 basename='snippetclassview')

# router5=DefaultRouter()
# router5.register('SnippetView',SnippetView.as_view(),
#                 basename='SnippetView')




urlpatterns = [

path('',include(router1.urls)),
# path('r2/',include(router2.urls)),
# path('r3/',include(router3.urls)),

# path('',include(router4.urls)),
# path('SnippetView/',include(router5.urls)),

# path('<int:pk>/', views.snippet_list, name='snippet_list'),
# path('',SnippetView.as_view()),
# path('detail_view/<int:id>/',SnippetDetialView.as_view()),
# path('generic_view/<int:id>/',GenericSnippetView.as_view()),
# path('<int:pk>/',SnippetView.as_view()),
]
