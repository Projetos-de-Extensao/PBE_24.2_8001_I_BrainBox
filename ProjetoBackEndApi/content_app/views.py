from rest_framework import viewsets
from .models import Feedback, Convite, Member
from .serializers import ConviteSerializer,FeedbackSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction


@login_required
@transaction.atomic
def accept_invitation(request):
    if request.method == 'POST':
        token = request.POST['token']
        try:
            convite = Convite.objects.get(link=token, status='Pendente')
            convite.status = 'Aceito'
            convite.save()
            return JsonResponse({'message': 'Invitation accepted and counted.'})
        except Convite.DoesNotExist:
            return JsonResponse({'error': 'Invalid or expired invitation token.'})
    return render(request, 'accept_invitation.html')

def send_invitation(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_remetente = Member.objects.get(user=request.user)
        try:
            convite = user_remetente.enviar_convite(email)
            invite_link = f'https://your-app.com/create-account?token={convite.link}'
            
            send_mail(
                'Account Invitation',
                f'You are invited to create an account. Click the link to create an account: {invite_link}',
                'your-email@gmail.com',
                [email],
                fail_silently=False,
            )
            
            return JsonResponse({'message': 'Invitation sent successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return render(request, 'send_invitation.html')
class ConviteViewSet(viewsets.ModelViewSet):
    queryset = Convite.objects.all()
    serializer_class = ConviteSerializer

    def perform_create(self, serializer):
        serializer.save(userRemetente=self.request.user.member)

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)
