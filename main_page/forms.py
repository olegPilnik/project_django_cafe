from django import forms
from .models import Booking, Client

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('ful_name', 'email', 'phone', 'date', 'time', 'of_people', 'message')
        widgets = {
            'ful_name': forms.TextInput(attrs={'placeholder': 'Your Name',
                                           'class': 'form-control',
                                           'data-msg': 'Please enter at least 4 chars',
                                           'data-rule': 'minlen:4',
                                           'id': 'name'
                                           }),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'phone',
                                            'placeholder': 'Your Phone'}),
            
            'date': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'date',
                                           'placeholder': 'Date'}),
            'time': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'time',
                                           'placeholder': 'Time'}),
            'of_people': forms.NumberInput(attrs={'class': 'form-control',
                                               'id': 'of_people',
                                               'placeholder': '# of people'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'id': 'message',
                                             'rows': '5',
                                             'placeholder': 'Message'}),
        }



class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('full_name', 'email', 'subject', 'message')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your Name',
                                           'class': 'form-control',
                                           'data-msg': 'Please enter at least 4 chars',
                                           'data-rule': 'minlen:4',
                                           'id': 'name'
                                           }),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'subject',
                                            'placeholder': 'Subject'}),
                       
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'id': 'message',
                                             'rows': '5',
                                             'placeholder': 'Message'}),
        }
