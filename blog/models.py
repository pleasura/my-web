from django.db import models
from django.utils import timezone
from django.conf import settings
# 在这里创建你的模型
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # 用于定义有限字符长度的文本
    text = models.TextField() # 用于定义无限字符长度的长文本属性
    created_date = models.DateTimeField(default=timezone.now) # 表示日期和时间
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self): # 对象调用时返回标题
        return self.title

    
