from rest_framework import serializers
from users.models import NewUser

#to create the serializer
class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=NewUser
        fields=('email','user_name','password')
        extra_kwargs={'password':{'write_only':True}}

        def create(self, validate_data):
            password=validate_data.pop('password',None)
            instance=self.Meta.model(**validate_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance

