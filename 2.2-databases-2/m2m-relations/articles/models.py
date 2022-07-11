from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=50, verbose_name="Раздел")

    class Meta:
        verbose_name = "Раздел"

    def __str__(self):
        return self.tag


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag,blank=True,
                                  verbose_name='Разделы',
                                  through='TagArticleRelation')


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class TagArticleRelation(models.Model):
    cur_tag = models.ForeignKey(Tag,verbose_name='раздел',on_delete=models.CASCADE, related_name='scopes')
    articles = models.ForeignKey(Article, verbose_name='статья',on_delete=models.CASCADE, related_name='scopes')
    main = models.BooleanField(default=False)
