from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)

    def clean_query(self):
        q = self.cleaned_data['query']
        return q.strip()
