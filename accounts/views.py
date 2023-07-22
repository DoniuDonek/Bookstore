from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class DashboardView(LoginRequiredMixin, DetailView):
    model = get_user_model() 
    template_name = 'account/dashboard.html'
    context_object_name = 'user_detail'

    def get_object(self, queryset=None):
        return self.request.user  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.request.user.books.all()  
        context['reviews'] = self.request.user.reviews.all()  
        return context