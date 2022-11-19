from email.message import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        attachment = request.FILES.get('file')
        
        
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'attachment': attachment,
            'message': message
        }
        message = '''
        Name of the Intern: {}
        
        From: {}
        
        New message: {}
        
        Attachment: {}
        
        
        '''.format( data['name'],  data['email'], data['message'], data['attachment'])
        
        send_mail(data['subject'], message, '', ['raufalibakhshov4@gmail.com'], ['raufalibakhshov02@gmail.com'])
        # send_mail(
        #         'subject',
        #         'That’s your message body',
        #         'raufalibakhshov4@gmail.com',
        #         ['raufalibakhshov02@gmail.com'],
        #         fail_silently=False,
        #     )
       
    return render(request, 'main.html', {})

