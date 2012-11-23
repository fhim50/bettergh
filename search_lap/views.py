from django.shortcuts import get_object_or_404, render_to_response
from search_lap.models import Name
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt


def home(request):
	
    return render_to_response('search_lap/base.html',{})
@csrf_exempt  
def search(request, term):
	search_name=request.POST.get('search_name')
	if (search_name==''):
         
		request.path='search_lap/base.html/'
		
			
		return render_to_response(request.path,{})
		
	else:
		try:
			names = Name.objects.filter(name__iexact= search_name)
			exist = True
			return render_to_response('search_lap/search.html', dict(names = names ,search_name = search_name, exist = exist))	
			
		except ObjectDoesNotExist:
			exist = False
			return render_to_response('search_lap/search.html', dict(names = names ,search_name = search_name, exist = exist))
			
			
			
'''			
argument = 'verify/search.html/'
				exist='True'
				t = loader.get_template(argument)
				c = Context({'posts':posts, 'search_product':search_product,'exist':exist})
				return HttpResponse(t.render(c))
			
			
def search(request, term):
	search_name=request.POST.get('search_name')
	if (search_name==''):
         
		request.path='search_lap/base.html/'
		
			
		return render_to_response(request.path,{})
		
	else:
		try:
			template = 'search_lap/search.html'
			names = Name.objects.filter(name__iexact= search_name)
			exist = True
			loader = loader.get_template(template)
			c = Context({'names': names , 'search_name': search_name, 'exist': exist})
			r
			render_to_response('search_lap/search.html', dict(names = names ,search_name = search_name, exist = exist))	
			
		except ObjectDoesNotExist:
			exist = False
			render_to_response('search_lap/search.html', dict(names = names ,search_name = search_name, exist = exist))
			
			
						
'''