from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta, date
from time_worked.models import TimeWorked
from work_order.models import WorkOrder
from workers.models import WorkerUser
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

def paymentView(request):
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect('/userlogin/')
    datefilter = ""
    rangofechas = ""
    if request.method == 'GET':
        userlist = []
        if 'date' in request.GET:
            dateget = request.GET.get('date')
            if dateget != "":
                datefilter = dateget
                dateget = dateget.split("-")
                print('-----------------')
                fecha = datetime(int(dateget[0]), int(dateget[1]), int(dateget[2]))
                unDia = timedelta(days=1)
                fecha2 = fecha - timedelta(days=14)
                rangofechas = []
                variablefechas = []
                for contador in range(0, 14):
                    fecha2 = fecha2 + unDia
                    variablefechas.append(fecha2.date())
                    rangofechas.append(str(diasemana(fecha2.weekday())) +'\n' + str(fecha2.date()).replace("-", "/"))
                # creamos los datos de los usuarios
                numuser = 1
                for u in WorkerUser.objects.filter(is_active=True):
                    userarray = {}
                    userarray['id'] = u.id
                    userarray['name'] = u.name
                    hourT = 0
                    minutesT = 0
                    hourTweekend = 0
                    minutesTweekend = 0
                    diasweekend = 0
                    for contador2 in range(0, 14):
                        TimeWorkedobj = TimeWorked.objects.values('hours', 'minutes').filter(user=u, date__range=(variablefechas[contador2], variablefechas[contador2]))
                        if TimeWorkedobj.count() == 0:
                            userarray[contador2] = "00:00"
                        else:
                            for times in TimeWorkedobj:
                                hourT = hourT + times['hours']
                                minutesT = minutesT + times['minutes']
                                if variablefechas[contador2].weekday() == 6 or variablefechas[contador2].weekday() == 5:
                                    diasweekend = diasweekend + 1
                                    hourTweekend = hourTweekend + times['hours']
                                    minutesTweekend = minutesTweekend + times['minutes']
                                if times['minutes'] < 10:
                                    userarray[contador2] = str(times['hours']) + ":0" + str(times['minutes'])
                                else:
                                    userarray[contador2] = str(times['hours']) + ":" + str(times['minutes'])
                    hm = int(minutesT/60)
                    minutesT = minutesT - (hm*60)
                    hourT = hourT + hm
                    if minutesT < 10:
                        userarray['htotal'] = str(hourT) + ":0" + str(minutesT)
                    else:
                        userarray['htotal'] = str(hourT) + ":" + str(minutesT)
                    hm = int(minutesTweekend/60)
                    minutesTweekend = minutesTweekend - (hm*60)
                    hourTweekend = hourTweekend + hm
                    if minutesTweekend < 10:
                        userarray['hweektotal'] = str(hourTweekend) + ":0" + str(minutesTweekend)
                    else:
                        userarray['hweektotal'] = str(hourTweekend) + ":" + str(minutesTweekend)
                    userarray['dweektotal'] = str(diasweekend)
                    userlist.append(userarray)
                    numuser = numuser + 1
                print(userlist)
                print("''''''''''''")
    context = {
        'users': userlist,
        'rangofechas': rangofechas,
        'prueba': 'WorkOrder_obj',        
        'datefilter': datefilter,
    }
    return render(request, 'payment.html', context)

def diasemana(dia):
    if dia == 0:
        return('Monday')
    if dia == 1:
        return('Tuesday')
    if dia == 2:
        return('Wednesday')
    if dia == 3:
        return('Thursday')
    if dia == 4:
        return('Friday')
    if dia == 5:
        return('Saturday')
    if dia == 6:
        return('Sunday')