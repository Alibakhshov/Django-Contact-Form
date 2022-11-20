from email.message import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        classrooms = request.POST.get('classTV')
        equipment = request.POST.get('equipments')
        missEquipment = request.POST.get('missEquipments')
        message = request.POST.get('message')
        
        
        
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'classrooms': classrooms,
            'equipment': equipment,
            'missEquipment': missEquipment,
            'message': message
            
        }
        message = '''
        This is an auto generated message, please do not reply. You may contact the sender via {}
        
        Name of the Intern: {}
        
        Checked classroom(TV Lounge): {}
        
        Classroom(TV Lounges) equipments: {}
        
        Missing equipments: {}
        
        Other comments: {}
        
        Best regards,
        IT Intern {}
        
        '''.format(data['email'], data['name'], data['classrooms'], data['equipment'], data['missEquipment'], data['message'], data['name'])
        
        send_mail(data['subject'], message, '', ['raufalibakhshov4@gmail.com'], ['raufalibakhshov02@gmail.com'])
        # send_mail(
        #         'subject',
        #         'That’s your message body',
        #         'raufalibakhshov4@gmail.com',
        #         ['raufalibakhshov02@gmail.com'],
        #         fail_silently=False,
        #     )
       
    return render(request, 'main.html', {})

