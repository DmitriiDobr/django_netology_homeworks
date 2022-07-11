from django.contrib import admin

from .models import Article, Tag, TagArticleRelation

class ArticleTagInline(admin.TabularInline):
    model = TagArticleRelation


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','tag']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','text','published_at','image']
    inlines = [ArticleTagInline]


