from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
import random
from .models import User
# Create your views here.
def index(request):
	return render(request,'index.html')

def signup(request):
	if request.method == 'POST':
		try:
			user=User.objects.get(email=request.session['email'])
			msg="email alredy register"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=request.POST['password'],
					gender=request.POST['gender'],
					language=request.POST.getlist('language')
					)
				msg="signup successfuly"
				return render(request,'login.html',{'msg':msg})
			else:
				msg='password does not match'
				return render(request,'signup.html',{'msg':msg})

	else:
		return render(request,'signup.html')

def header(request):
	return render(request,'header.html')

def login(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'],
				password=request.POST['password']
				)
			request.session['email']=user.email
			request.session['fname']=user.fname
			return render(request,'index.html')
		except Exception as e:
			print(e)
			msg='email does not match'
			return render(request,'login.html')
	else:
		return render(request,'login.html')

def logout(request):
	del request.session['email']
	del request.session['fname']
	return redirect('login')

def forgotpassword(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'])
			print(user)
			subject = 'OTP For Forgot Password'
			otp=random.randint(1000,9999)
			message = 'Your OTP For Forgot Password Is '+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email,]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'otp':otp,'email':user.email})
		except Exception as e:
			print(e)
			msg="Email Not Registered"
			return render(request,'forgot_password.html',{'msg':msg})
	else:
		return render(request,'forgotpassword.html')
def otp(request):
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	email=request.POST['email']
	if request.POST['otp']==request.POST['uotp']:
		return render(request,'newpassword.html',{'email':email})
	else:
		msg='otp does not match'
		return  render(request,'otp.html',{'msg':msg,'otp':otp,'email':email})

def newpassword(request):
	email=request.POST['email']
	password=request.POST['password']
	cpassword=request.POST['cpassword']
	if request.POST['password']==request.POST['cpassword']:
		user=User.objects.get(email=request.POST['email'])
		user.password=request.POST['password']
		user.save()
		return render(request,'login.html')
	else:
		msg='password and confirm does not match'
		return render(request,'newpassword.html',{'msg':msg})
def  contact(request):
	user=User.objects.all()
	return render(request,'contact.html',{'user':user})

def updateprofile(request,pk):
	user=User.objects.get(pk=pk)

	if request.method=='POST':
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.email=request.POST['email']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		user.gender=request.POST['gender']
		user.language=request.POST.getlist('language')
		user.save()
		msg='user update successfuly'
		return render(request,'updateprofile.html',{'user':user})
	else:
		return render(request,'updateprofile.html',{'user':user})

def delet(request,pk):
	user=User.objects.get(pk=pk)
	user.delete()
	return redirect('contacts')
