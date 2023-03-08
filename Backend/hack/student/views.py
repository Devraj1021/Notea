from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import notes, profile
from .forms import NoteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm, JoinUsForm
# hack
# hack@gmail.com
# hack123
# Create your views here.

# arya
# stark123

def home(request):
    return render(request, 'student/home.html')

@login_required
def h(request):
    if request.method != 'GET':
        data = notes.objects.all()
        return render(request, 'student/h.html', {'data':data})
    else:
        q = request.GET.get('q') if request.GET.get('q') != None else ''

        data = notes.objects.filter(
            Q(name__icontains=q) | 
            Q(description__icontains=q)
            )

        return render(request, 'student/h.html', {"data":data})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('h')

    return render(request, 'student/login.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')

# def registerPage(request):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return redirect('h')
#         else:
#             messages.error(request, 'An error occurred during registration')

#     return render(request, 'student/register.html', {'form': form})

# register form without inbuild forms
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        pw = request.POST.get('password')
        pw1 = request.POST.get('repeat-password')
        if pw == pw1:
            try:
                usr = User.objects.get(username=username)
                return render(request, 'student/register.html', {"msg":"Username already registered"})
            except User.DoesNotExist:
                usr = User.objects.create_user(username=username, password=pw, email=email)
                usr.save()
                login(request, usr)
                return redirect('h')
        else:
            return render(request, 'student/register.html', {"msg":"passwords did not match"})
    else:
        return render(request, 'student/register.html')


@login_required
def createNote(request):
    fm = NoteForm()
    if request.method == 'POST':
        data = NoteForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            fm = NoteForm()
            return render(request, 'student/createNote.html', {"fm":fm, "msg":"record created"})
        else:
            return render(request, 'student/createNote.html', {"fm":data, "msg":"check errors "})
    else:
        fm = NoteForm()
        return render(request, 'student/createNote.html', {"fm":fm})

@login_required
def updateNote(request, pk):
        data = notes.objects.all()
        return render(request, 'student/home.html', {"data":data})

@login_required
def deleteNote(request, pk):
        data = notes.objects.all()
        return render(request, 'student/home.html', {"data":data})

@login_required
def note(request, note_id):
    note = get_object_or_404(notes, id=note_id)
    context = {'note': note}
    return render(request, 'student/note.html', context)

def h_note(request, note_id):
    note = get_object_or_404(notes, id=note_id)
    context = {'note': note}
    return render(request, 'student/h_note.html', context)

def index(request):
    # Get all questions and display them
    questions = Question.objects.all()
    return render(request, 'student/index.html', {'questions': questions})

def i(request):
    questions = Question.objects.all()
    return render(request, 'student/i.html', {'questions': questions})

@login_required
def ask_question(request):
    # Display a form for asking a new question
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('h')
    else:
        form = QuestionForm()
    return render(request, 'student/ask_question.html', {'form': form})

@login_required
def answer_question(request, question_id):
    # Display a form for answering a question
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('index')
    else:
        form = AnswerForm()
    return render(request, 'student/answer_question.html', {'form': form, 'question': question})

@login_required
def question_detail(request, question_id):
    # Display a question and its answers
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'student/question_detail.html', {'question': question, 'answers': answers})

# def joinus(request):
#     if request.method == 'POST':
#         join = joinus.objects.create(
#             name = request.POST.get('name'),
#             email = request.POST.get('email'),
#             description = request.POST.get('description')
#         )
#         return redirect('home')
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     name = request.POST.get('name')
    #     description = request.POST.get('description')
    #     try:
    #         join = joinus.get(email=email)
    #         return render(request, 'student/joinus.html', {"msg":"Email already registered"})
    #     except:
    #         join = joinus.create(email=email, name=name, description=description)
    #         join.save()
    # #         return redirect('home')
    # else:
    #     return render(request, 'student/joinus.html')
def joinus(request):
    if request.method == 'POST':
        form = JoinUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'student/joinus.html')
    else:
        form = JoinUsForm()
    return render(request, 'student/joinus.html', {'form':form})


def h_notes(request):
    if request.method != 'GET':
        data = notes.objects.all()
        return render(request, 'student/notes.html', {'data':data})
    else:
        q = request.GET.get('q') if request.GET.get('q') != None else ''

        data = notes.objects.filter(
            Q(name__icontains=q) | 
            Q(description__icontains=q)
            )

        return render(request, 'student/notes.html', {"data":data})

@login_required
def h(request):
    if request.method != 'GET':
        data = notes.objects.all()
        return render(request, 'student/h.html', {'data':data})
    else:
        q = request.GET.get('q') if request.GET.get('q') != None else ''

        data = notes.objects.filter(
            Q(name__icontains=q) | 
            Q(description__icontains=q)
            )

        return render(request, 'student/h.html', {"data":data})