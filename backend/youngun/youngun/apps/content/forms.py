from django import forms

class QuoteRTForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    imgurl = forms.URLField(label='Image URL', max_length=8000, required=True)