
from django.shortcuts import render
from .ml import get_review_status


def review_status(request):
    if request.method == 'POST':
        text = request.POST.get('review_text')
        if text:
            resp = get_review_status(text)
            context = {'sentiment': resp['sentiment'],
                       'rating': resp['stars_count'],
                       'review_text': text}
            return render(request, 'review_status.html', context)
    context = {'sentiment': '?',
               'rating': '?',
               'review_text': ""}
    return render(request, 'review_status.html', context)
