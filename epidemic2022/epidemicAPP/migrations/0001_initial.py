# Generated by Django 4.1.3 on 2022-11-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="China_epidemic_TB",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Counity_name", models.CharField(max_length=50, verbose_name="国家名称")),
                ("nowConfirm", models.IntegerField(default=0, verbose_name="当前确诊人数")),
                ("confirm", models.IntegerField(default=0, verbose_name="累计确诊人数")),
                ("confirm_add", models.IntegerField(default=0, verbose_name="新增确诊人数")),
                ("dead", models.IntegerField(default=0, verbose_name="死亡人数")),
                ("heal", models.IntegerField(default=0, verbose_name="痊愈人数")),
                (
                    "highRiskAreaNum",
                    models.IntegerField(default=0, verbose_name="高风险地区"),
                ),
                ("wzz_add", models.IntegerField(default=0, verbose_name="新增无症状")),
                ("wzz", models.IntegerField(default=0, verbose_name="无症状数量")),
                ("mtime", models.CharField(max_length=50, verbose_name="更新时间")),
                ("dead_add", models.IntegerField(default=0, verbose_name="新增死亡人数")),
                (
                    "mediumRiskAreaNum",
                    models.IntegerField(default=0, verbose_name="中风险地区"),
                ),
                (
                    "local_confirm_add",
                    models.IntegerField(default=0, verbose_name="本地新增"),
                ),
                ("abroad_confirm", models.IntegerField(default=0, verbose_name="境外输入")),
                ("local_confirm", models.IntegerField(default=0, verbose_name="本地确诊")),
                ("localWzzAdd", models.IntegerField(default=0, verbose_name="本地无症状新增")),
            ],
            options={"db_table": "China_epidemic_TB",},
        ),
        migrations.CreateModel(
            name="City_epidemic_TB",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("City_name", models.CharField(max_length=50, verbose_name="城市名称")),
                ("Pname", models.CharField(max_length=50, verbose_name="省份名称")),
                ("nowConfirm", models.IntegerField(default=0, verbose_name="当前确诊人数")),
                ("confirm", models.IntegerField(default=0, verbose_name="累计确诊人数")),
                ("confirm_add", models.IntegerField(default=0, verbose_name="新增确诊人数")),
                ("dead", models.IntegerField(default=0, verbose_name="死亡人数")),
                ("heal", models.IntegerField(default=0, verbose_name="痊愈人数")),
                ("City_adcode", models.CharField(max_length=50, verbose_name="城市编码")),
                (
                    "highRiskAreaNum",
                    models.IntegerField(default=0, verbose_name="高风险地区"),
                ),
                ("wzz_add", models.IntegerField(default=0, verbose_name="新增无症状")),
                ("wzz", models.IntegerField(default=0, verbose_name="无症状数量")),
                ("mtime", models.CharField(max_length=50, verbose_name="更新时间")),
                (
                    "mediumRiskAreaNum",
                    models.IntegerField(default=0, verbose_name="中风险地区"),
                ),
            ],
            options={"db_table": "City_epidemic_TB",},
        ),
        migrations.CreateModel(
            name="Province_epidemic_TB",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Provinc_name", models.CharField(max_length=50, verbose_name="省份名称")),
                ("nowConfirm", models.IntegerField(default=0, verbose_name="当前确诊人数")),
                ("confirm", models.IntegerField(default=0, verbose_name="累计确诊人数")),
                ("confirm_add", models.IntegerField(default=0, verbose_name="新增确诊人数")),
                ("dead", models.IntegerField(default=0, verbose_name="死亡人数")),
                ("dead_add", models.IntegerField(default=0, verbose_name="新增死亡人数")),
                ("heal", models.IntegerField(default=0, verbose_name="痊愈人数")),
                (
                    "Provinc_adcode",
                    models.CharField(max_length=50, verbose_name="城市编码"),
                ),
                (
                    "highRiskAreaNum",
                    models.IntegerField(default=0, verbose_name="高风险地区"),
                ),
                ("wzz_add", models.IntegerField(default=0, verbose_name="新增无症状")),
                ("wzz", models.IntegerField(default=0, verbose_name="无症状数量")),
                ("mtime", models.CharField(max_length=50, verbose_name="更新时间")),
                (
                    "mediumRiskAreaNum",
                    models.IntegerField(default=0, verbose_name="中风险地区"),
                ),
                (
                    "local_confirm_add",
                    models.IntegerField(default=0, verbose_name="本地新增"),
                ),
                (
                    "abroad_confirm_add",
                    models.IntegerField(default=0, verbose_name="境外新增"),
                ),
            ],
            options={"db_table": "Province_epidemic_TB",},
        ),
    ]