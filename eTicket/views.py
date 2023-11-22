from django.shortcuts import render
from .forms import BookTicketForm

# Create your views here.

def bookticket(request):
	if request.method == 'POST':
		form = BookTicketForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			age = form.cleaned_data['age']
			ticket_type = form.cleaned_data['ticket_type']
			book_date = form.cleaned_data['book_date']
			book_time = form.cleaned_data['book_time']
			number_of_ticket = form.cleaned_data['number_of_ticket']
			print('Name:', name)
			print('Email:', email)
			print('Age:', age)	
			print('Ticket Type:',ticket_type)
			print('Book Date and Time:', book_date, book_time)
			print('Number of Tickets', number_of_ticket)      
	form = BookTicketForm()
	return render(request, "book.html", {'form':form})