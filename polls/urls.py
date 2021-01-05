from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /polls/
    ##path('', views.index, name='index'),
    # ex: /polls/5/
    # the 'name' value is set as called by the {% url %} template tag in ...polls\templates\polls\detail.html
    ##path('specifics/<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    ##path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    ##path('<int:question_id>/vote/', views.vote, name='vote'),
]
