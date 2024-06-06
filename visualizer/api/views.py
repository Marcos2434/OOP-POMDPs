# Standard
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

# REST framework
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

# Local
from .forms import OOP_Form
# from .solver.solvers import Z3_Solver, Brute_Force_Solver
from solver.solvers import Z3_Solver, Heuristic_Solver

@api_view(['GET'])
@permission_classes(())
def apiIndex(request):
    apiUrls = {
        'api' : {
            'Create Model' : '/createModel',
        },
    }
    return Response(apiUrls)

@api_view(['POST'])
@permission_classes(())
def createModel(request):
    form = OOP_Form(request.data)
    if form.is_valid():
        request.data['deterministic'] = True if 'deterministic' in request.data else False

        if request.data['solver'] == 'Z3': return Z3_Solver(request.data)
        elif request.data['solver'] == 'Heuristic': return Heuristic_Solver(request.data)
        
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


 
    

# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
# def apiAllOrders(request):
#     if request.user.is_staff or request.user.work_staff:
#         serializedOrders = OrderSerializer(Order.objects.all().order_by('-date_created'), many=True)
#         return Response({'total' : Order.objects.all().count(), 'orders' : serializedOrders.data})
#     return HttpResponseRedirect(reverse('index'))

# @api_view(['GET'])   
# @permission_classes((IsAuthenticated,))     
# def apiDates(request, date):
#     if request.user.work_staff or request.user.is_staff:
#         date = modifyDateString(string=date)
#         serializedOrders = OrderSerializer(Order.objects.filter(pay_date=date), many=True)

#         return Response(serializedOrders.data)
#     return HttpResponseRedirect(reverse('index'))

# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def apiMarkOrderAsPaid(request):
#     if request.user.is_staff or request.user.work_staff:
#         order = Order.objects.get(pk=request.data['order_id'])
#         order.payed = bool(request.data['paid'])
#         order.save()
        
#         return Response({'paid': order.payed})
#     return HttpResponseRedirect(reverse('index'))

# @api_view(['POST'])
# @permission_classes((IsAdminUser,))
# def apiDeleteOrder(request):  
#     if request.user.is_staff or request.user.work_staff:
#         try: 
#             order_id = request.data['order_id']
#             Order.objects.get(pk=order_id).delete()
#             return Response({
#                 'deleted' : True,
#                 'info' : f'Succesfully deleted item with id {order_id}',
#             })
#         except Exception as e:
#             return Response({
#                 'deleted' : False,
#                 'info' : str(e),
#             })
#     return HttpResponseRedirect(reverse('index'))