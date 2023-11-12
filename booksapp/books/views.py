from django.shortcuts import render,redirect
from books.forms import BookForm

# Create your views here.
from django.views.generic import View
from books.models import Book
class IndexView(View):
    def get(self,request,*args,**kwargs):
        print("index")
        return render(request,"index.html")
    
class BookListView(View): 
    def get(self,request,*args,**kwargs):
        qs=Book.objects.all()
        return render(request,"book_list.html",{"data":qs})

 #localhost/books/id=2   
class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,"book_detail.html",{"data":qs})
    
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.filter(id=id).delete()
        return redirect("books-all")

class BookAddView(View):
    def get(self,request,*args,**kwargs):
        form=BookForm()
        return render(request,"book_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books-all")
        else:
            return render(request,"book_add.html",{"form":form})
    
    

    
# class BookUpdateView(View):
#     def get(self,request,*args,**kwargs):
#         print("update books")
#         return render(request,"book_update.html")
