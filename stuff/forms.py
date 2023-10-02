from .models import Comment,CartItem
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']