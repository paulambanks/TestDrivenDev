from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
from accounts.models import Token


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for your To-Do List',
        message_body,
        'noreply@tdd',
        [email]
    )
    messages.success(
        request,
        "Check your email, we've send you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    return redirect('/')