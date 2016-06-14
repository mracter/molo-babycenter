from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from molo.core.tests.base import MoloTestCaseMixin

from molo.core.models import SiteLanguage


class RegistrationViewTest(TestCase, MoloTestCaseMixin):

    def setUp(self):
        self.client = Client()
        # Creates Main language
        self.english = SiteLanguage.objects.create(
            locale='en',
        )
        self.mk_main()

        # Creates a section under the index page
        self.english_section = self.mk_section(
            self.section_index, title='English section')
        for i in range(200):
            self.mk_article(
                self.english_section, title=str(i))

    def test_first_page_pagination(self):
        response = self.client.get('/sections/english-section/')

        self.assertNotContains(response, 'Prev')
        self.assertContains(response, '<a href="?p=2">2</a>')
        self.assertContains(response, '<a href="?p=3">3</a>')
        self.assertContains(response, '...')
        self.assertContains(response, '<a href="?p=15">15</a>')
        self.assertContains(response, '<a href="?p=16">16</a>')
        self.assertContains(response, 'Next')

    def test_second_page_pagination(self):
        response = self.client.get('/sections/english-section/?p=2')
        self.assertContains(response, 'Prev')
        self.assertContains(response, '<a href="?p=1">1</a>')
        self.assertContains(response, '<a href="?p=3">3</a>')
        self.assertContains(response, '<a href="?p=4">4</a>')
        self.assertContains(response, '...')
        self.assertContains(response, '<a href="?p=15">15</a>')
        self.assertContains(response, '<a href="?p=16">16</a>')
        self.assertContains(response, 'Next')

    def test_third_page_pagination(self):
        response = self.client.get('/sections/english-section/?p=3')
        self.assertContains(response, 'Prev')
        self.assertContains(response, '<a href="?p=1">1</a>')
        self.assertContains(response, '<a href="?p=2">2</a>')
        self.assertContains(response, '<a href="?p=4">4</a>')
        self.assertContains(response, '<a href="?p=5">5</a>')
        self.assertContains(response, '...')
        self.assertContains(response, '<a href="?p=15">15</a>')
        self.assertContains(response, '<a href="?p=16">16</a>')
        self.assertContains(response, 'Next')


    def test_fifth_page_pagination(self):
        response = self.client.get('/sections/english-section/?p=5')
        self.assertContains(response, 'Prev')
        self.assertContains(response, '<a href="?p=1">1</a>')
        self.assertContains(response, '<a href="?p=2">2</a>')
        self.assertContains(response, '...')
        self.assertContains(response, '<a href="?p=3">3</a>')
        self.assertContains(response, '<a href="?p=4">4</a>')
        self.assertContains(response, '<a href="?p=6">6</a>')
        self.assertContains(response, '<a href="?p=7">7</a>')
        self.assertContains(response, '...')
        self.assertContains(response, '<a href="?p=15">15</a>')
        self.assertContains(response, '<a href="?p=16">16</a>')
        self.assertContains(response, 'Next')

    def test_fourteenth_page_pagination(self):
        response = self.client.get('/sections/english-section/?p=14')
        self.assertContains(response, 'Prev')
        self.assertContains(response, '<a href="?p=1">1</a>')
        self.assertContains(response, '<a href="?p=2">2</a>')
        self.assertContains(response, '...')
        self.assertContains(response, '<a href="?p=12">12</a>')
        self.assertContains(response, '<a href="?p=13">13</a>')
        self.assertContains(response, '<a href="?p=15">15</a>')
        self.assertContains(response, '<a href="?p=16">16</a>')
        self.assertContains(response, 'Next')

    def test_fifteenth_page_pagination(self):
        response = self.client.get('/sections/english-section/?p=15')
        self.assertContains(response, 'Prev')
        self.assertContains(response, '<a href="?p=1">1</a>')
        self.assertContains(response, '<a href="?p=2">2</a>')
        self.assertContains(response, '...')
        self.assertContains(response, '<a href="?p=13">13</a>')
        self.assertContains(response, '<a href="?p=14">14</a>')
        self.assertContains(response, '<a href="?p=16">16</a>')
        self.assertContains(response, 'Next')

    def test_sixteenth_page_pagination(self):
        response = self.client.get('/sections/english-section/?p=16')
        self.assertContains(response, 'Prev')
        self.assertContains(response, '<a href="?p=1">1</a>')
        self.assertContains(response, '<a href="?p=2">2</a>')
        self.assertContains(response, '...')
        self.assertContains(response, '<a href="?p=14">14</a>')
        self.assertContains(response, '<a href="?p=15">15</a>')
        self.assertNotContains(response, 'Next')
