from django import forms
from .models import Product, Comment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'school', 'subject', 'grade', 'is_free', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # 설명을 위한 텍스트 영역
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']  # 모델 필드 이름과 일치해야 합니다
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # 댓글 텍스트 영역
        }
        
    # 필드 레이블을 변경하여 '이름'과 '내용'으로 표시
    name = forms.CharField(label='이름', widget=forms.TextInput(attrs={'placeholder': '이름을 입력하세요', 'class': 'form-control'}))
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={'placeholder': '댓글 내용을 입력하세요', 'class': 'form-control', 'rows': 4, 'cols': 40}))
