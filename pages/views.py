from pages.models import Image

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['test'] = Image.objects.all()

        return context


class DownloadImgView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        image_id = kwargs.get('pk')
        image = Image.objects.get(id=image_id)   
        
        image_file = requests.get(image.url)
        # https://stackoverflow.com/questions/26274021/simply-save-file-to-folder-in-django
        # save image_file to media
        # wyswietlic 
        return super().get(request, *args, **kwargs)

#

class AboutPageView(TemplateView):
    template_name = 'about.html'

