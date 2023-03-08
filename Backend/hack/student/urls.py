from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('h/', views.h, name="h"),

    path('join/', views.joinus, name="joinus"),

    path('i/', views.i, name="i"),
    # URLS for Question & Answers (Community)
    path('index/', views.index, name="index"),
    path('ask-question/', views.ask_question, name="ask_question"),
    path('answer-question/<int:question_id>/', views.answer_question, name="answer_question"),
    path('question-detail/<int:question_id>/', views.question_detail, name="question_detail"),


    path('notes/', views.h_notes, name="h_notes"),
    path('create-note/', views.createNote, name="createNote"),
    path('update-note/<str:pk>/', views.updateNote, name="updateNote"),
    path('delete-note/<str:pk>/', views.deleteNote, name="deleteNote"),
    path('note/<int:note_id>/', views.note, name="note"),
    path('h-note/<int:note_id>/', views.h_note, name="h_note"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)