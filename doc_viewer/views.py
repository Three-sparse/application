from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def viewer(request: HttpRequest, document_id: int):
    context = {
        'document_id': document_id,
        'comment_user': 'Taro',
        'comment_page': '1 / 2',
        'comment_text': 'Hello',
    }
    return render(request, 'doc_viewer/viewer.html', context)
