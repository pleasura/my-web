from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post) # 通过这行代码，我们的模型将在 admin 网站上可见。