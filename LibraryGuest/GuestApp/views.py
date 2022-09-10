from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from GuestApp.models import Book, User
from GuestApp.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from GuestApp.serializer import BookSerializer
from django.template import loader
from GuestApp.forms import *
from django.core.exceptions import ObjectDoesNotExist

# from GuestApp.forms import ReserveForm

# Create your views here.

# 1a. Homepage
def home_page(request):
    return render(request,"homepage.html")


# 2a. Viewing all Books
def viewbooks_site(request):
    book_data = Book.objects.all()
    book_template = loader.get_template("view_books.html")
    context = {"books_data":book_data}
    html_data = book_template.render(context)
    return HttpResponse(html_data)


# 2.c Viewing all Book Reservations
def view_reservation(request):
    user_data = User.objects.all()
    user_template = loader.get_template("reservations.html")
    context = {"users_data":user_data}
    html_data = user_template.render(context)
    return HttpResponse(html_data)

# 2.e All Books REST API
class BookView(APIView):
    def get(self,request):
        book_list = Book.objects.all()
        serializer = BookSerializer(book_list,many=True)
        return Response(serializer.data)
        # book_json = json.dumps([
        #     dict(
        #         id = book.id, title = book.title, isbn = book.isbn, author = book.isbn, available_count = book.av_count
        #     ) for book in book_list
        # ]
        # ) this manual job is easily done by the serializer


# 2b. Creating a book reservation
class ReservationView(CreateView):
    form_class = ReserveBook
    template_name = "reserve_book.html"
    success_url = "/guest/success/"

    def form_valid(self, form):
        self.object = form.save()
        try:
            curr_book = Book.objects.get(isbn=self.object.isbn)
            if curr_book.av_count == 0:
                self.object.status = None
                self.object.save()
                return HttpResponseRedirect("/guest/reserfail/")
            curr_book.av_count -= 1
            curr_book.save()
            self.object.save()
            return HttpResponseRedirect(self.get_success_url()+"?id="+str(self.object.resver_id))
        except ObjectDoesNotExist:
            self.object.status = None
            self.object.save()
            return HttpResponseRedirect("/guest/reserfail/")


# 2d. Reservation Cancellation
def cancellation_view(request):
    if request.method == "POST":
        resver_id = request.POST['resver_id']
        try:
            curr_user = User.objects.get(pk=int(resver_id))
            curr_user.status = False
            curr_book = Book.objects.get(isbn=curr_user.isbn)
            curr_book.av_count += 1
            curr_book.save()
            curr_user.save()
            return HttpResponseRedirect("/guest/cancellation/?id="+str(curr_user.resver_id))
        except ObjectDoesNotExist:
            return HttpResponseRedirect("/guest/cancelfailed/")
    else:
        return render(request,"cancel_reservation.html")

# class GetBookData(APIView):
#     def get(self,request,pk):
#         book_list = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book_list)
#         return Response(serializer.data)


# Success page in case of a successfull Reservation
def success_res(request):
    return render(request,"success_regis.html")

# Reservation Failure view
def reservation_failure(request):
    return render(request,"reserve_failed.html")

# Reservation cancelled confirmation page
def cancelled_reservation(request):
    return render(request,"cancelled_reservation.html")

# Failed Reservation View
def cancellation_failed(request):
    return render(request,"cancel_fail.html")