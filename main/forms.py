from django import forms
from .models import Jasoseol, Comment

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label ="제목" 
        self.fields['title'].content ="자기소개서내용" 
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title',
            'placeholder':'제목',
        })

        #class 추가해서 css만지기

    
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)