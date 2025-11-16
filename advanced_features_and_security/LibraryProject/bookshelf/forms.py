from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)

    def clean_query(self):
        q = self.cleaned_data['query']

        return q.strip()
    
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
