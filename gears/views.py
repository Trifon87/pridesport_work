from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.clean_up import clean_up_files
from decorators.decorators import group_required
from gears.forms.comment_form import CommentForm
from gears.forms.gear_form import GearForm
from gears.models import Gear, Like, Comment


# Create your views here.


def gear_list(request):
    context = {
        'gears': Gear.objects.all(),
    }
    return render(request, 'gear_list_try.html', context)


def gear_details(request, pk):
    gear = Gear.objects.get(pk=pk)
    if request.method == "GET":

        context = {
            'gear': gear,
            'form': CommentForm(),
        }

        return render(request, 'gear_detail_try.html', context)

    else:
        form = CommentForm(request.POST)
        if form.is_valid():

            comment = Comment(text=form.cleaned_data['text'])
            comment.gear = gear
            comment.save()
            return redirect('gear detail', pk)
        context = {
            'gear': gear,
            'form': form,
        }

        return render(request, 'gear_detail_try.html', context)


# def gear_like(request, pk):
#     gear = Gear.objects.get(pk=pk)
#     # like = Like(test=str(pk))
#
#     like.save()
#     return redirect('gear detail', pk)
@login_required
def gear_like(request, pk):
    gear = Gear.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.gear = gear
    like.save()
    return redirect('gear detail', pk)



@login_required
def edit(request, pk):
    gear = Gear.objects.get(pk=pk)
    if request.method == "GET":
        form = GearForm(instance=gear)
        context = {
            'form': form,
            'gear': gear,
        }
        return render(request, 'gear_edit.html', context)
    else:

        form = GearForm(request.POST, request.FILES, instance=gear)
        if form.is_valid():
            gear = form.save()
            return redirect('gear detail', gear.pk)
        context = {
            'form' : form,
            'gear': gear,
        }
        return render(request, 'gear_edit.html', context)

@login_required
def delete(request, pk):
    gear = Gear.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'gear': gear,
        }
        return render(request, 'gear_delete.html', context)
    else:
        gear.delete()
        return redirect('gears')


# @group_required(['Regular User'])
@login_required
def create(request):

    if request.method == "GET":
        form = GearForm()
        context = {
            'form': form,
        }
        return render(request, 'gear_create.html', context)
    else:
        form = GearForm(request.POST,request.FILES)
        if form.is_valid():
            gear = form.save()
            return redirect('gear detail', gear.pk)
        context = {
            'form': form,
        }
        return render(request, 'gear_list_try.html', context)


def about(request):
    return render(request, 'about_us.html')

