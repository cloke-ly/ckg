import datetime

from django.db import models

# Create your models here.
from Social.models import Friend


class User(models.Model):
    '''个人信息'''
    SEX = (
        ('male','男性'),
        ('female','女性'),
        ('unkonwn','不详'),
    )
    LOCATIONS = (
        ('北京','北京'),
        ('上海','上海'),
        ('广州','广州'),
        ('深圳','深圳'),
        ('武汉','武汉'),
        ('南京','南京'),
        ('西安','西安'),
        ('成都','成都'),
        ('重庆','重庆'),
    )
    phonenum = models.CharField(max_length=16,unique=True,verbose_name='手机号')
    nickname = models.CharField(max_length=32,verbose_name='昵称')
    sex = models.CharField(max_length=8,choices=SEX,verbose_name='性别')
    birthday = models.DateField(default=datetime.date(1990,10,1),verbose_name='出生日期')
    avatar = models.CharField(max_length=256,verbose_name='个人形象')
    location = models.CharField(max_length=16,choices=LOCATIONS,verbose_name='常居地')

    vip_id = models.IntegerField(default=0)

    def __str__(self):
        return f'({self.id}:{self.nickname})'

    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile, created = Profile.objects.get_or_create(id=self.id)
        return self._profile



    @property
    def friends(self):
        friend_ids = Friend.my_friends_ids(self.id)
        return User.objects.filter(id__in=friend_ids)

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum':self.phonenum,
            'nickname':self.nickname,
            'sex':self.sex,
            'birthday':str(self.birthday),
            'avatar':self.avatar,
            'location':self.location,
        }

    class Meta:
        db_table = 'user'

class Profile(models.Model):
    '''个人交友资料及客户端配置'''
    dating_sex = models.CharField(max_length=18,choices=User.SEX)
    dating_location = models.CharField(max_length=16,choices=User.LOCATIONS)
    min_distance = models.IntegerField(default=1)
    max_distance = models.IntegerField(default=10)
    min_dating_age = models.IntegerField(default=16)
    max_dating_age = models.IntegerField(default=45)
    vibration = models.BooleanField(default=True)
    only_matche = models.BooleanField(default=True)
    auto_play = models.BooleanField(default=True)

    def to_dict(self):
        return{
            'dating_sex':self.dating_sex,
            'dating_location':self.dating_location,
            'min_distance':self.min_distance,
            'max_distance':self.max_distance,
            'min_dating_age':self.min_dating_age,
            'max_dating_age':self.max_dating_age,
            'vibration':self.vibration,
            'only_matche':self.only_matche,
            'auto_play':self.auto_play
        }
    class Meta:
        db_table = 'profile'