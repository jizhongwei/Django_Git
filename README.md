# Django_Git
> 这是本人自学Django的一个实例，一步一步安装网上的教程进行学习，很感谢网上的教程。让我能迅速掌握Django开发的基础内容

### Django 视图
> Django的视图是一个个函数，也可以是一个个类，但类需要面向对象的知识，初学阶段我们一般都是先学习函数的形式，这样入门的门槛低，也能为后面的视图类学习打下基础
比如：

```python
from django.http import HttpResponse

def index(request):
  return HttpResponse("<h2>Welcome to my blog index page!</h2>")
```
