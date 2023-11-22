from django import forms
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox

# Create your forms here.

select_ticket_type = (
    ("1","VIP"),
    ("2", "Standard"),
)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookTicketForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18,max_value=50)
    ticket_type = forms.CharField(widget=forms.RadioSelect(choices=select_ticket_type))
    book_date = forms.DateTimeField(widget=DateInput)
    book_time = forms.TimeField(widget=TimeInput)
    number_of_ticket = forms.IntegerField(min_value=1,max_value=100)
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)