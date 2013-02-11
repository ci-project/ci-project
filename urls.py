from django.conf.urls.defaults import patterns, url

handler404 = 'utils.error_handlers.page_not_found'
handler500 = 'utils.error_handlers.server_error'

urlpatterns = patterns('')

urlpatterns += patterns(
    'project.pages',
    url(r'^search?', 'project'),
    url(r'^task?', 'task'),
    )

urlpatterns += patterns(
    'utils.pages',
    url(r'^/?', 'welcome'),    
    )