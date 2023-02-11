from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    user = {
        'name': 'Ali'
    }
    user['age'] = 20
    user['fav_fruits'] = ['Banana', 'Apple', 'Pineapple']

    return render(request, 'index.html', context=user)

def about(request):
    return render(request, 'about.html')
