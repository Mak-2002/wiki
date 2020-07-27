from django.shortcuts import render
from django import forms

from . import util

class new_entry_form(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new(request):
    return render(request, "encyclopedia/new.html",{
        "form" : new_entry_form()
    })