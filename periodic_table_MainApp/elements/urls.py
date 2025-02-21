from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Authentication
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Home
    path('', views.home, name='home'),

    # About Page
    path('about/', views.about, name='about'),

    # Periodic Table
    path('elements/', views.element_list, name='element_list'),
    path('element/<str:symbol>/', views.element_detail, name='element_detail'),

    # Update Element Description & Upload Image
    path('element/<str:symbol>/update/', views.update_element, name='update_element'),
    path('element/<str:symbol>/upload/', views.upload_image, name='upload_image'),

    # Quiz Pages
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/multiple-choice/', views.multiple_choice_quiz, name='multiple_choice_quiz'),
    path('quiz/jumbled-words/', views.jumbled_words_quiz, name='jumbled_quiz'),

    # Password Change
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
]

# ✅ Ensuring media files can be accessed in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
