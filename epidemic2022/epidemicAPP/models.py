from django.db import models

# Create your models here.
class China_epidemic_TB(models.Model):
    Counity_name=models.CharField('国家名称',max_length=50)
    nowConfirm=models.IntegerField('当前确诊人数',default=0)
    confirm=models.IntegerField('累计确诊人数',default=0)
    confirm_add=models.IntegerField('新增确诊人数',default=0)
    dead=models.IntegerField('死亡人数',default=0)
    heal=models.IntegerField('痊愈人数',default=0)
    highRiskAreaNum=models.IntegerField('高风险地区',default=0)
    wzz_add=models.IntegerField('新增无症状',default=0)
    wzz=models.IntegerField('无症状数量',default=0)
    mtime=models.CharField('更新时间',max_length=50)
    dead_add = models.IntegerField('新增死亡人数', default=0)
    mediumRiskAreaNum=models.IntegerField('中风险地区',default=0)
    local_confirm_add=models.IntegerField('本地新增',default=0)
    abroad_confirm=models.IntegerField('境外输入',default=0)
    local_confirm=models.IntegerField('本地确诊',default=0)
    localWzzAdd=models.IntegerField('本地无症状新增',default=0)
    class Meta:
        db_table = 'China_epidemic_TB'
    def todict(self):
        return {
            'id': self.id,
            'Counity_name': self.Counity_name,
            'nowConfirm':self.nowConfirm,
            "confirm": self.confirm,
            "confirm_add": self.confirm_add,
            "dead": self.dead,
            "heal": self.heal,
            "highRiskAreaNum": self.highRiskAreaNum,
            "wzz_add": self.wzz_add,
            "wzz": self.wzz,
            "mtime": self.mtime,
            "dead_add": self.dead_add,
            "mediumRiskAreaNum": self.mediumRiskAreaNum,
            "local_confirm_add": self.local_confirm_add,
            'abroad_confirm':self.abroad_confirm,
            'local_confirm':self.local_confirm,
            'localWzzAdd': self.localWzzAdd
        }

class City_epidemic_TB(models.Model):
    City_name=models.CharField('城市名称',max_length=50)
    Pname=models.CharField('省份名称',max_length=50)
    nowConfirm=models.IntegerField('当前确诊人数',default=0)
    confirm=models.IntegerField('累计确诊人数',default=0)
    confirm_add=models.IntegerField('新增确诊人数',default=0)
    dead=models.IntegerField('死亡人数',default=0)
    heal=models.IntegerField('痊愈人数',default=0)
    City_adcode=models.CharField('城市编码',max_length=50)
    highRiskAreaNum=models.IntegerField('高风险地区',default=0)
    wzz_add=models.IntegerField('新增无症状',default=0)
    wzz=models.IntegerField('无症状数量',default=0)
    mtime=models.CharField('更新时间',max_length=50)
    mediumRiskAreaNum=models.IntegerField('中风险地区',default=0)
    class Meta:
        db_table = 'City_epidemic_TB'
    def todict(self):

        return {
            'id':self.id,
            '城市名称':self.City_name,
            '省份名称':self.Pname,
            "新增确诊人数":self.confirm_add,
            "当前确诊人数":self.nowConfirm,
            "累计确诊人数":self.confirm,
            "死亡人数":self.dead,
            "痊愈人数":self.heal,
            "城市编码":self.City_adcode,
            "高风险地区":self.highRiskAreaNum,
            "新增无症状":self.wzz_add,
            "无症状数量":self.wzz,
            "更新时间":self.mtime,
            "中风险地区":self.mediumRiskAreaNum
        }



class Province_epidemic_TB(models.Model):
    Provinc_name=models.CharField('省份名称',max_length=50)
    nowConfirm=models.IntegerField('当前确诊人数',default=0)
    confirm=models.IntegerField('累计确诊人数',default=0)
    confirm_add=models.IntegerField('新增确诊人数',default=0)
    dead=models.IntegerField('死亡人数',default=0)
    dead_add = models.IntegerField('新增死亡人数',default=0)
    heal=models.IntegerField('痊愈人数',default=0)
    Provinc_adcode=models.CharField('城市编码',max_length=50)
    highRiskAreaNum=models.IntegerField('高风险地区',default=0)
    wzz_add=models.IntegerField('新增无症状',default=0)
    wzz=models.IntegerField('无症状数量',default=0)
    mtime=models.CharField('更新时间',max_length=50)
    mediumRiskAreaNum=models.IntegerField('中风险地区',default=0)
    local_confirm_add=models.IntegerField('本地新增',default=0)
    abroad_confirm_add=models.IntegerField('境外新增',default=0)
    class Meta:
        db_table = 'Province_epidemic_TB'


    def todict(self):
        return {
            'id': self.id,
            '省份名称': self.Provinc_name,
            '新增死亡人数':self.dead_add,
            "新增确诊人数": self.confirm_add,
            "当前确诊人数": self.nowConfirm,
            "累计确诊人数": self.confirm,
            "死亡人数": self.dead,
            "痊愈人数": self.heal,
            "城市编码": self.Provinc_adcode,
            "高风险地区": self.highRiskAreaNum,
            "新增无症状": self.wzz_add,
            "无症状数量": self.wzz,
            "更新时间": self.mtime,
            "中风险地区": self.mediumRiskAreaNum,
            '本地新增':self.local_confirm_add,
            '境外新增':self.abroad_confirm_add
        }