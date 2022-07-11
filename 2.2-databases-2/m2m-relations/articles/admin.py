from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, Tag, TagArticleRelation
from django.forms import BaseInlineFormSet


class AboutScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        selected_topics = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')

            if form.cleaned_data and form.cleaned_data['main']:
                selected_topics += 1

        if selected_topics == 0:
            raise ValidationError('Выберите основной раздел статьи')
        if selected_topics > 1:
            raise ValidationError('Основной раздел может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода



class ArticleTagInline(admin.TabularInline):
    model = TagArticleRelation
    formset = AboutScopeInlineFormset



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','tag']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','text','published_at','image']
    inlines = [ArticleTagInline]


