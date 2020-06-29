from django.shortcuts import render, get_object_or_404

from app.models import Announcement


def index(request):
    announcements = Announcement.objects.all()

    context = {
        'announcements': announcements,
    }
    return render(request, 'studybuddy/index.html', context)


def announcement(request, slug):
    announcement = get_object_or_404(Announcement, slug=slug)

    context = {
        'announcement': announcement,
    }

    return render(request, 'studybuddy/group.html', context)
