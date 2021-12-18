from django.db import models


# Create your models here.


class Module(models.Model):
    Module_Type = (
        ("valid", "valid"),
        ("invalid", "invalid")
    )
    name = models.CharField(max_length=150, unique=True, null=True)
    type = models.CharField(max_length=150, choices=Module_Type)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Module"


class Evaluation(models.Model):
    note = models.FloatField(max_length=2 , null=True)
    comment = models.TextField(max_length=250, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Evaluation"


class Session(models.Model):
    Session_Status = (
        ("In_progress", "In progress"),
        ('Completed', 'Completed'),
        ("Canceled", "Canceled"))
    Tools_Type = (('software', 'software'),
                  ("hardware", "hardware"))
    Session_Type = (
        ("Normal", "Normal"),
        ("Catch-up", "Catch-up"),
        ("Support", "Support"),
        ("training", "training")
    )
    start_date = models.DateTimeField(verbose_name="start date", null=True)
    end_date = models.DateTimeField(verbose_name="start date", null=True)
    class_number = models.IntegerField()
    module =  models.ForeignKey(Module ,  null=True , blank =  True , on_delete=models.CASCADE)
    objectif = models.TextField(max_length=150)
    resume = models.TextField(max_length=150)
    status = models.CharField(max_length=100, choices=Session_Status)
    tools = models.CharField(max_length=100, choices=Tools_Type)
    type = models.CharField(max_length=100, choices=Session_Type)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Session"


