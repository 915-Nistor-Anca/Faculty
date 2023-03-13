
# Create your views here.
import django_filters
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from animals.models import Animal, Specie, Area
from animals.serializers import AnimalSerializer, SpecieSerializer, AreaSerializer, SpecieSerializer2, AnimalSerializer2


class AnimalFilter(django_filters.FilterSet):
    kilograms = django_filters.NumberFilter()
    kilograms__gt = django_filters.NumberFilter(field_name='kilograms', lookup_expr='gt')

    class Meta:
        model = Animal
        fields = ['kilograms']


class AnimalList(APIView):
    #def get(self, request, format=None):
        #animals = Animal.objects.all()
    #   animals = Animal.objects.filter(kilograms__gt=50)
    #    serializer = AnimalSerializer(animals, many=True)
    #   return Response(serializer.data)

    def get(self, request, format=None):
        kilograms = request.query_params.get('kilograms', None)
        if kilograms is not None:
            animals = Animal.objects.filter(kilograms__gt=kilograms)
        else:
            animals = Animal.objects.all()
        serializer = AnimalSerializer2(animals, many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = AnimalSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnimalDetail(APIView):
    def get_object(self, pk):
        try:
            return Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        animal = self.get_object(pk)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        animal = self.get_object(pk)
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        animal = self.get_object(pk)
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SpecieList(APIView):
        def get(self, request, format=None):
            species = Specie.objects.all()
            serializer = SpecieSerializer2(species, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = SpecieSerializer2(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpecieDetail(APIView):
        def get_object(self, pk):
            try:
                return Specie.objects.get(pk=pk)
            except Specie.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            specie = self.get_object(pk)
            serializer = SpecieSerializer(specie)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            specie = self.get_object(pk)
            serializer = SpecieSerializer(specie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            specie = self.get_object(pk)
            specie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)





class AreaList(APIView):
            def get(self, request, format=None):
                areas = Area.objects.all()
                serializer = AreaSerializer(areas, many=True)
                return Response(serializer.data)

            def post(self, request, format=None):
                serializer = AreaSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AreaDetail(APIView):
            def get_object(self, pk):
                try:
                    return Area.objects.get(pk=pk)
                except Area.DoesNotExist:
                    raise Http404

            def get(self, request, pk, format=None):
                area = self.get_object(pk)
                serializer = AreaSerializer(area)
                return Response(serializer.data)

            def put(self, request, pk, format=None):
                area = self.get_object(pk)
                serializer = AreaSerializer(area, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def delete(self, request, pk, format=None):
                area = self.get_object(pk)
                area.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)