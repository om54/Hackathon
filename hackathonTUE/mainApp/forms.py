from .models import Feedback
from django import forms
from django.urls import reverse


class FeedbackForm(forms.ModelForm):
    message = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "class": "w-full bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-48 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out ",
		'rows':4,
		'cols':75
            }),
        label="Feed Back",
    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200'
            }
        )
    )

    class Meta:
        model = Feedback
        fields = ('message', 'name')

    # def get_success_url(self):
    # 	return reverse('/feedback/')
