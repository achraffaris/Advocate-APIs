from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Advocate
from .serializers import AdvocateSerializer

class AdvocatesAPIView(ListAPIView):
    serializer_class = AdvocateSerializer
    def get_queryset(self):
        query_param = self.request.GET.get('query')
        if (query_param == None):
            query_param = ''
        return Advocate.objects.filter(username__icontains=query_param)


class AdvocateDetailAPIView(ListAPIView):
    serializer_class = AdvocateSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        adv = Advocate.objects.filter(username=username)
        if (adv is not None):
            return (adv)
        return (None)