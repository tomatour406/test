from django.db import models
from django.contrib.auth import get_user, get_user_model
from utils.random_string import random_string_generator

User = get_user_model()

def slug_maker():
    repeat = True
    while repeat:
        new_slug = random_string_generator()
        counter = NippoModel.objects.filter(slug=new_slug).count()
        if counter == 0:
            repeat = False
    return new_slug
    
from django.db.models import Q #インポート
from django.utils import timezone

class NippoModelQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        # qs = qs.filter(public=True) #公開済みの日報のみでQuerySetを作成しています
        if query is not None:
            or_lookup = (
                Q(title__icontains=query)|
                Q(content__icontains=query)            
            )
            qs = qs.filter(or_lookup).distinct()
        return qs.order_by("-date") #新しい順に並び替えてます

class NippoModelManager(models.Manager):
    def get_queryset(self):
        return NippoModelQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
    
class NippoModel(models.Model):
    user = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="タイトル", max_length=100)
    content = models.TextField(verbose_name="本文", max_length=1000)
    public = models.BooleanField(verbose_name="公開する", default=False)
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=20, unique=True, default=slug_maker)
    timestamp = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    
    class Meta:
        verbose_name="日報"
        verbose_name_plural="日報"
        
    objects = NippoModelManager()
    
    def __str__(self):
        return self.title

    def get_profile_page_url(self):
        from django.urls import reverse_lazy
        return reverse_lazy("nippo-list") + f"?profile={self.user.profile.id}"