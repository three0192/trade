from django.contrib import admin
from .models import Product, Comment

# Product와 Comment 모델 등록
admin.site.register(Product)
admin.site.register(Comment)
