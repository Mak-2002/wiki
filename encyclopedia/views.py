from django.shortcuts import render
from django import forms

from . import util

class new_entry_form(forms.Form):
    title = forms.CharField(min_length=1)
    content = forms.CharField(min_length=1, widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new(request):
    if request.method == "POST":
        form = new_entry_form(request.POST)
        if util.get_entry(form.cleaned_data["title"]):
            return render(request, "encyclopedia/new.html", {
                "err_existed" : "Sorry, there's an existed page with the this title, please choose another one",
                "form" : form
            })
    return render(request, "encyclopedia/new.html", {
        "form" : new_entry_form(),
        "err_existed" : ""
    })

def open_entry(request, entry):
    if util.get_entry(entry) == None :
        return render(request, "encyclopedia/err_not_found.html")
    