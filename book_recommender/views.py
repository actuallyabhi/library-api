from django.http import JsonResponse
from book_recommender.models import Book
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response_data = {
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
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(response_data, status=status.HTTP_200_OK)



def top_books_by_category(request, category):
    books = Book.objects.filter(category = category).order_by('-rating')[:5]
    data = {
        'category': category,
        'books': [
            {'title': book.title,
             'author': book.author,
             'publication_date': book.publication_date,
             'rating': book.rating
             } for book in books]
    }
    return JsonResponse(data)
