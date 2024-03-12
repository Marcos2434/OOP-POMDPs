from z3 import *

# from rest_framework import serializers


def Z3Serializer(m : Model) -> str:
    # Extract values from the model
    values = {}
    for decl in m.decls():
        values[str(decl)] = m[decl].as_long() if m[decl].sort().kind() == Z3_INT_SORT else str(m[decl])

    # Convert values to JSON serializable format
    # json_serializable_values = {key: int(value) if isinstance(value, int) else value for key, value in values.items()}

    return values



# class MerchItemSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = MerchItem
#         fields = ('id', 'name', 'price', 'isavailable')

# class UserSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = User
#         fields = ('id', 'username', 'email', 'is_staff', 'work_staff')
#         # fields = '__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     item = MerchItemSerializer() # many=True     
#     user = UserSerializer()   
#     class Meta():
#         model = Order
#         fields = '__all__'