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
    product = get_object_or_404(Product, product_id=product.pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.author = user
            review = form.save()
            messages.success(request, 'Your review was added successfully.')
            return redirect(reverse('product_detail', args=[product.pk]))
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
