from django.shortcuts import render
import openai


openai.api_key = ""


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


def chatbot_view(request):
    chatbot_response = ""
    if request.method == 'POST':
        question = request.POST.get('question')
        chatbot_response = chatbot(question)
    return render(request, 'index.html', {'chatbot_response': chatbot_response})
