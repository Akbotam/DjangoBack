from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class CompanyManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class ReviewManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Company(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    objects = CompanyManager()

    class Meta:
        verbose_name = 'Co  mpany'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return '{}:{}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Review(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=10000)
    publication_date = models.DateTimeField(default=None, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(5)], default=None, null=True)

    objects = ReviewManager()

    def __str__(self):
        #return '{} : {}'.format(self.id, self.title)
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'summary': self.summary,
            'publication date': self.publication_date
        }
