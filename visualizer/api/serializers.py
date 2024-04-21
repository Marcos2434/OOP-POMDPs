from z3 import *

# from rest_framework import serializers

def z3_rational_to_float(rational):
    return float(rational.numerator_as_long()) / float(rational.denominator_as_long())

def Z3Serializer(m : Model) -> dict:
    """
    Convert a Z3 model to a JSON serializable format. Support for int, rational, and string values.

    Args:
        m (Model): a Z3 model
        
    Returns:
        dict: a dictionary representation of the model
    """
    values = {}
    for decl in m.decls():
        if m[decl].sort().kind() == Z3_INT_SORT:
            values[str(decl)] = m[decl].as_long()
        elif m[decl].sort().kind() == Z3_REAL_SORT:
            values[str(decl)] = z3_rational_to_float(m[decl])
        else:
            values[str(decl)] = str(m[decl])
    
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