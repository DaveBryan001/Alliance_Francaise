from rest_framework import viewsets, permissions, generics
from .models import Course, Event, Resource
from .serializers import CourseSerializer, EventSerializer, ResourceSerializer, RegisterSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from haystack.query import SearchQuerySet
from rest_framework.response import Response
from rest_framework.views import APIView



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def search(self, request):
        query = request.query_params.get('q', '')
        courses = self.get_queryset().filter(name__icontains=query)
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def search(self, request):
        query = request.query_params.get('q', '')
        events = self.get_queryset().filter(name__icontains=query)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def search(self, request):
        query = request.query_params.get('q', '')
        resources = self.get_queryset().filter(name__icontains=query)
        serializer = self.get_serializer(resources, many=True)
        return Response(serializer.data)


class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class SearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        course_results = SearchQuerySet().models(Course).filter(content=query)
        event_results = SearchQuerySet().models(Event).filter(content=query)
        resource_results = SearchQuerySet().models(Resource).filter(content=query)

        results = {
            'courses': [{'name': course.name, 'description': course.description} for course in course_results],
            'events': [{'name': event.name, 'description': event.description} for event in event_results],
            'resources': [{'name': resource.name, 'description': resource.description} for resource in resource_results],
        }
        return Response(results)