from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

# Create your views here.
class TodosView(viewsets.ModelViewSet):
    serializer_class = TodosSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.headers["X-Total-Count"] = response.data["count"]
        return response

    def get_queryset(self, *args, **kwargs):
        queryset = Todos.objects.all().filter(user=self.request.user.id)
        return queryset
