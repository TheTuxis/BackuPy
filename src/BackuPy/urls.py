from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BackuPy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^main/$', 'apps.backup.views.main'),
    url(
        r'^list_backup/$',
        'apps.backup.views.list_backup'
    ),
    url(
        r'^detail_backup/(?P<id_backup>\d+)/$',
        'apps.backup.views.list_files'
    ),
    url(
        r'^download/(?P<id_backup>\d+)/(?P<name_file>.*)/$',
        'apps.backup.views.download_backup'
    ),
)

urlpatterns += staticfiles_urlpatterns()