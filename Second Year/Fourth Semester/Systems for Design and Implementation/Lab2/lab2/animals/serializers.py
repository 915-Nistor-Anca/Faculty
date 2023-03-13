from rest_framework import serializers
from animals.models import Animal, Specie, Area

class SpecieSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = ('__all__')

class AnimalSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('__all__')

class AnimalSerializer(serializers.ModelSerializer):
    specie = SpecieSerializer2()
    class Meta:
        model = Animal
        fields = ('__all__')

class SpecieSerializer(serializers.ModelSerializer):
    content = AnimalSerializer2(many=True, read_only=True)
    class Meta:
        model = Specie
        fields = ('__all__')


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('__all__')