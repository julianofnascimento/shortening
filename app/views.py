from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from urllib.parse import urlparse
import re
from app.models import Urls
from app.forms import UrlForm
from lib.url_shortening import shorten_url

class IndexView(View):
    def get(self, request):
        form = UrlForm()
        return render(request, "app/index.html", {"form": form})

    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            shortened_url = Urls.objects.filter(url=url).first()
            if shortened_url:
                return HttpResponse(url + ': ' + shortened_url.short_url_key)
            else:
                try:
                    last_url_key = Urls.objects.latest('id').short_url_key
                except ObjectDoesNotExist:
                    last_url_key = ''
                short_url_key = shorten_url(last_url_key)
                stored_url = Urls(url=url, short_url_key=short_url_key)
                stored_url.save()

                full_url = request.get_host() + '/' + short_url_key

                return HttpResponse(url + ': ' + full_url)
        else:
            return render(request, "app/index.html", {"form": form})

class RedirectUrlView(View):
    def get(self, request, url_key):
        try:
            url = Urls.objects.filter(short_url_key=url_key).first()
            return HttpResponseRedirect('http://' + url.url)
        except ObjectDoesNotExist:
            return HttpResponse('Link not found')

