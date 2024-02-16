from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Review
from .forms import ReviewForm


def review_list(request):
    """
    Function for all reviews
    """
    form = ReviewForm()
    reviews = Review.objects.all()
    return render(
        request,
        'review/review.html',
        {'reviews': reviews, 'form': form})


@login_required
def review_create(request):
    """
    Function for creating a new review
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Your review was successfully submitted!')
            return redirect('review_list')

        else:
            messages.error(request, 'Something went wrong, try agian.')
            return render(request, 'review/review.html', {'form': form})

    return HttpResponse('Invalid request method or something went wrong.')


@login_required
def review_edit(request, pk):
    """
    Function for editing a review
    """
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review is updated!')
            return redirect('review_list')
    else:
        messages.error(request, 'Something went wrong, try again!')
        form = ReviewForm(instance=review)

    return render(
        request,
        'review/review_edit.html',
        {'form': form, 'review': review}
    )


@login_required
def review_delete(request, review_id):
    """
    Function for deleting a review
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    messages.success(request, 'Your review was deleted!')
    return redirect('review_list')
