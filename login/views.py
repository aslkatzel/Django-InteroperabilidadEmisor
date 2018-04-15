from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

@csrf_protect    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def index(request):
    return render_to_response(
    'index.html',
    { 'user': request.user }
    )
