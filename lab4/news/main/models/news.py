from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings
from PIL import Image
import os
import uuid
import datetime


IMAGE_W = 640
IMAGE_H = 360

def image_name():
    cfg = {}
    cfg['root'] = 'news'
    cfg['now'] = datetime.datetime.now()
    cfg['rnd'] = uuid.uuid4()
    cfg['ext'] = 'jpg'

    return  '{root}/{now:%Y/%m/%d}/{rnd}.{ext}'.format(**cfg)

class News(models.Model):

    class Meta:
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pubtime']

    title = models.CharField(max_length=50, verbose_name='Заголовок')

    image = models.ImageField(
                              upload_to='temp',
                              verbose_name='Изображение'
                             )

    short_text = models.TextField(verbose_name='Краткое описание')

    text = models.TextField(verbose_name='Тескт')

    pubtime = models.DateTimeField(
                                   auto_now_add=True,
                                   editable=False,
                                   verbose_name='Дата публикации'
                                   )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if News.objects.filter(pk=self.pk).exists():
            try:
                this_record = News.objects.get(pk=self.pk)
                if this_record.image != self.image:
                    this_record.image.delete(save=False)
            except:
                print("WARNING: Can't delete file {}".format(thisself_record.image.path))

        super(News, self).save(*args, **kwargs)

        im = Image.open(self.image.path)
        im = im.resize((IMAGE_W, IMAGE_H))
        new_path = image_name()
        full_path = os.path.join(settings.MEDIA_ROOT, new_path)
        os.makedirs(os.path.split(full_path)[0], exist_ok=True)
        im.save(full_path)
        os.remove(self.image.path)

        self.image.name = new_path
        super(News, self).save(*args, **kwargs)
        print('ok')


    def delete(self, *args, **kwargs):
        try:
            this_record.image.delete(save=False)
        except:
            pass
        super(News, self).delete(*args, **kwargs)
