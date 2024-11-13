from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Tweet, Like
from .forms import TweetForm
from .forms import CustomUserCreationForm

# Get all tweets
def tweet_list_view(request):
    tweets = Tweet.objects.all()
    for tweet in tweets:
        tweet.is_liked_by_user = tweet.likes.filter(user=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'tweet/tweet_list.html', {'tweets': tweets})

# Create a tweets
@login_required
def tweet_create_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list_view')
    else:
        form = TweetForm()
    return render(request, 'tweet/tweet_create.html', {'form': form})

# Edit a tweet
@login_required
def tweet_edit_view(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk, user=request.user)  # Ensure the user owns the tweet
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list_view')  # Redirect to tweet list view after saving
    else:
        form = TweetForm(instance=tweet)  # Populate form with tweet data
    return render(request, 'tweet/tweet_edit.html', {'form': form, 'tweet': tweet}) 

# Delete a tweet
@login_required
def tweet_delete_view(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk, user=request.user)  # Ensure the user owns the tweet
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list_view')  # Redirect to tweet list view after saving
    else:
        form = TweetForm(instance=tweet)  # Populate form with tweet data
    return render(request, 'tweet/tweet_confirm_delete.html', {'tweet': tweet})


@login_required
def like_tweet_view(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, tweet=tweet)
    
    if not created:
        like.delete()
    
    return redirect('tweet_list_view')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the new user
            return redirect('tweet_list_view')  # Redirect to home or any other page
    else:
        form = CustomUserCreationForm()
    return render(request, 'tweet/register.html', {'form': form})
