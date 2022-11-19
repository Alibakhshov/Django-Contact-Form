from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message {}:
        
        From: {}
        '''.format(data['message'], data['email'], data['name'], data['subject'])
        # send_mail(data['subject'], message, '', ['raufalibakhshov4@gmail.com'])
        send_mail(data['subject'], data['name'], data['message'], ['raufalibakhshov4@gmail.com'])
        
       
    return render(request, 'main.html', {})

