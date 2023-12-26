from django.shortcuts import render, get_object_or_404
from apps.base.models import Index
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot
from apps.telegram.views import get_text
from django.core.mail import send_mail


def index(request, slug=None):
    if slug:
        index = get_object_or_404(Index, slug=slug)
    else:
        index = Index.objects.latest('id')
    
    if request.method =="POST":
        info =  request.POST.get('fullinfo').split(",")
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        fullinfo = []
        for i in info:
            if len(i) > 1:
                fullinfo.append(i)
                print(i)
        print(fullinfo)
        print(len(fullinfo))

        fullinfo_pro = [i.strip() for i in info if len(i.strip()) > 1]
        formatted_fullinfo = '\n'.join(fullinfo_pro)
        get_text(
        f"""
Новая заявка:

Имя пользователя: {name}

Номер телефона: {phone}

Почта (email): {email}

Выбранные поля:

{formatted_fullinfo}
        """
    )

        send_mail(
            f'{name}',

            f'Новая заявка от пользователя {name}. \nНомер телефона - {phone} \nПочта - {email} \nВыбранные поля: \n{formatted_fullinfo}',
            "noreply@somehost.local",
            ["grogertm@gmail.com"])
        
        return redirect('index_no_slug')
    return render(request, "base/index.html", locals())


def errors(request, exception):
    return render(request, "404/404.html", status=404)


