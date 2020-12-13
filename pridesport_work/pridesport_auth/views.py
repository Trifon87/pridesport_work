from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import generic as views
from pridesport_work.pridesport_auth.forms.forms import RegisterForm, ProfileForm, LoginForm


from pridesport_work.pridesport_auth.models import UserProfile


class RegisterView(TemplateView):
    template_name = 'auth/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = RegisterForm()
        context['profile_form'] = ProfileForm()
        return context

    @transaction.atomic
    def post(self, request):
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('user profile')

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(request, 'auth/register.html', context)


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'landing page'


def login_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }

        return render(request, 'auth/login.html', context)
    else:
        login_form = LoginForm(request.POST)

        return_url = get_redirect_url(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return render(request, 'auth/user_profile.html')

        context = {
            'login_form': login_form,
        }

        return render(request, 'auth/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('landing page')


class UserProfileView(views.UpdateView):
    template_name = 'auth/user_profile.html'
    form_class = ProfileForm
    model = UserProfile
    success_url = reverse_lazy('user profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        return user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_profile'] = self.get_object().user

        return context

