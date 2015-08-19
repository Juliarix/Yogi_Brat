from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Yogi_Brat.models import Blog, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from members.views import User
from django.shortcuts import redirect 
# from django.core.urlresolvers import reverse


def home(request):
	return render(request, 'Yogi_Brat/home.html', {})

def yoga(request):
	return render(request, 'Yogi_Brat/Yoga.html', {})

def thai_yoga_massage(request):
	return render(request, 'Yogi_Brat/Thai_Yoga_Massage.html', {})

def blog(request):
	blogs = Blog.objects.all()
	return render(request, 'Yogi_Brat/Blog.html', {"blogs": blogs, "text":"text"})

def blog_page(request,blog_id):
	b = Blog.objects.get(pk=blog_id)
	return render(request, 'Yogi_Brat/Blog.html', {"title":b.title, "text":b.text})

def events(request):
	return render(request, 'Yogi_Brat/Events.html', {})

def contact(request):
	return render(request, 'Yogi_Brat/Contact.html', {})

def submit_contact(request):
	contact = Contact()
	contact.name = request.POST["name"]
	contact.question = request.POST["question"]
	contact.email = request.POST["email"]
	contact.save()
	return HttpResponse('Thank you, your question has been submitted successfully!')

# def course_register(request):
# 	user = authenticate(username = request.POST.get('user_name'), password = request.POST.get('password'))
# 	if user is not None:
# 		login(request, user)
# 		return HttpResponseRedirect(reverse('members:index'))
# 	return HttpResponseRedirect(reverse('members:login'))


# def appt_scheduler(request):
# 	user = authenticate(username = request.POST.get('user_name'), password = request.POST.get('password'))
# 	if user is not None:
# 		login(request, user)
# 		return HttpResponseRedirect(reverse('members:index'))
# 	return HttpResponseRedirect(reverse('members:login'))


def quiz(request):
	return render(request, 'Yogi_Brat/quiz.html', {})

def quiz_results(request):
	score=0
	
	limbs = request.POST.get('limbs')
	if limbs == "8":
		score += 10

	
	yamas = request.POST.get('yamas')
	if yamas == "5":
		score += 10

	niyamas = request.POST.get('niyamas')
	if niyamas == "5":
		score += 10

	
	asana = request.POST.get('asana')
	if asana == "Asana":
		score += 10

	pranayama = request.POST.get("pranayama")
	if pranayama == "Pranayama":
		score += 10

	pratyahara = request.POST.get("pratyahara")
	if pratyahara == "Turning inward, withdrawal of the senses":
		score += 10

	dharana	= request.POST.get("dharana")
	if dharana == "concentration":
		score += 10
	
	dhyana = request.POST.get("dhyana")
	if dhyana == "meditation":
		score += 10

	ayamas = request.POST.get("ayamas")
	if ayamas == "sauca":
		score += 10
	
	aniyamas = request.POST.get("aniyamas")
	if aniyamas == "asteya":
		score += 10

	samadhi = request.POST.get("samadhi")
	if samadhi == "False":
		score += 8
	
	if score == 108:
		return render(request, 'Yogi_Brat/quiz_results.html', {'string':'You must be a guru! Your quiz score is a sacred yogic number: ', 'score': score })

	if score >= 90:
		return render(request, 'Yogi_Brat/quiz_results.html', {'string': 'You are an excellent Yogi. Your quiz score is ', 'score': score})

	if score >= 80:
		return render(request, 'Yogi_Brat/quiz_results.html', {'string': 'You are a good Yogi. Your quiz score is ', 'score': score})

	else:
		return render(request, 'Yogi_Brat/quiz_results.html', {'string': 'You are on the path. Keep practicing! Your quiz score is ', 'score': score})


	# Member Model for DB build
	# member = Member()
	# member.first_name = request.POST["first_name"]
	# member.last_name = request.POST["last_name"]
	# member.username = request.POST["username"]
	# member.password = request.POST["password"]
	# member.email = request.POST["email"]
	# member.save()
	# return HttpResponse


#   DB result model code
# 	results = Quiz()
# 	quiz.limbs = request.POST["limbs"]
# 	quiz.yamas = request.POST["yamas"]
# 	quiz.niyamas = request.POST["niyamas"]
# 	quiz.asana = request.POST["asana"]
# 	quiz.dhyana = request.POST["dhyana"]
# 	quiz.pratyahara = request.POST["pratyahara"]
# 	quiz.samadhi = request.POST["samadhi"]
# 	quiz.dharana = request.POST["dharana"]
#	quiz.pranayama = request.POST["pranayama"]
# 	quiz.ayamas = request.POST["ayamas"]
# 	quiz.aniyamas = request.POST["aniyamas"]
#	return render(request, 'Yogi_Brat/quiz_results.html', {})



# def contact(request):
# 	errors = []
# 	if request.method == 'POST':
# 		if not request.POST.get('subject', ''):
# 			errors.append('Enter a subject.')
#     		if not request.POST.get('message', ''):
#     			errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#         	try:
#         		send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'juliarix@gmail.com'),
#                 ['juliarix@mac.com'],
#                 )
#             	return HttpResponse('Thank you, form has been submitted successfully')
#             except Exception, err: 
#             	return HttpResponse(str(err))
#     return render(request, 'contact_form.html',
#         {'errors': errors})

