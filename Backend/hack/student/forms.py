from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import notes, Question, Answer, JoinUs

class NoteForm(ModelForm):
    class Meta:
        model = notes
        fields = ['host', 'name', 'file', 'description', 'std']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['body']

class JoinUsForm(ModelForm):
    class Meta:
        model = JoinUs
        fields = ['name', 'email', 'description']