from django.shortcuts import render, redirect
from .models import Course, Event, Resource
from .forms import SearchForm, CustomUserCreationForm
from haystack.query import SearchQuerySet
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .filters import CourseFilter, EventFilter
from dal import autocomplete

def home(request):
    return render(request, 'Hompage.html')


def search(request):
    form = SearchForm()
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = SearchQuerySet().filter(content=query)

    return render(request, 'Homepage.html', {'form': form, 'results': results})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def course_list(request):
    course_filter = CourseFilter(request.GET, queryset=Course.objects.all())
    return render(request, 'course_list.html', {'filter': course_filter})

def event_list(request):
    event_filter = EventFilter(request.GET, queryset=Event.objects.all())
    return render(request, 'event_list.html', {'filter': event_filter})


class CustomLoginView(LoginView):
    template_name = 'login.html'

class CourseAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Course.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs