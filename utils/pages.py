from django.views.generic.simple import direct_to_template

def welcome(request):
    context = dict(title = 'Homepage')
    return direct_to_template(request, "welcome.html", context)