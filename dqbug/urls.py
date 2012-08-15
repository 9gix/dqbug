from django.conf.urls import patterns, include, url
from django.contrib import admin
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^comments/', include('django.contrib.comments.urls')),
)

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

urlpatterns += patterns('django.contrib.sitemaps.views',
            url(r'^sitemap.xml$', 'index',
                {'sitemaps': sitemaps}),
            url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
                {'sitemaps': sitemaps}),)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)
