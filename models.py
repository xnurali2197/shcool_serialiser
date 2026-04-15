class School(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
