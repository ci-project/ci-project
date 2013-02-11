from google.appengine.ext import db

class Project(db.Model):
    name = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
            
    @classmethod
    def create(cls, **kwargs):
        kwargs['name'] = kwargs.get('name', None)
        project = cls.all().filter('name =', kwargs['name']).get()
        if (project):
            return project
        else:
            project = cls(**kwargs)
        project.put()
        return project
    
class Task(db.Model):
    title = db.StringProperty(required=True)
    description = db.StringProperty(required=True)
    notes = db.StringListProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def create(cls, **kwargs):
        kwargs['parent'] = kwargs.get('parent', None)
        if (not kwargs['parent']):
            return None
        kwargs['title'] = kwargs.get('title', None)
        kwargs['description'] = kwargs.get('description', None)
        kwargs['notes'] = kwargs.get('notes', [])
       
        task = cls(**kwargs)
        task.put()
        return task

    @classmethod
    def findAllFor(cls, parent):
        return cls.all().ancestor(parent).fetch(150)
    
    def getParent(self):
        return self.key.parent().get()