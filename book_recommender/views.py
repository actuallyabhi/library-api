from django.http import JsonResponse
from .models import Book
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth.models import User
from datetime import datetime

from django.http import HttpResponse

@api_view(['GET'])
def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

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
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None or not user.check_password(password):
        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)
    refresh = RefreshToken.for_user(user)
    response_data = {
        'status': 'success',
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def top_books_by_category(request, category):
    books = Book.objects.filter(ISBN = category)[:10]
    data = {
        'category': category,
        'books': [
            {'title': book.Book_Title,
             'author': book.Book_Author,
             'publication_year': book.Year_Of_Publication,
            'publisher': book.Publisher,
            'image_urls': [book.Image_URL_S, book.Image_URL_M, book.Image_URL_L],
             } for book in books]
    }
    return JsonResponse(data)

   
