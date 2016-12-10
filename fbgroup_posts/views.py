from django.views.generic.list import ListView
from .models import Post

# Create your views here.


class PostView(ListView):
    model = Post
    template_name = 'fbgroup_posts/posts_list.html'
    paginate_by = 24
