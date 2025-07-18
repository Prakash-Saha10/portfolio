from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Project,Contact
from django.contrib.auth.models import User
from .forms import ContactForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request):
    return render(request,'myportfolio/index.html')

def about(request):
    skills = [
        {'name': 'Python', 'level': 70},
        {'name': 'Django', 'level': 70},
        {'name': 'Product Analysis', 'level': 80},
        {'name': 'SQL', 'level': 75},
    ]
    return render(request, 'myportfolio/about.html', {'skills': skills})


def Projects(request):
    projects = Project.objects.all()
    return render(request, 'myportfolio/projects.html', {'projects': projects})


# def Projects(request):
#     Projects=Project.objects.all()
#     Projects = [
#         {
#             'title': 'Shooping cart using Python',
#             'description': 'Python based shopping cart which help me to analyze python basic system well',
#             'image': 'myportfolio/images/shopping.png',
#             'link': 'https://github.com/'
#         },
#         {
#             'title': 'Blog and ToDo Application',
#             'description': 'A custom-built blog and todo application with form registration and login process using Django.',
#             'image': 'myportfolio/images/blog applicaton.png',
#             'link': 'https://github.com/yourusername/dictionary-app'
#         },
#         {
#             'title': 'Library management using SQL',
#             'description': 'This is Database related problem where solving many basic and moderation query problems',
#             'image': 'myportfolio/images/library managment.png',
#             'link': '#'
#         },
#     ]
#     return render(request, 'myportfolio/projects.html', {'Projects': Projects})


def resume(request):
    return render(request, 'myportfolio/resume.html')



def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
          form.save()
          messages.success(request,'your message has been sent successfully')
          return redirect ('contact')
    
    else:
        form =ContactForm()
    return render(request,'myportfolio/contact.html',{'form':form})



@staff_member_required
def custom_admin_dashboard(request):
    user_count = User.objects.count()
    project_count = Project.objects.count()
    message_count = Contact.objects.count()
    recent_messages = Contact.objects.order_by('-timestamp')[:5]

    return render(request, 'admin/admin_dashboard.html', {
        'user_count': user_count,
        'project_count': project_count,
        'message_count': message_count,
        'recent_messages': recent_messages,
    })




