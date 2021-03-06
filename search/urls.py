from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from search import views, apis

urlpatterns = [url(r'^$',
                 views.search, name='index'),
             url(r'^autocomplete$',
                 views.autocomplete, name='autocomplete'),
             url(r'^search',
                 views.search_list, name='search'),
             url(r'^browse',
                 views.browse, name='browse'),
             url(r'^feedback',
                 views.feedback, name='feedback'),

             url(r'^tag/(?P<handle>.+)/$',
                 views.tag, name='tag'),
             url(r'^person/(?P<pk>\d+)/$',
                 views.person, name='person'),

             # Infos
             url(r'^information/(?P<pk>\d+)/$',
                 views.InformationView.as_view(), name='info'),
             url(r'^event/(?P<pk>\d+)/$',
                 views.EventView.as_view(), name='info'),
             url(r'^project/(?P<pk>\d+)/$',
                 views.ProjectView.as_view(), name='info'),
             url(r'^goodpractice/(?P<pk>\d+)/$',
                 views.GoodPracticeView.as_view(), name='goodpractice'),
             url(r'^glossary/(?P<pk>\d+)/$',
                 views.GlossaryView.as_view(), name='glossary'),
             url(r'^question/(?P<pk>\d+)/$',
                 views.QuestionView.as_view(), name='question'),

             url(r'^loadquestionform$',
                 views.loadquestionform, name='loadquestionform'),
             url(r'^submitquestion$',
                 views.submitquestion, name='submitquestion'),
             url(r'^comment$',
                 views.comment, name='comment'),
             url(r'^vote$',
                 views.cast_vote, name='cast_vote'),
             url(r'^api/comment$',
                 apis.comment, name='api_comment'),

             url(r'^login',
                 views.login_user, name='login'),
             url(r'^logout',
                 views.logout_user, name='logout'),
             url(r'ivoauth_debug$',
                 views.ivoauth_debug, name='ivoauth_debug'),
             url(r'ivoauth/debug_callback',
                 views.ivoauth_debug_callback, name='ivoauth_debug_callback'),
             url(r'ivoauth/callback',
                 views.ivoauth_callback, name='ivoauth_callback'),
             url(r'ivoauth$',
                 views.ivoauth, name='ivoauth'),
]
