# Generated by Django 2.1.3 on 2019-01-06 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_auto_20170820_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orcamentocompra',
            options={'verbose_name': 'Orçamento de Compra'},
        ),
        migrations.AlterModelOptions(
            name='pedidocompra',
            options={'permissions': (('faturar_pedidocompra', 'Pode faturar Pedidos de Compra'),), 'verbose_name': 'Pedido de Compra'},
        ),
        migrations.AlterField(
            model_name='compra',
            name='local_dest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='compra_local_estoque', to='estoque.LocalEstoque'),
        ),
    ]