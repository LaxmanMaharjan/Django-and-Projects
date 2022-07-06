from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    roll_no = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    created_at = serializers.DateTimeField()
