from django.shortcuts import render
from django.views.generic import ListView


def trending(request):
	return render(request, 'sidebar/trending.html', { 'Title': 'Trending'})
