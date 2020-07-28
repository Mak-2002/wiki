from django.shortcuts import render

from . import util

def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new(request):
    return render(request, "encyclopedia/new.html")

def open_entry(request, entry):
    if util.get_entry(entry) == None :
        return render(request, "encyclopedia/err_not_found.html")
    