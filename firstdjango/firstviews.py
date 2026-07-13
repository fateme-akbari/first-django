from django.http import HttpResponse, JsonResponse

def json_views(request):
    return JsonResponse(
        {"name":"Fateme",
            "age": "24"}
    )
    
def http_views(requests):
    return HttpResponse("<h1> this is a test for django</h1>")
    