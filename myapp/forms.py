from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from .models import Comment
from .models import Blog

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Email')
    rate_site = forms.ChoiceField(label='Оцените сайт',
                                  choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'),
                                           (1, 'Очень плохо')], widget=forms.RadioSelect)
    sites = forms.ChoiceField(label='Оцените по сравнению с другими сайтами',
                              choices=[(1, 'Лучше других'), (2, 'Как большинство'), (3, 'Хуже других')],
                              widget=forms.Select)
    feedback = forms.CharField(label='Ваш отзыв', widget=forms.Textarea)

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Пароль'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {"text": "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "description", "content", "image",)
        labels = {"title": "Заголовок", "description": "Краткое содержание", "content": "Полное содержание",
                  "image": "Картинка"}
