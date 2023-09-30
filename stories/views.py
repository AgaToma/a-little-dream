from django.views.generic import (CreateView, ListView,
                                  DetailView, DeleteView, UpdateView)
from .forms import StoryForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Story


class StoryList(ListView):
    """View for showing all stories"""
    template_name = 'stories/stories.html'
    model = Story
    context_object_name = 'stories'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            rooms = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(age_match__icontains=query)
            )
        else:
            stories = self.model.objects.all()
        return stories


class StoryDetails(DetailView):
    """View for showing story details"""
    template_name = 'stories/story_details.html'
    model = Story
    context_object_name = 'story'


class AddStory(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    View for adding stories by staff
    """
    model = Story
    form_class = StoryForm
    template_name = 'stories/add_story.html'
    success_url = '/stories/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddStory, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class EditStory(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for editing stories by staff
    """
    template_name = 'stories/edit_story.html'
    model = Story
    form_class = StoryForm
    success_url = '/stories/'

    def test_func(self):
        return self.request.user.is_staff


class DeleteStory(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting stories by staff
    """
    model = Story
    success_url = '/stories/'
    template_name = 'stories/edit_story.html'

    def test_func(self):
        return self.request.user.is_staff
