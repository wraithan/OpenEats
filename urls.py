from django.conf.urls.defaults import *
from django.conf import settings
from openeats.accounts.forms import ProfileForm
import helpers.signals  #needed to import the signal for when a user is saved their profile is created
from relationships.listeners import attach_relationship_listener
attach_relationship_listener()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^accounts/logout/$', 'accounts.views.logout_page'),
    (r'^accounts/signIn/$', 'accounts.views.signIn_page'),
    (r'^accounts/ajax-signIn/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/ajax_signIn.html',}),
    (r'^accounts/ajax-create/$', 'registration.views.register', {'backend': 'registration.backends.default.DefaultBackend','template_name': 'accounts/ajax_create.html',}),
    (r'^accounts/', include('registration.backends.default.urls')),
    ('^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
    (r'^profiles/', include('profiles.urls')),
    (r'^rosetta/', include('rosetta.urls')),
    (r'^follow/', include('relationships.urls')),
    (r'^friends/', include('friends.urls')),
    (r'^feed/', include('feed.urls')),
    (r'^groups/', include('recipe_groups.urls')),
    (r'^recipe/', include('recipe.urls')),
    (r'^ingredient/', include('ingredient.urls')),
    (r'^list/', include('list.urls')),
    (r'^tags/', include('tags.urls')),
    (r'^search/', include('haystack.urls')),
    (r'^sentry/', include('sentry.web.urls')),
    #(r'^api/', include('contrib.api.urls')), #api is in the testing phase leaving commented out for release
    (r'^$', 'recipe.views.index'),

)



if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        )
