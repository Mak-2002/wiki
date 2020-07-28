from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
import random

from . import util

class new_entry_form(forms.Form):
    title = forms.CharField(min_length=1, label="")
    content = forms.CharField(min_length=1, label="", widget = forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def new(request):
    if request.method == "POST" :
        form = new_entry_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) == None:
                util.save_entry(title, content)
                return HttpResponseRedirect(f"/wiki/{title}")
            return render(request, "encyclopedia/new.html", {
                "form" : new_entry_form(request.POST),
                "err_found" : "Sorry, there's an existing page with this title"
            })
    return render(request, "encyclopedia/new.html", {
        "form" : new_entry_form(),
        "err_found" : ""
    })

def random_entry(request):
    return HttpResponseRedirect(f"/wiki/{random.choice(util.list_entries()) }")