from django.views.generic.simple import direct_to_template

def page_not_found(request):
    response = direct_to_template(request, 
                                  "404.html",
                                  {'notification': {'type': 'error',
                                                    'content': 'Sorry, that could not be found'}
                                  })
    response.status_code = 404
    return response

def server_error(request):
    response = direct_to_template(request, 
                                  "500.html", 
                                  {'notification': {'type': 'error',
                                                    'content': 'Sorry, service had an error'}
                                  })
    response.status_code = 500
    return response
