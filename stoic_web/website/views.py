import random
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin
from website.models import Blog, Event, Programme, Video

class IndexView(TemplateView):
	template_name = 'index.html'

class BlogListView(ListView):
    model=Blog
    template_name = 'blog_list.html'
    context_object_name='post_list'
    paginate_by=5

class EventListView(ListView):
    model=Event
    template_name = 'event_list.html'
    context_object_name='post_list'
    paginate_by=5

class ProgrammeListView(ListView):
    model=Programme
    template_name= 'programme_list.html'
    

class VideoListView(ListView):
    model=Video
    template_name='video_list.html'
    paginate_by=10

class VideoGenreList(VideoListView):
    pass
class VideoIndex(ListView):
    model=Video
    template_name='video_index.html'
    paginate_by=12

    def get_context_data(self, **kwargs):
         # Call the base implementation first to get a context
         context = super(VideoIndex, self).get_context_data(**kwargs)
         # Add QuerySet of several featured videos
         # TODO ADD cached variable to enable dynamic changes to number of videos in admin
         featured=list( Video.objects.filter(featured=True) )
         random.shuffle(featured)

         context['feat_videos'] = featured[:5]
         return context

class VideoDetailView( DetailView):
    model=Video
    template_name='video_detail.html'

    slug_field='youtube_id'


