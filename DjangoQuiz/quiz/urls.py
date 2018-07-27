from django.urls import path
from quiz import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play-quiz', views.playquiz, name='play-quiz'),
    path('play-quiz-next', views.playquiznext, name='play-quiz-next'),
    path('contactus', views.contactus, name='contactus'),
    path('questions',views.QuestionList.as_view(),name='qlist'),
    path('question/<int:pk>',views.QuestionDetail.as_view(),name='qdetail'),
    path('new',views.QuestionCreate.as_view(),name='qcreate'),
    path('edit/<int:pk>',views.QuestionUpdate.as_view(),name='qedit'),
    path('delete/<int:pk>',views.QuestionDetete,name='qdelete'),
]
