from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def viewer(request: HttpRequest, document_id: int):
    return render(request, 'doc_viewer/viewer.html', {})
