import json
from json import JSONDecodeError

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import (
    HttpRequest,
    HttpResponse,
)

@csrf_exempt
def testing_webhook(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        print("Headers: ",request.headers)
        body = request.body.decode("utf-8")
        print("Body: ", body)
        try:
            json_body = json.loads(body)
            print("JSON Body: ", json_body)
        except JSONDecodeError:
            print("Error decoding JSON, the payload might be empty.")
            response = HttpResponse('Error 500')
            response.status_code = 500
            return response

    response = HttpResponse('OK')
    response.status_code = 200
    return response
