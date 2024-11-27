from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book, Category
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.decorators import action

# Create your views here.


class BookAPIList(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('pk')
    serializer_class = BookSerializer

class BookAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIDestroy(generics.RetrieveDestroyAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer






# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all().order_by('id')
#     serializer_class = BookSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")

#         if not pk:
#             return Book.objects.all().order_by('id')[:5]
#         return Book.objects.filter(pk=pk)
   
   
#     @action(methods=['get'], detail = True)
#     def category(self, requset, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name })
    
        





# class BookAPIView(generics.ListCreateAPIView):
#      queryset = Book.objects.all()
#      serializer_class = BookSerializer


# class BookAPIUpdate(generics.UpdateAPIView):
#      queryset = Book.objects.all()
#      serializer_class = BookSerializer

# class BookAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#      queryset = Book.objects.all()
#      serializer_class = BookSerializer

