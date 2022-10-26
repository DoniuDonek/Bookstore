from django.test import TestCase
from pages.models import Image


class TestImage(TestCase):
    # given
    # when
    # then

    def test_image_model_has_str_method(self):
        # given
        image_model = Image.objects.create(name="my_image", url="http://test.com/image.jpg")
        image_model2 = Image.objects.create(name="test_img_2", url="http://test111111.com/image.jpg")

        # then
        self.assertEqual(str(image_model), "Name: my_image, url: http://test.com/image.jpg")
        self.assertEqual(str(image_model2), "Name: test_img_2, url: http://test111111.com/image.jpg")

    # def test_raises_error_when_trying_to_add_img_without_url(self)

