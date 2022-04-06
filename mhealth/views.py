from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def home(request):
 return render(request, 'mhealth/index.html', {'title': 'Home'})
 #return HttpResponse('<h1>Blog Home</h1>')

def contact(request):
 if request.method == "POST":
  message_name = request.POST['message-name']
  message_email = request.POST['message-email']
  message = request.POST['message']

  # send an email
  send_mail(
    message_name, # subject
    message, # message
    message_email, # from email
    ['team6iwd@gmail.com'], # To Email (our receptionist email)
  )
  return render(request, 'mhealth/contact.html', {'message_name':message_name})
 else:
  return render(request, 'mhealth/contact.html', {'title': 'Contact'})

def appointment(request):
 if request.method == "POST":
  your_name  = request.POST['your-name']
  your_number    = request.POST['your-number']
  your_email = request.POST['your-email']
  your_date  = request.POST['your-date']

      #send an Email

  appointment = "Name: " +   your_name + "Phone Number: " + your_number + "Email : " + your_email + "Appointment Date :" + your_date


  send_mail(
     "Appointment Request", # subject
     appointment, # message
     your_email, # from email
     ['team6iwd@gmail.com'], # To Email (our receptionist email)
   )

  # send_mail(
  #       'Appointment Request' # subject
  #       appointment, # message
  #       message_email, # from email
  #       ['team6iwd@gmail.com'],)


  return render(request, 'mhealth/appointment.html', {'your_name': your_name})
 else:
  return render(request, 'mhealth/appointment.html', {'title': 'Appointment'})

def pharmacy(request):
  return render(request, 'mhealth/pharmacy.html', {'title': 'Pharmacy'})

def testkit(request):
  return render(request, 'mhealth/testkit.html', {'title': 'Testkit'})
