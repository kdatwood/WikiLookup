import requests
from django.shortcuts import render


def my_view(request):
    # check if the form was submitted
    if request.method == 'POST':
        # get the user's question from the form
        question = request.POST['question']

        # set up the parameters for the API request
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "titles": question,
            "exsentences": 3,
            "explaintext": True,
        }

        # make the API request
        response = requests.get(
            "https://en.wikipedia.org/w/api.php", params=params)

        # get the page content from the API response
        page_content = response.json()["query"]["pages"]

        # extract the page's extract
        for page_id in page_content:
            extract = page_content[page_id]["extract"]

        # pass the extract to the template
        return render(request, 'index.html', {'extract': extract})

    # if the form was not submitted, just render the template
    return render(request, 'index.html')
