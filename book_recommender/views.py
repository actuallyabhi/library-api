from django.http import JsonResponse
from .models import Book, Ratings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth.models import User
from datetime import datetime

from django.http import HttpResponse



@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response_data = {
            'status': 'success',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.filter(username=username).first()
    if user is None or not user.check_password(password):
        return Response({'error': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)
    refresh = RefreshToken.for_user(user)
    response_data = {
        'status': 'success',
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def top_books_by_category(request, category):
    books = Book.objects.filter(Category=category)[:10]
    data = {
        'category': category,
        'books': [
            {   'isbn': book.ISBN, 
                'title': book.Book_Title,
                'author': book.Book_Author,
                'publication_year': book.Year_Of_Publication,
                'publisher': book.Publisher,
                'image_urls': [book.Image_URL_S, book.Image_URL_M, book.Image_URL_L],
                'ratings': get_book_ratings(book.ISBN),
            } for book in books]
    }
    return JsonResponse(data)


# search api
@api_view(['GET'])
def search(request, query):
    books = Book.objects.filter(Book_Title__icontains = query)[:10]
    data = {
        'query': query,
        'books': [
            {   'isbn': book.ISBN, 
                'title': book.Book_Title,
                'author': book.Book_Author,
                'publication_year': book.Year_Of_Publication,
                'publisher': book.Publisher,
                'image_urls': [book.Image_URL_S, book.Image_URL_M, book.Image_URL_L],
                'ratings': get_book_ratings(book.ISBN),
            } for book in books]
    }
    return JsonResponse(data)

   
@api_view(['POST'])
def add_rating(request):
    username = request.data.get('username')
    isbn = request.data.get('isbn')
    rating = request.data.get('rating')
    user = User.objects.filter(username=username).first()
    book = Book.objects.filter(ISBN=isbn).first().ISBN
    if user is None or book is None:
        return Response({'error': 'Invalid username or book.'}, status=status.HTTP_400_BAD_REQUEST)
    rating = Ratings.objects.create(username=user, ISBN=book, rating=rating)
    return Response({'status': 'success'}, status=status.HTTP_201_CREATED)

def get_book_ratings(isbn):
    ratings = Ratings.objects.filter(ISBN=isbn)
    total_ratings = 0
    num_ratings = 0
    for rating in ratings:
        total_ratings += rating.rating
        num_ratings += 1
    average_rating = total_ratings / num_ratings if num_ratings > 0 else 0
    return {
        'num_ratings': num_ratings,
        'average_rating': average_rating,
    }
