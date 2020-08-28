from django.shortcuts import render, get_object_or_404

from .models import Obavestenje, Kontakt

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template.defaultfilters import slugify

from django.db.models import Q

from .forms import ObavestenjeModelForm


from django.core.files.storage import FileSystemStorage

from django.urls import reverse_lazy


# Create your views here.

def home_page(request):
	return render(request, 'webapp/home.html',{})


def contact_page(request):

	kontakti = Kontakt.objects.all()
	template_name = "webapp/contact.html"
	context = {"kontakti":kontakti}
	return render(request, 'webapp/contact.html',context)


def about_page(request):
	return render(request, 'webapp/about.html',{})


def finansije_page(request):
	return render(request, 'webapp/finansije.html',{})





#OBAVESTENJA START
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


#Django Forms: Handling form data in the POST
#https://sixfeetup.com/blog/django-form-data-in-post -> check page
def obavestenje_dodaj(request):
	created = False
	form = ObavestenjeModelForm(request.POST or None)
	if form.is_valid():
		uploaded_file = request.FILES.get('dokument')
		obj = form.cleaned_data
		obj = form.save(commit=False)
		obj.slug = slugify(obj.naslov) #mora da se instalira pipenv shell python-slugify
		obj.autor = request.user
		obj.dokument = uploaded_file
		obj.save()
		created = True		
		form = ObavestenjeModelForm()

	template_name = "webapp/dodaj_obavestenje.html"
	context = {"form" : form}
	return render (request, template_name, context)



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES.get['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)










def obavestenje_azuriraj():
	pass

def obavestenje_obrisi():
	pass

#OBAVESTENJA END