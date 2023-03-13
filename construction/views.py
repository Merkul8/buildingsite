from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from .models import ConstructionModel
from django.views.generic import ListView

class Home(ListView):
    model = ConstructionModel
    template_name = 'construction/main.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pol'] = ConstructionModel.objects.get(pk=1)
        context['polpod'] = ConstructionModel.objects.get(pk=2)
        context['kotel'] = ConstructionModel.objects.get(pk=3)
        context['electro'] = ConstructionModel.objects.get(pk=7)
        context['lest'] = ConstructionModel.objects.get(pk=8)
        context['potolki'] = ConstructionModel.objects.get(pk=9)
        context['logo'] = ConstructionModel.objects.get(pk=10)
        context['inzh'] = ConstructionModel.objects.get(pk=11)
        context['otdelka'] = ConstructionModel.objects.get(pk=12)
        context['form'] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text_for_send = ' '.join(
                ['NAME - ' + form.cleaned_data['name'] + '\n', 
                'PHONE NUMBER - ' + str(form.cleaned_data['phone_number']) + '\n', 
                'E-MAIL - ' + form.cleaned_data['email'] + '\n', 
                'COMMENT - ' + form.cleaned_data['comment'] + '\n'])
            mail = send_mail(form.cleaned_data['name'], text_for_send,
                      'max.merkulov.00@mail.ru', ['max.merkulov.00@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')


class InzhCons(ListView):
    model = ConstructionModel
    template_name = 'construction/inzh.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = ConstructionModel.objects.get(pk=10)
        context['work_inzh'] = ConstructionModel.objects.filter(category_id=2)
        context['form'] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text_for_send = ' '.join(
                ['NAME - ' + form.cleaned_data['name'] + '\n', 
                'PHONE NUMBER - ' + str(form.cleaned_data['phone_number']) + '\n', 
                'E-MAIL - ' + form.cleaned_data['email'] + '\n', 
                'COMMENT - ' + form.cleaned_data['comment'] + '\n'])
            mail = send_mail(form.cleaned_data['name'], text_for_send,
                      'max.merkulov.00@mail.ru', ['max.merkulov.00@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')


class OtdelkaCons(ListView):
    model = ConstructionModel
    template_name = 'construction/otdelka.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = ConstructionModel.objects.get(pk=10)
        context['work_otdelka'] = ConstructionModel.objects.filter(category_id=1)
        context['form'] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text_for_send = ' '.join(
                ['NAME - ' + form.cleaned_data['name'] + '\n', 
                'PHONE NUMBER - ' + str(form.cleaned_data['phone_number']) + '\n', 
                'E-MAIL - ' + form.cleaned_data['email'] + '\n', 
                'COMMENT - ' + form.cleaned_data['comment'] + '\n'])
            mail = send_mail(form.cleaned_data['name'], text_for_send,
                      'max.merkulov.00@mail.ru', ['max.merkulov.00@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')


class HouseCons(ListView):
    model = ConstructionModel
    template_name = 'construction/houses.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = ConstructionModel.objects.get(pk=10)
        context['work_houses'] = ConstructionModel.objects.filter(category_id=3)
        context['form'] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text_for_send = ' '.join(
                ['NAME - ' + form.cleaned_data['name'] + '\n', 
                'PHONE NUMBER - ' + str(form.cleaned_data['phone_number']) + '\n', 
                'E-MAIL - ' + form.cleaned_data['email'] + '\n', 
                'COMMENT - ' + form.cleaned_data['comment'] + '\n'])
            mail = send_mail(form.cleaned_data['name'], text_for_send,
                      'max.merkulov.00@mail.ru', ['max.merkulov.00@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')


class ContactCons(ListView):
    model = ConstructionModel
    template_name = 'construction/contact.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = ConstructionModel.objects.get(pk=10)
        context['form'] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text_for_send = ' '.join(
                ['NAME - ' + form.cleaned_data['name'] + '\n', 
                'PHONE NUMBER - ' + str(form.cleaned_data['phone_number']) + '\n', 
                'E-MAIL - ' + form.cleaned_data['email'] + '\n', 
                'COMMENT - ' + form.cleaned_data['comment'] + '\n'])
            mail = send_mail(form.cleaned_data['name'], text_for_send,
                      'max.merkulov.00@mail.ru', ['max.merkulov.00@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')


class VacanciesCons(ListView):
    model = ConstructionModel
    template_name = 'construction/vacancies.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = ConstructionModel.objects.get(pk=10)
        context['form'] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text_for_send = ' '.join(
                ['NAME - ' + form.cleaned_data['name'] + '\n', 
                'PHONE NUMBER - ' + str(form.cleaned_data['phone_number']) + '\n', 
                'E-MAIL - ' + form.cleaned_data['email'] + '\n', 
                'COMMENT - ' + form.cleaned_data['comment'] + '\n'])
            mail = send_mail(form.cleaned_data['name'], text_for_send,
                      'max.merkulov.00@mail.ru', ['max.merkulov.00@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')


class AboutUsCons(ListView):
    model = ConstructionModel
    template_name = 'construction/about_us.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = ConstructionModel.objects.get(pk=10)
        context['form'] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text_for_send = ' '.join(
                ['NAME - ' + form.cleaned_data['name'] + '\n', 
                'PHONE NUMBER - ' + str(form.cleaned_data['phone_number']) + '\n', 
                'E-MAIL - ' + form.cleaned_data['email'] + '\n', 
                'COMMENT - ' + form.cleaned_data['comment'] + '\n'])
            mail = send_mail(form.cleaned_data['name'], text_for_send,
                      'max.merkulov.00@mail.ru', ['max.merkulov.00@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')