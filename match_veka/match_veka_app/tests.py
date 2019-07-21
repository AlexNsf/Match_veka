from django.test import TestCase, Client


class HtmlStatusTest(TestCase):
    list_of_pages = ['', '/schedule/', '/news/', '/photo/', '/video/', '/history/', '/reg_form/']

    def setUp(self):
        self.client = Client()

    def test_details(self):
        for page in HtmlStatusTest.list_of_pages:
            response = self.client.get(page)
            self.assertEqual(response.status_code, 200)
