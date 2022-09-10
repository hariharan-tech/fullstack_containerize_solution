from django import forms
from GuestApp.models import *

# class ReserveForm(forms.Form):
#     isbn_book = forms.CharField(max_length=40)
#     email_id = forms.CharField(max_length=100)
#     phno_user = forms.IntegerField()
#     guest_user_name = forms.CharField(max_length=100)


class ReserveBook(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReserveBook, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = (
            "name", "mail_id", "phno","isbn"
        )


class CancelReservation(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CancelReservation, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = (
            "mail_id", "phno","resver_id"
        )