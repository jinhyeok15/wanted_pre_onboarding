# Generated by Django 2.1.7 on 2022-04-27 13:57

from django.db import migrations, models
import django.db.models.deletion
import funding.apps.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(max_length=256, null=True)),
                ('price', models.IntegerField()),
                ('target_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'shop_items',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_join', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'shop_participants',
            },
        ),
        migrations.CreateModel(
            name='ShopPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('poster_name', models.CharField(max_length=50)),
                ('final_date', models.CharField(max_length=25, validators=[funding.apps.core.validators.validate_date_component])),
                ('status', models.CharField(default='DONATE', help_text='\n        PURCHASE는 펀딩이 성공적으로 진행되어 상품 준비단계까지 진행된 상태이며, \n        DONATE는 펀딩에 참여하였으나 마감일이 끝나지 않은 상태, \n        CANCEL은 펀딩을 취소한 상태, \n        CLOSE는 펀딩 목표 금액을 넘지 못하여 펀딩이 취소된 상태를 의미한다. \n        결제는 DONATE단계에서 진행되며, CANCEL이 되면 결제 내역이 환불된다.\n    ', max_length=12)),
            ],
            options={
                'db_table': 'shop_posts',
            },
        ),
        migrations.CreateModel(
            name='ShopPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
            options={
                'db_table': 'shop_purchases',
            },
        ),
    ]
