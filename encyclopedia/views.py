from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

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
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        if util.get_entry(title) == None:
            util.save_entry(title, content)
            return HttpResponseRedirct(f"/wiki/{title}")
        return render(request, "encyclopedia/add.html", {
            "form" : form,
            "err_existed" : "Sorry, there's an existing page with this title"
        })
    return render(request, "encyclopedia/new.html", {
        "form" : new_entry_form(),
        "err_existed" :""
    })

def open_entry(request, entry):
    if util.get_entry(entry) == None :
        return render(request, "encyclopedia/err_not_found.html")
    