from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        print(request.POST.get('image_url', ''))
    context = {'data': 'This is Face App'}
    return render(request, 'face/index.html', context)
