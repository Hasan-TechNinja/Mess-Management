from django.shortcuts import render
from django.views import View
from . models import TransactionType
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

class TransactionTypeView(View):
    def post(self, request):
        title = TransactionType.title()
        description = TransactionType.description()
        if title.is_valid():
            title.save()
        elif description.is_valid():
            description.save()
            messages.success(request, "Success!")
        return render(request, 'Home/transactiontype.html', {'title': title}, {'description': description})