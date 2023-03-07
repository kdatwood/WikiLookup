import wikipedia
from django.shortcuts import render


def my_view(request):
    # check if the form was submitted
    if request.method == 'POST':
        # get the user's question from the form
        question = request.POST['question']

        # search for the answer on Wikipedia
        wikipedia.set_lang("en")  # set language to English
        page = wikipedia.page(question)
        extract = page.summary

        # pass the extract to the template
        return render(request, 'index.html', {'extract': extract})

    # if the form was not submitted, just render the template
    return render(request, 'index.html')
