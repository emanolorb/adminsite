from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from time_worked.models import TimeWorked
from users.models import User


def iniView(request):
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect('/userlogin/')
    else:
        if request.method == 'POST':
            date = request.POST.get('date')
            hora1 = request.POST.get('hora1')
            hora2 = request.POST.get('hora2')
            context = request.POST.get('context')
            file = request.POST.get('file')
            userid = request.POST.get('userid')
            usuario = User.objects.get(id=userid)
            registro = TimeWorked(
                user=usuario,
                date=date,
                start=hora1,
                finish=hora2,
                context=context,
                work_order=request.POST.get('work_order'),
                img=request.FILES['img'],
                )
            registro.save()
            print('------------')
            print(request.FILES)
            print('------------')
        return render(request, 'worker.html', )


def LoginView(request):
    if str(request.user) != "AnonymousUser":
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        context = {
            'error': False,
        }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            # Paquete para el template
            context = {
                'error': True,
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html', context)


def LogoutView(request):
    logout(request)
    return render(request, 'logout.html')


def error404(request):
    return render(request, 'error404.html')

def WorkOrder(request):
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect('/userlogin/')
    return render(request, 'workOrder.html')
