from django.shortcuts import render, redirect
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

import openai
from dotenv import load_dotenv
import os

# load the environment variables
load_dotenv()

# get the API key from the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


openai.api_key = OPENAI_API_KEY


def chatbot(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


@login_required
def chatbot_view(request):
    chatbot_response = ""
    chatlogs = request.session.get('chatlogs', [])

    if request.method == 'POST':
        question = request.POST.get('question')
        chatbot_response = chatbot(question)
        chatlogs.append({'user': question, 'chatbot': chatbot_response})
        request.session['chatlogs'] = chatlogs

    return render(request, 'index.html', {'chatlogs': chatlogs})


def clear_chatlog(request):
    if 'chatlogs' in request.session:
        del request.session['chatlogs']
    return redirect('chatbot_view')  # Replace 'chatbot_view' with the name of your chatbot_view URL pattern

    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chatbot_view')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})