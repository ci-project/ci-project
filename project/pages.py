from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
import models as projects

def project(request):
    kwargs = {}
    kwargs['name'] = request.GET.get('project', None)
    project = projects.Project.create(**kwargs)
    tasks = projects.Task.findAllFor(project)
    context = {'title' : 'Project Page', 
               'project' : project,
               'tasks' : tasks}
    return direct_to_template(request, "project.html", context)

def task(request): 
    kwargs = {}
    kwargs['name'] = request.POST.get('name', None)
    project = projects.Project.create(**kwargs)
    
    kwargs = {}
    kwargs['parent'] = project
    kwargs['title'] = request.POST.get('title', None)
    kwargs['description'] = request.POST.get('description', None)
    kwargs['notes'] = request.POST.get('notes', [])
    project = projects.Task.create(**kwargs)

    return redirect('/search?project='+'bar')