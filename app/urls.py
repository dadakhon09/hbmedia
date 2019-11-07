from django.urls import path
from .views import index, about, blog, contact, portfolio, services, single_blog, send_mail, video_create, \
	content_create, web_create

urlpatterns = [
	path('', index, name='index'),
	path('about/', about, name='about'),
	path('blog/', blog, name='blog'),
	path('contact/', contact, name='contact'),
	path('portfolio/', portfolio, name='portfolio'),
	path('services/', services, name='services'),
	path('web/', web_create, name='web-create'),
	path('content/', content_create, name='content-create'),
	path('video/', video_create, name='video-create'),
	path('single_blog/', single_blog, name='single_blog'),
	path('sendmail/', send_mail, name='sendmail'),
]
