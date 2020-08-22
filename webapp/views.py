from django.shortcuts import render, get_object_or_404

from .models import Obavestenje

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.db.models import Q

# Create your views here.

def home_page(request):
	return render(request, 'webapp/home.html',{})


def contact_page(request):
	return render(request, 'webapp/contact.html',{})


def about_page(request):
	return render(request, 'webapp/about.html',{})



def obavestenja_page(request):


	search_query = request.GET.get('text_search', '')

	if search_query:

		object_list = Obavestenje.objects.filter(Q(naslov__icontains=search_query) |
			Q(sadrzaj__icontains=search_query))
	else:

		object_list = Obavestenje.objects.all()

	paginator = Paginator(object_list, 6)
	page = request.GET.get('page')
	try:
		obavestenja = paginator.page(page)

	except PageNotAnInteger:
		# If page is not an integer deliver the first page
		obavestenja = paginator.page(1)

	except EmptyPage:
		# If page is out of range deliver last page of results
		obavestenja = paginator.page(paginator.num_pages)


	template_name = 'webapp/obavestenja.html'
	context = {'page': 'page', 'obavestenja' : obavestenja}
	return render(request, template_name, context)






def obavestenje_detalji(request, year, month, day, obavestenje ):
	obavestenje = get_object_or_404(Obavestenje, slug=obavestenje,
												status='objavljen',
												datum_objave__year=year,
												datum_objave__month=month,
												datum_objave__day=day)
	template_name = "webapp/obavestenje_detalji.html"
	context = {'obavestenje':obavestenje}
	return render(request, template_name, context)




