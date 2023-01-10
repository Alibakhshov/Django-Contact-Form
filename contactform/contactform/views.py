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
            'missEquipment': missEquipment,
            'message': message
            
        }
        message = '''
        This is an auto generated message, please do not reply. You may contact the sender via {}
        
        Name of the Intern: {}
        
        Checked classroom(TV Lounge): {}
        
        Missing equipments in {}: {}
        
        Other comments: {}
        
        Best regards,
        IT Intern {}
        
        '''.format(data['email'], data['name'], data['classrooms'], data['classrooms'], data['equipment'], data['classrooms'], data['missEquipment'], data['message'], data['name'])
        
        send_mail(data['subject'], message, '', ['<receiveremail>'], ['<senderemail>'])
        
       
    return render(request, 'main.html', {})

