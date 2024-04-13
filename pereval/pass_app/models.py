from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False, unique=True, verbose_name='user id')
    email = models.EmailField(unique=True, max_length=255, verbose_name='email')
    fam = models.CharField(max_length=200, verbose_name='surname')
    name = models.CharField(max_length=200, verbose_name='name')
    otc = models.CharField(max_length=200, blank=True, null=True, verbose_name='patronymic')
    phone = models.CharField(max_length=20, verbose_name='phone')


class PerevalAdded(models.Model):
    STATUS = [
        ('new', 'Ожидает модерацию'),
        ('pending', 'Принято на модерацию'),
        ('accepted', 'Модерация пройдена успешно'),
        ('rejected', 'Модерация завершена, отклонено')
    ]

    beauty_title = models.CharField(max_length=200, verbose_name='beauty title')
    title = models.CharField(max_length=200, verbose_name='title')
    other_titles = models.TextField(verbose_name='other titles')
    connect = models.TextField(blank=True, null=True, verbose_name='connect')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='add time')
    user_id = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='user id')
    coords_id = models.ForeignKey('Coords', on_delete=models.PROTECT, verbose_name='coords')
    level_id = models.ForeignKey('Level', on_delete=models.PROTECT, verbose_name='level')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='status', default='new')


class Level(models.Model):
    LEVEL = [
        ('1A', '1А'),
             ('1B', '1Б'),
             ('2A', '2А'),
             ('2B', '2Б'),
             ('3A', '3А'),
             ('3B', '3Б')
    ]
    winter = models.CharField(max_length=2, blank=True, null=True, choices=LEVEL, verbose_name='winter level')
    spring = models.CharField(max_length=2, blank=True, null=True, choices=LEVEL, verbose_name='spring level')
    summer = models.CharField(max_length=2, blank=True, null=True, choices=LEVEL, verbose_name='summer level')
    autumn = models.CharField(max_length=2, blank=True, null=True, choices=LEVEL, verbose_name='autumn level')


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='latitude')
    longitude = models.FloatField(verbose_name='latitude')
    height = models.IntegerField(verbose_name='latitude')


class Image(models.Model):
    image_data = models.URLField(verbose_name='image')
    title = models.CharField(max_length=255, verbose_name='image title')


class PerevalImage(models.Model):
    image_id = models.OneToOneField('Image', on_delete=models.CASCADE)
    pereval_id = models.OneToOneField('PerevalAdded', on_delete=models.CASCADE)
