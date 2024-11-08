from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer, ConviteSerializer, CadastroSerializer, SistemaConviteSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     queryset = Content.objects.all()
    #     content_type = self.request.query_params.get('content_type')

    #     if content_type in [choice[0] for choice in Content.CONTENT_TYPE_CHOICES]:
    #         queryset = queryset.filter(content_type=content_type)

    #     return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ConviteViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = ConviteSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = CadastroSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class SistemaViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = SistemaConviteSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)