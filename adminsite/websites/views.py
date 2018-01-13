from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta, date
from time_worked.models import TimeWorked
from work_order.models import WorkOrder
from users.models import User


def iniView(request):
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect('/userlogin/')
    else:
        TimeWorked_obj = TimeWorked.objects.filter(user=request.user)
        WorkOrder_obj = WorkOrder.objects.filter(is_active=True)
        context = {
            'orders': WorkOrder_obj,
            'save': False,
            'works': TimeWorked_obj,
        }
        if ('date' in request.GET):
            datefilter = request.GET.get('date')
            if (request.GET.get('date') != ''):
                context['datefilter'] = datefilter
                datefilter = datefilter.split("-")
                datefilter = date(int(datefilter[0]),int(datefilter[1]),int(datefilter[2]))
                fecha1 = datefilter + timedelta(days=1)
                fecha2 = datefilter - timedelta(days=1)
                context['works'] = TimeWorked_obj.filter(date__range=(datefilter, datefilter))
                TimeWorked_obj = TimeWorked_obj.filter(date__range=(datefilter, datefilter))
        # filter(pub_date__gte=datetime.date(2005, 1, 30))
        if request.method == 'POST':
            formato = "%H:%M"
            h1 = datetime.strptime(request.POST.get('hora1'), formato)
            h2 = datetime.strptime(request.POST.get('hora2'), formato)
            resultado = h2 - h1
            resultado = str(resultado).split(":")
            workorderobj = WorkOrder.objects.get(id=request.POST.get('workorder'))
            usuario = User.objects.get(id=request.user.id)
            registro = TimeWorked(
                user=usuario,
                date=request.POST.get('date'),
                start=request.POST.get('hora1'),
                finish=request.POST.get('hora2'),
                context=request.POST.get('context'),
                work_order=workorderobj,
                hours=int(resultado[0]),
                minutes=int(resultado[1]),
                location=request.POST.get('location'),
                img=request.FILES['img'],
                )
            registro.save()
            context['save'] = True
        if (TimeWorked_obj.count() > 0):
            h = 0
            m = 0
            for works in TimeWorked_obj:
                h = h + works.hours
                m = m + works.minutes
            hm = int(m/60)
            m = m - (hm*60)
            h = h + hm
            context['horastotal'] = True
            context['horas'] = str(h) + " hours "+ str(m) + " minutes "
            print(context)
        return render(request, 'worker.html', context )


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

def WorkOrderView(request):
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect('/userlogin/')
    # WorkOrderWorkOrder_obj = WorkOrder.objects.filter(is_active=True)
    WorkOrder_obj = WorkOrder.objects.all()
    print(WorkOrder_obj.count())
    context = {
        'orders': WorkOrder_obj,
    }
    return render(request, 'workOrder.html', context)
