from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils import timezone
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=1,
                                   published_date__lte=timezone.now())

    def lastmod(self, obj):
        return obj.published_date
    
    # Generates the URL for the object's detail page.
    # It does the same job as defining get_absolute_url() on the model,
    # but is implemented as a separate function (e.g., for use in the admin).
    def location(self, item):
        return reverse("blog:single", kwargs={"pid": item.id})