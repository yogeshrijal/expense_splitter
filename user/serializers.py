from user.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','profile_picture','address','contact']
        read_only_fields=['id','role']




class RegisterUserSerializer(ModelSerializer):
    confirm_password=serializers.CharField(write_only=True)
    class Meta:
       model=User
       fields=['id','username','password','confirm_password','address','contact','role','email']
    


    def validate(self, attrs):
        if attrs['password']!=attrs['confirm_password']:
            raise serializers.ValidationError('the password did not match try again')
        
        return attrs


    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user=User.objects.create_user( 
            username=validated_data['username'],
            password=validated_data['password'],
            address=validated_data['address'],
            contact=validated_data['contact'],
            role=validated_data['role'],
            email=validated_data['email'],
        )
        return user








    
       