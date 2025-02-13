from django.urls import path
from .views import PageListViews,Page_Detail_view,PageCreateView,PageUpdateView,PageDeleteView


pages_patterns = ([
    path('', PageListViews.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', Page_Detail_view.as_view(), name='page'),
    path('create/',PageCreateView.as_view(), name='create'),
    path('update/<int:pk>/',PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',PageDeleteView.as_view(), name='delete')
],'pages')