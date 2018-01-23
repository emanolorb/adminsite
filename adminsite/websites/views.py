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
        now = datetime.now()
        datenow = date(now.year,now.month,now.day)
        TimeWorked_obj = TimeWorked.objects.filter(user=request.user, date__range=(datenow, datenow))
        WorkOrder_obj = WorkOrder.objects.filter(is_active=True)
        context = {
            'orders': WorkOrder_obj,
            'save': False,
            'works': TimeWorked_obj,
            'querytoday': True,
        }
        if ('date' in request.GET):
            datefilter = request.GET.get('date')
            if (request.GET.get('date') != ''):
                context['datefilter'] = datefilter
                datefilter = datefilter.split("-")
                datefilter = date(int(datefilter[0]),int(datefilter[1]),int(datefilter[2]))
                fecha1 = datefilter + timedelta(days=1)
                fecha2 = datefilter - timedelta(days=1)
                context['works'] = TimeWorked.objects.filter(user=request.user, date__range=(datefilter, datefilter))
                TimeWorked_obj = TimeWorked.objects.filter(user=request.user, date__range=(datefilter, datefilter))
                context['querytoday'] = False
        # filter(pub_date__gte=datetime.date(2005, 1, 30))
        if request.method == 'POST':
            resultado = CuentaHoras(request.POST.get('hora1'), request.POST.get('hora2'))
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
    context = {
        'orders': WorkOrder_obj,
    }
    return render(request, 'workOrder.html', context)

def EditView(request, wrk=None):
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect('/userlogin/')
    editsave = False
    if request.method == 'POST':
        TimeWorked_obj = TimeWorked.objects.get(id=wrk)
        if (request.POST.get('Start') != TimeWorked_obj.start):
            TimeWorked_obj.start = request.POST.get('Start')
        if (request.POST.get('workorder') != str(TimeWorked_obj.work_order.id)):
            TimeWorked_obj.work_order = WorkOrder.objects.get(id=request.POST.get('workorder'))
        if (request.POST.get('Finish') != TimeWorked_obj.finish):
            TimeWorked_obj.finish = request.POST.get('Finish')
        if (request.POST.get('context') != TimeWorked_obj.context):
            TimeWorked_obj.context = request.POST.get('context')
        if (request.POST.get('location') != TimeWorked_obj.location):
            TimeWorked_obj.location = request.POST.get('location')
        if ('img' in request.FILES):
            TimeWorked_obj.img=request.FILES['img']
        horasminutos = CuentaHoras(TimeWorked_obj.start, TimeWorked_obj.finish)
        TimeWorked_obj.hours = horasminutos[0]
        TimeWorked_obj.minutes = horasminutos[1]
        TimeWorked_obj.save()
        editsave = True
    if  wrk != None:
        vacio = False
        try:
            TimeWorked_obj = TimeWorked.objects.get(id=wrk)
            Workselect_obj = WorkOrder.objects.get(id=TimeWorked_obj.work_order_id)
        except:
            TimeWorked_obj = None
            vacio = True
            Workselect_obj = "- -"
    else:
        TimeWorked_obj = None
        vacio = True
        Workselect_obj = "- -"
    WorkOrder_obj = WorkOrder.objects.filter(is_active=True)
    context = {
        'orders': WorkOrder_obj,        
        'work': TimeWorked_obj,
        'vacio': vacio,
        'Workselect_obj': Workselect_obj,
        'save': editsave,
    }
    return render(request, 'edit.html', context)

def CuentaHoras(a, b):
    formato = "%H:%M"
    h1 = datetime.strptime(a, formato)
    h2 = datetime.strptime(b, formato)
    if (h1>h2):
        dh = timedelta(hours=24) 
        resultado = h1 - h2
        resultado = dh - resultado
        resultado = str(resultado).split(":")
        return(resultado[0],resultado[1])
    elif (h1==h2):
        return("24","00")
    else:
        resultado = h2 - h1
        resultado = str(resultado).split(":")
        return(resultado[0],resultado[1])
