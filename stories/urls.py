from django.urls import path
from .views import AddStory, StoryList, StoryDetails, DeleteStory, EditStory


urlpatterns = [
    path('add/', AddStory.as_view(), name='add_story'),
    path('', StoryList.as_view(), name='stories'),
    path("<slug:pk>/", StoryDetails.as_view(), name='story_details'),
    path('delete/<slug:pk>/', DeleteStory.as_view(), name='delete_story'),
    path('edit/<slug:pk>/', EditStory.as_view(), name='edit_story')
]
