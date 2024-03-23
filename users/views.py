from os import error
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from serializers import UserSerializer


@api_view(['POST'])
def register(request):
    form = UserRegistrationForm(data=request.data)
    if form.is_valid():
       form.save(user=request.user)
       username = form.cleaned_data('username')
       messages.success(request, f'Your Account has been created, you can now login!')
       return Response(status=306, headers={'Location': 'login'})
    return Response(form.error, status=status.HTTP_400_BAD_REQUEST)
    # if request.method == "POST":
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'your Account has been created, you can now proceed to login for!')
    #         return redirect('login')
    # else:
    #     form = UserRegistrationForm
    # return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Update!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/profile.html', context)


@login_required
def update_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Update!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/Update_profile.html', context)
