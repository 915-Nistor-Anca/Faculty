from django.db.models import Avg
from rest_framework import serializers
from animals.models import Animal, Specie, Area, Job, Employee, Assignment, Attraction

class SpeciesKilogramsSerializer(serializers.ModelSerializer):
    avg_kilograms = serializers.SerializerMethodField()

    class Meta:
        model = Specie
        fields = ('id', 'name', 'specifications', 'endangered', 'years_expected_to_live', 'food_type', 'avg_kilograms')

    def get_avg_kilograms(self, obj):
        avg_weight = obj.content.aggregate(Avg('kilograms'))['kilograms__avg']
        return avg_weight if avg_weight else 0

class JobsSalarySerializer(serializers.ModelSerializer):
    avg_salary = serializers.FloatField()

    class Meta:
        model = Job
        fields = ('id', 'name', 'description', 'avg_salary')


class AreaEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['employee']

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


class AreaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('__all__')


class JobSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('__all__')

class EmployeeSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')

class AssignmentSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('__all__')

class AreaSerializer(serializers.ModelSerializer):
    species = SpecieSerializer2(many=True, read_only=True)
    employees = AreaEmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Area
        fields = ('__all__')


class JobSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer2(many=True, read_only=True)
    class Meta:
        model = Job
        fields = ('__all__')


class EmployeeSerializer(serializers.ModelSerializer):
    job = JobSerializer2()
    class Meta:
        model = Employee
        fields = ('__all__')


class AssignmentSerializer(serializers.ModelSerializer):
    area = AreaSerializer2()
    employee = EmployeeSerializer2()
    class Meta:
        model = Assignment
        fields = ('__all__')



class AttractionSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('__all__')

class AttractionSerializer(serializers.ModelSerializer):
    area = AreaSerializer2()
    class Meta:
        model = Attraction
        fields = ('__all__')



