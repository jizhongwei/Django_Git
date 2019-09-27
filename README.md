# Django_Git
> 这是本人自学Django的一个实例，一步一步安装网上的教程进行学习，很感谢网上的教程。让我能迅速掌握Django开发的基础内容

### Django 视图
> Django的视图是一个个函数，也可以是一个个类，但类需要面向对象的知识，初学阶段我们一般都是先学习函数的形式，这样入门的门槛低，也能为后面的视图类学习打下基础
比如：

views.py
```python
from django.http import HttpResponse

def index(request):
  return HttpResponse("<h2>Welcome to my blog index page!</h2>")
```

urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    ]
```

### Django 模型
> Django中的模型对应就是数据库，使用Django的一大优势就是不用直接或者说几乎不用跟数据库打交道，我们完全可以通过编写models.py文件来定义相关的数据库表，创建数据库表都是通过Django提供的命令来完成。跟数据库的交互也是通过Django封装的数据库API。

比如定义模型类
```
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('-created_time',)
```
> 上面是自定义的一个模型类，里面涉及到很多的知识点
>
> 1、每一个模型类对应到数据库中是一个数据表<br/>
> 2、每一个模型类都要继承models.Model父类<br/>
> 3、模型类中的每一个字段都对应数据表中的一个字段，并且不用的类型体现到数据表中字段的不同类型<br/>
4、字段可以接收不同的参数来控制字段，比如max_length来控制该字段最多只能存储的字符数<br/>
5、ForeignKey表示一对多的关系，意思就是一篇博客只能有一个作者，但是一个作者可以有多篇博客<br/>