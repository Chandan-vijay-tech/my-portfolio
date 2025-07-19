from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact

def home(request):
    # 👇 Define the skills list here
    skills = [
        "Python", "Machine Learning", "Deep Learning", "NLP",
        "Power BI", "EDA", "AI", "AI Agents", "LLM",
        "RAG", "HTML", "CSS"
    ]
    return render(request, 'home.html', {'skills': skills})

def contact(request):
    if request.method == "POST":
        print('post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number = request.POST.get('number')
        print(name, email, number, content)

        if len(name) > 1 and len(name) < 30:
            pass
        else:
            messages.error(request, 'Length of name should be greater than 2 and less than 30 words')
            return render(request, 'home.html')

        if len(email) > 1 and len(email) < 30:
            pass
        else:
            messages.error(request, 'Invalid email, try again')
            return render(request, 'home.html')

        if len(number) > 2 and len(number) < 12:
            pass
        else:
            messages.error(request, 'Invalid number, try again')
            return render(request, 'home.html')

        ins = models.Contact(name=name, email=email, content=content, number=number)
        ins.save()
        messages.success(request, 'Thank you for contacting me || your message has been saved')
        print('Data has been saved to database')

    # Also pass the skills here to avoid template errors
    skills = [
        "Python", "Machine Learning", "Deep Learning", "NLP",
        "Power BI", "EDA", "AI", "AI Agents", "LLM",
        "RAG", "HTML", "CSS"
    ]
    return render(request, 'home.html', {'skills': skills})
