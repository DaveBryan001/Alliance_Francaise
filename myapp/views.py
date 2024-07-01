from django.shortcuts import render
from .models import Course, Event, Resource
from .forms import SearchForm


def search(request):
    form = SearchForm()
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Course.objects.filter(name__icontains=query) | \
                      Event.objects.filter(name__icontains=query) | \
                      Resource.objects.filter(name__icontains=query)

    return render(request, 'search.html', {'form': form, 'results': results})
