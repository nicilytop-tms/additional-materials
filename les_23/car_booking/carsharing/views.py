from django.shortcuts import render


def get_main_page(request):
    return render(request, 'main.html')


def create_user(request):
    if request.method == 'GET':
        return render(request, 'create_user.html')


def create_car(request):
    if request.method == 'GET':
        return render(request, 'create_car.html')

    elif request.method == 'POST':
        model_auto = request.POST['model']
        brand = request.POST['brand']
        vin = request.POST['vin']

        return render(request, 'create_car.html', context={'success_message': 'Success!'})


def book_or_take(request):
    if request.method == 'GET':
        return render(request, 'book_or_take.html')
