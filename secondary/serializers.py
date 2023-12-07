from djoser.serializers  import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields=['first_name','last_name','username','email','password']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields=['first_name','last_name','username','email']


