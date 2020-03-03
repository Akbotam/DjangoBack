from django.test import TestCase
from api.models import Review
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse




# models test
class ReviewTest(TestCase):

    def create_review(self, title="only a test", summary="yes, this is only a test"):
        return Review.objects.create(title=title, summary=summary, publication_date=timezone.now())

    def test_review_creation(self):
        r = self.create_review()
        self.assertTrue(isinstance(r, Review))
        self.assertEqual(str(r), r.title)

#views (uses reverse)

    def setUp(self):
        self.user = User(username="akbota", email="akbota@gmail.com")
        password = 'some_password'
        self.user.set_password(password)
        self.user.save()

        self.client = APIClient()
        self.client.login(username=self.user.username, email=self.user.email, password=password)

    def test_review_list_view(self):
        r = self.create_review()
        url = reverse("review.views.ReviewList")
        resp = self.client.get(url, format='json')

        self.assertEqual(resp.status_code, 200)
       # self.assertIn(r.title, resp.content)


