# Generated by Django 3.2.15 on 2022-10-04 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0027_alter_person_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="members.department",
                verbose_name="Afdeling",
            ),
        ),
        migrations.AlterField(
            model_name="activityinvite",
            name="activity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="members.activity",
                verbose_name="Aktivitet",
            ),
        ),
        migrations.AlterField(
            model_name="activityparticipant",
            name="activity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="members.activity",
                verbose_name="Aktivitet",
            ),
        ),
        migrations.AlterField(
            model_name="activityparticipant",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="members.member",
                verbose_name="Medlem",
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="members.address",
                verbose_name="Adresse",
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="department_leaders",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"user__is_staff": True},
                to="members.Person",
                verbose_name="Afdelingsledere",
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="members.department",
                verbose_name="Afdeling",
            ),
        ),
        migrations.AlterField(
            model_name="union",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="members.address",
                verbose_name="Adresse",
            ),
        ),
        migrations.AlterField(
            model_name="union",
            name="board_members",
            field=models.ManyToManyField(
                blank=True, to="members.Person", verbose_name="Menige medlemmer"
            ),
        ),
        migrations.AlterField(
            model_name="union",
            name="cashier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="cashier",
                to="members.person",
                verbose_name="Kasserer",
            ),
        ),
        migrations.AlterField(
            model_name="union",
            name="chairman",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="chairman",
                to="members.person",
                verbose_name="Formand",
            ),
        ),
        migrations.AlterField(
            model_name="union",
            name="second_chair",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="second_chair",
                to="members.person",
                verbose_name="Næstformand",
            ),
        ),
        migrations.AlterField(
            model_name="union",
            name="secretary",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="secretary",
                to="members.person",
                verbose_name="Sekretær",
            ),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="members.department",
                verbose_name="Afdeling",
            ),
        ),
        migrations.AlterField(
            model_name="waitinglist",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="members.department",
                verbose_name="Afdeling",
            ),
        ),
    ]
