from rest_framework.serializers import ModelSerializer
from .models import User

# Feed에서 노출시킬 User Serializer
class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "is_business")

class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" # Model의 전체 field 가져옴       