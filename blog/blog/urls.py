from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

     url(r'^$', 'articles.views.archive', name='home'),
     url(r'^article/new/', 'articles.views.create_post', name='create_post'),
     url(r'^registration', 'articles.views.create_user', name='create_user'),
     url(r'^authenticate', 'articles.views.authorization', name='authorization'),                  
     #url(r'^$', 'articles.views.archive', name='archive'),
     url(r'^article/(?P<article_id>\d+)$', 'articles.views.get_article', name='get_article'),                  
     #url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
     #url(r'^$', 'articles.views.home', name='home'),
     url(r'^admin/', include(admin.site.urls)),
)
