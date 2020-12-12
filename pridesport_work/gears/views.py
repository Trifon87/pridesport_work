from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from pridesport_work.core.clean_up import clean_up_files
from pridesport_work.decorators.decorators import group_required
from pridesport_work.gears.forms.comment_form import CommentForm
from pridesport_work.gears.forms.gear_form import GearForm, FilterForm
from pridesport_work.gears.models import Gear, Like, Comment


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''
    price = params['price'] if 'price' in params else FilterForm.ORDER_ASC

    return {
        'order': order,
        'text': text,
        'price': price,
    }

def gear_list(request):
    params = extract_filter_values(request.GET)
    order_by = 'price' if params['order'] == FilterForm.ORDER_ASC else '-price'
    # order_by = 'text' if params['order'] == FilterForm.ORDER_ASC else '-text'
    gears = Gear.objects.filter(name__icontains=params['text']).order_by(order_by)

    for gear in gears:
        gear.can_delete = gear.created_by_id == request.user.id
    context = {
        'gears': gears,
        'filter_form': FilterForm(initial=params),
    }
    return render(request, 'gear_list.html', context)


def gear_details(request, pk):

    gear = Gear.objects.get(pk=pk)
    gear.can_delete = gear.created_by_id == request.user.id
    gear.can_edit = gear.created_by_id == request.user.id
    if request.method == "GET":

        context = {
            'gear': gear,
            'form': CommentForm(),
        }

        return render(request, 'gear_detail.html', context)

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

        return render(request, 'gear_detail.html', context)



@login_required
def gear_like(request, pk):
    gear = Gear.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.gear = gear
    like.save()
    return redirect('gear detail', pk)

@group_required(['Staff'])
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

@group_required(['Staff'])
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


@group_required(['Staff'])
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
        return render(request, 'gear_list.html', context)


class CreateGearView(views.CreateView):
    template_name = 'gear_create.html'
    form_class = GearForm
    success_url = reverse_lazy('user profile')


def about(request):
    return render(request, 'about_us.html')

