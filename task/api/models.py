from django.db import models
from datetime import datetime


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}:{}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Reviewer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return '{}:{}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

class Review(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=10000)
    publication_date = models.DateTimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}'.format(self.id, self.title)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'summary': self.summary,
            'publication date': self.publication_date
        }
