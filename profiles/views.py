from django.shortcuts import render
from .models import Profile
from .forms import ProfileFrom
from django.http import JsonResponse
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def my_profile_view(request):
    obj = Profile.objects.get(user=request.user)
    form = ProfileFrom(request.POST or None, request.FILES or None, instance = obj)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if form.is_valid():
            instance = form.save()
            return JsonResponse({
                'bio': instance.bio,
                'avatar': instance.avatar.url,
                'user': instance.user.username
            })
    context = {
        'obj' : obj,
        'form' : form,
    }

    return render(request, 'profiles/main.html', context)