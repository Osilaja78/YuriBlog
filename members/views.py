from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm, CreateProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from blog.models import Profile

# import math, random
# from email.message import EmailMessage
# import ssl, smtplib
# from django.http import HttpResponse

# Create your views here.
class CreateUserView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class EditUserView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name='registration/update_password.html'
    success_url = reverse_lazy('password_success')

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/profile_page.html'

    def get_absolute_url(self):
        return reverse('user_profile', args={self.pk})

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        current_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["current_user"] = current_user
        return context

class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'twitter_url', 'facebook_url', 'instagram_url', 'linkedin_url']
    success_url = reverse_lazy('home')

class CreateProfilePageView(CreateView):
    form_class = CreateProfileForm
    model = Profile
    template_name = 'registration/create_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def PasswordChangeSuccess(request):
    return render(request, 'registration/password_success.html', {})
