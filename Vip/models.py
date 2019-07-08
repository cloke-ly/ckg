from django.db import models

# Create your models here.
class Vip1(models.Model):
    name = models.CharField(max_length=16,verbose_name='会员名称')
    level = models.IntegerField(verbose_name='会员等级')
    price = models.FloatField(verbose_name='每月价格')

    class Meta:
        db_table = 'vip'

    def perms(self):
        perm_id_list = VipPermRelation.objects.filter(vip_id=self.id
                                                       ).values_list('perm_id', flat=True)
        return Permission.objects.filter(id__in=perm_id_list)

    def has_perm(self,perm_name):
        for perm in self.perms():
            if perm_name == perm.name:
                return True
        return False

class Permission(models.Model):
    name = models.CharField(max_length=16,unique=True,verbose_name='权限名称')
    desc = models.TextField(verbose_name='权限描述')

    class Meta:
        db_table = 'permission'


class VipPermRelation(models.Model):
    vip_id = models.IntegerField(verbose_name='vip 的id')
    perm_id = models.IntegerField(verbose_name='Permission 的 id')


    class Meta:
        db_table = 'vippermrelstion'

