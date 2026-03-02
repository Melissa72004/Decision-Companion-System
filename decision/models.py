from django.db import models

class Decision(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Criteria(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    weight = models.FloatField()

    def __str__(self):
        return self.name


class Option(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Score(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return f"{self.option.name} - {self.criteria.name}"