from django.shortcuts import render
from . models import Books

# Create your views here.
def getAllBooks(request):
    
    #books = select * from books
    #books = selec name price from books
    books = Books.objects.all().values_list('name','price','qty','ratings')
    books1 = Books.objects.filter(name="java").values_list()
    #books2 = Books.objects.filter(price__gte=200).values_list()
    #books2 = Books.objects.filter(price__lte=200).values_list()
    #books2 = Books.objects.filter(name__startswith ='j').values_list()
    #books2 = Books.objects.filter(name__iendswith ='N').values_list()
    #books2 = Books.objects.filter(name__icontains = 'n').values_list()
    # exact ,iexact,contains,icontains,startswith,istartswith,endswith,iendswith
    #books2 = Books.objects.filter(price__range =(120,200)).values_list()
    #books2 = Books.objects.filter(qty__isnull = True).values_list()
    #regex
    #books2 = Books.objects.filter(name__regex = r'^[a-z]').values_list()
    #books2 = Books.objects.filter(name__in = ['java','python']).values_list()
    #books2 = Books.objects.filter(price__gt = 50).order_by('name').values_list()
    #order by desc
    books2 = Books.objects.filter(price__gt=50).order_by('price').values()

    #querySet obejct
    print(books2)
    
    
    return render(request,'book/bookList.html',{'books':books2})
    