from rest_framework import serializers
from student_api.utils import College, Student

class CollegeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    location = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return College(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        return instance

class StudentSerializer(serializers.Serializer):
    roll_no = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    college = CollegeSerializer()

    def create(self, validated_data):
        serializer = CollegeSerializer(data = validated_data['college'])
        college = None
        if serializer.is_valid():
            college = serializer.save()

        validated_data['college'] = college
        return Student(**validated_data)

    def update(self, instance, validated_data):
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)

        serializer = CollegeSerializer(instance.college, data = validated_data['college'])
        college = None
        if serializer.is_valid():
            college = serializer.save()

        instance.college = college
        return instance

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("You are Under Age. Must be 18+")
        return value

    def validate(self, data):
        if data['name'] == 'ram' and data['age'] < 20:
            raise serializers.ValidationError("If you are Ram you must be 20+")
        return data



