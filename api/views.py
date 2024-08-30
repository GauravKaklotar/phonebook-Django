from rest_framework import generics, permissions, status
from .models import User, Contact, Spam
from .serializers import UserSerializer, ContactSerializer, SpamSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'message': 'Login successful'
        }, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

class SpamView(generics.CreateAPIView):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        phone_number = serializer.validated_data.get('phone_number')
        spam, created = Spam.objects.get_or_create(phone_number=phone_number)
        spam.marked_by.add(self.request.user)

        if created:
            message = f"Spam with phone number {phone_number} successfully created."
            return Response({'message': message}, status=status.HTTP_201_CREATED)
        else:
            message = f"Spam with phone number {phone_number} already exists."
            return Response({'message': message}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Spam added successfully'}, status=status.HTTP_201_CREATED)


class SearchView(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def list(self, request, *args, **kwargs):
        search_query = request.query_params.get('search', None)
        if not search_query:
            return Response({'message': 'Search query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Search by name
        name_results_startswith = Contact.objects.filter(name__startswith=search_query)
        name_results_contains = Contact.objects.filter(name__contains=search_query).exclude(id__in=name_results_startswith)
        
        # Search by phone number
        phone_results = Contact.objects.filter(phone_number=search_query)

        # Combine results
        search_results = name_results_startswith.union(name_results_contains, phone_results)
        serializer = self.get_serializer(search_results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)