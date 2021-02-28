from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    category_name = models.ForeignKey(Category, related_name='courses_category', on_delete=models.CASCADE)
    subcategory_name = models.ForeignKey(Category, related_name='courses_subcategory', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name='courses_level', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    real_price = models.FloatField()
    price = models.FloatField()
    discount = models.IntegerField()
    course_score = models.FloatField()
    users = models.IntegerField()
    def __str__(self):
        return self.name

