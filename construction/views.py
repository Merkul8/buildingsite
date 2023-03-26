from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from .models import Construction
from django.views.generic import ListView, DetailView

class Home(ListView):
    model = Construction
    template_name = 'construction/main.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pol'] = Construction.objects.get(pk=1)
        context['vanna'] = Construction.objects.get(pk=4)
        context['polpod'] = Construction.objects.get(pk=5)
        context['kotel'] = Construction.objects.get(pk=6)
        context['electro'] = Construction.objects.get(pk=7)
        context['lest'] = Construction.objects.get(pk=3)
        context['potolki'] = Construction.objects.get(pk=2)
        context['voda'] = Construction.objects.get(pk=8)
        context['logo'] = Construction.objects.get(pk=9)
        context['inzh'] = Construction.objects.get(pk=10)
        context['otdelka'] = Construction.objects.get(pk=11)
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
    model = Construction
    template_name = 'construction/inzh.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Construction.objects.get(pk=9)
        context['work_inzh'] = Construction.objects.filter(category_id=2)
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


class CategoryInzh(DetailView):
    model = Construction
    form_class = ContactForm
    context_object_name = 'work_item'
    template_name = 'category_item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Construction.objects.get(pk=9)
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
    model = Construction
    template_name = 'construction/otdelka.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Construction.objects.get(pk=9)
        context['work_otdelka'] = Construction.objects.filter(category_id=1)
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
    model = Construction
    template_name = 'construction/houses.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Construction.objects.get(pk=9)
        context['work_houses'] = Construction.objects.filter(category_id=3)
        context['project_text'] = 'Проекты домов обсуждаются индивидуально с каждым клиентом, сделаем всё по вашему желанию!'
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
    model = Construction
    template_name = 'construction/contact.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Construction.objects.get(pk=9)
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
    model = Construction
    template_name = 'construction/vacancies.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Construction.objects.get(pk=9)
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
    model = Construction
    template_name = 'construction/about_us.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Construction.objects.get(pk=9)
        context['pol'] = Construction.objects.get(pk=1)
        context['pot'] = Construction.objects.get(pk=2)
        context['les'] = Construction.objects.get(pk=3)
        context['van'] = Construction.objects.get(pk=4)
        context['polpod'] = Construction.objects.get(pk=5)
        context['kot'] = Construction.objects.get(pk=6)
        context['ele'] = Construction.objects.get(pk=7)
        context['voda'] = Construction.objects.get(pk=8)
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


class PoliticaCons(ListView):
    model = Construction
    template_name = 'construction/politica.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Construction.objects.get(pk=9)
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