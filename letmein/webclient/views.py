#encoding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import os
from letmein import settings

def index_view(request):		
	return render_to_response('webclient/index.html', context_instance=RequestContext(request))

def registro_view(request):		
	return render_to_response('webclient/registro.html', context_instance=RequestContext(request))