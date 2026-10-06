from rest_framework import serializers
from employees.models import Employee


# class EmployeeSerializer(serializers.Serializer):
#     empid = serializers.IntegerField()
#     name = serializers.CharField(max_length=50)
#     age = serializers.IntegerField()
#     place = serializers.CharField(max_length=30)
#     gender_choices = [ ('male','Male'),('female','Female') ]
#     gender = serializers.ChoiceField(choices=gender_choices)
#     salary = serializers.IntegerField()
#     joining_date = serializers.DateField()
#     designation = serializers.CharField()
#
#     def create(self, validated_data):
#         e=Employee.objects.create(**validated_data)
#         return e
#
#     def update(self,i,validated_data):
#         i.empid = validated_data.get('empid',i.empid)
#         i.name = validated_data.get('name',i.name)
#         i.age = validated_data.get('age',i.age)
#         i.place = validated_data.get('place',i.place)
#         i.gender = validated_data.get('gender', i.gender)
#         i.salary = validated_data.get('salary', i.salary)
#         i.joining_date = validated_data.get('joining_date', i.joining_date)
#         i.designation = validated_data.get('designation', i.designation)
#
#         i.save()
#         return i

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        return data
