from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """
    Add review to product
    """
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    form_class = ReviewForm

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # review = form.save(commit=False)
            review.product = product
            review.author = user
            review = form.save()
            messages.success(request, 'Your review was added successfully.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(
                request,
                'Unable to add the review. Please check the form and resubmit')
    else:
        form = ReviewForm()
   
    template = reviews/review.html
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required()
def edit_review(request, product_id, review_id):
    """
    Allows logged in authors to edit their own reviews
    """
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)

    if user == review.author:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                review = form.save(commit=False)
                review.save()
                messages.success(request, 'Your review has been updated')
                
                return redirect(reverse('product_detail', args=[product.pk]))
            else:
                messages.error(
                    request,
                    'Not able to update review. Please check the form.'
                )
        else:
            form = ReviewForm(instance=review)
    else:
        messages.error(request, 'You need to be the review author to edit.')
        return redirect(reverse('product_detail', args=[product.pk]))

    context = {
        'form': form,
        'product': product,
        'review': review,
    }

    return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, product_id, review_id):
    """
    Let's author or admin delete the review
    """ 
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)

    if not (user == review.user or user.is_superuser):
        messages.error(
            request,
            f'Only the site owner or the review author can delete it.',
        )
        return redirect(reverse('product_detail', args=[product.pk]))

    review.delete()
    messages.success(request, f'Review has been deleted')
    return redirect(reverse('product_detail', args=[product.pk]))
