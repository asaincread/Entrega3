from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.urls import reverse
from .forms import PersonForm
from .models import Person


def person_post_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # Do something with the data
    else:
        form = PersonForm()
    return render(
        request,
        'person_post.html',
        {
            'form': form,
            'url_post': reverse('add_person'),
        }
    )


def person_show_view(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        return render(
            request,
            'person_show.html',
            {
                'person_list': persons,
            }
        )
    return HttpResponseNotAllowed([request.method])
