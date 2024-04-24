from rest_framework import serializers
from .models import LoginUser
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model= LoginUser
        fields=['id','name','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self,validated_data):
        password=validated_data.pop('password', None)
        instance= self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

class UserDetailSerializer(serializers.ModelSerializer):
    '''
    This class serializes the user data
    '''
    class Meta:
        '''
        This is a meta class
        '''
        model = LoginUser
        fields = ['id', 'email','password']