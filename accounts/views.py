from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate as django_auth, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required


def logout(request):
    django_logout(request)
    response = HttpResponseRedirect(reverse('login'))
    return response


def login(request):

    if request.user.is_authenticated() and request.user.userprofile.profile_complete:
        return HttpResponseRedirect('/')

    if request.method == "POST":
        user = django_auth( username=request.POST.get('username'),
                            password=request.POST.get('password') )
        if user is not None:
            if user.is_active:
                django_login(request, user)
                if not user.userprofile.profile_complete:
                    response = HttpResponseRedirect(reverse('home'))
                else:
                    response = HttpResponseRedirect('/')
                response.delete_cookie('twitter_anywhere_identity')
                return response
            else:
                print "user not active"
        else:
            print "Invalid login"


    return render_to_response('accounts/login.html',
        context_instance=RequestContext(request))