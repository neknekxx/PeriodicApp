import os
from django.utils.timezone import now
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import default_storage
from .models import Element

# Home page view
@login_required
def home(request):
    return render(request, 'home.html')

# Log in view
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': "Invalid login details."})
    return render(request, 'login.html')

# Sign up view
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# About view
def about(request):
    return render(request, 'about.html')

# Periodic Table view
@login_required
def element_list(request):
    elements = Element.objects.all().order_by('atomic_number')
    return render(request, 'elements/periodic_table.html', {'elements': elements})

# Element detail view
@login_required
def element_detail(request, symbol):
    element = get_object_or_404(Element, symbol=symbol)
    return render(request, 'elements/element_detail.html', {'element': element})

# Update Element Description
@login_required
def update_element(request, symbol):
    element = get_object_or_404(Element, symbol=symbol)

    if request.method == "POST":
        new_description = request.POST.get('description')
        if new_description:
            element.description = new_description
            element.save()
        return redirect('element_detail', symbol=element.symbol)

    return render(request, 'elements/element_detail.html', {'element': element})

# Upload Element Image
@login_required
def upload_image(request, symbol):
    element = get_object_or_404(Element, symbol=symbol)

    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        filename, file_extension = os.path.splitext(image.name)
        new_filename = f"{element.symbol}_{now().strftime('%Y%m%d%H%M%S')}{file_extension}"

        # Delete old image if it exists
        if element.image and default_storage.exists(element.image.name):
            default_storage.delete(element.image.name)

        # Save the new image
        element.image.save(new_filename, image, save=True)

        return redirect('element_detail', symbol=element.symbol)

    return render(request, 'elements/element_detail.html', {'element': element})

# Main Quiz Page
@login_required
def quiz(request):
    return render(request, 'quiz.html')

# Multiple Choice Quiz Page
@login_required
def multiple_choice_quiz(request):
    return render(request, 'mcq_quiz.html')

# Jumbled Words Quiz Page
@login_required
def jumbled_words_quiz(request):
    return render(request, 'jumbled_quiz.html')
