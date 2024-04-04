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
from .serializers import Z3Serializer

# OOP
from OOP.createLine import create_line_constrained
from OOP.createGrid import create_grid_constrained
from OOP.createMaze import create_maze_constrained

from OOP.createLineFixed import create_line_pre
from OOP.createGridFixed import create_grid_pre
from OOP.createMazeFixed import create_maze_pre

import importlib.util

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
        if request.data['model'] == "Line":

            if not 'sensor_selection' in request.data:
                create_line_constrained(
                    target=int(request.data['target']),
                    size=int(request.data['size']),
                    budget=int(request.data['budget']),
                    threshold="<= " + request.data['threshold'],
                    det=bool(request.data['deterministic']),
                )
                
                if bool(request.data['deterministic']): module_path = 'OOP/generated_models/' + request.data['model'].lower() + '_' + request.data['size'] + '_det_z3.py'
                else: module_path = 'OOP/generated_models/' + request.data['model'].lower() + '_' + request.data['size'] + '_ran_z3.py'
            else:
                create_line_pre(
                    target=int(request.data['target']),
                    size=int(request.data['size']),
                    budget=int(request.data['budget']),
                    threshold="<= " + request.data['threshold'],
                    det=bool(request.data['deterministic']),
                    pre=request.data['observables'],
                )
                if bool(request.data['deterministic']): module_path = 'OOP/generated_models/fixed_line_' + request.data['size'] + '_det_z3.py'
                else: module_path = 'OOP/generated_models/fixed_line_' + request.data['size'] + '_ran_z3.py'
                
        elif request.data['model'] == "Grid":
            if not 'sensor_selection' in request.data:
                create_grid_constrained(
                    target=int(request.data['target']),
                    size=int(request.data['size']),
                    budget=int(request.data['budget']),
                    threshold="<= " + request.data['threshold'],
                    det=bool(request.data['deterministic']),
                )
                if bool(request.data['deterministic']): module_path = 'OOP/generated_models/' + request.data['model'].lower() + '_' + request.data['size'] + 'x' + request.data['size'] + '_det_z3.py'
                else: module_path = 'OOP/generated_models/' + request.data['model'].lower() + '_' + request.data['size'] + 'x' + request.data['size'] + '_ran_z3.py'
            else:
                create_grid_pre(
                    target=int(request.data['target']),
                    sizex=int(request.data['size']),
                    sizey=int(request.data['size']),
                    budget=int(request.data['budget']),
                    threshold="<= " + request.data['threshold'],
                    det=bool(request.data['deterministic']),
                    pre=request.data['observables'],
                )
                if bool(request.data['deterministic']): module_path = 'OOP/generated_models/fixed_grid_' + request.data['size'] + 'x' + request.data['size'] + 'det_z3.py'
                else: module_path = 'OOP/generated_models/fixed_grid_' + request.data['size'] + 'x' + request.data['size'] + '_ran_z3.py'
                
        elif request.data['model'] == "Maze":
            if not 'sensor_selection' in request.data:
                create_maze_constrained(
                    budget = int(request.data['budget']),
                    target = int(request.data['target']),
                    sizex = int(request.data['rows']), 
                    sizey = int(request.data['columns']), 
                    threshold="<= " + request.data['threshold'],
                    det = bool(request.data['deterministic'])
                )
                if bool(request.data['deterministic']): module_path = 'OOP/generated_models/' + request.data['model'].lower() + '_' + request.data['rows'] + 'x' + request.data['columns'] + '_det_z3.py'
                else: module_path = 'OOP/generated_models/' + request.data['model'].lower() + '_' + request.data['rows'] + 'x' + request.data['columns'] + '_ran_z3.py'
            else:
                create_maze_pre(
                    budget = int(request.data['budget']),
                    target = int(request.data['target']),
                    sizex = int(request.data['rows']), 
                    sizey = int(request.data['columns']), 
                    threshold="<= " + request.data['threshold'],
                    det = bool(request.data['deterministic']),
                    pre = request.data['observables']
                )
                if bool(request.data['deterministic']): module_path = 'OOP/generated_models/fixed_maze_' + request.data['rows'] + 'x' + request.data['columns'] + '_det_z3.py'
                else: module_path = 'OOP/generated_models/fixed_maze_' + request.data['rows'] + 'x' + request.data['columns'] + '_ran_z3.py'
                
        # import module
        spec = importlib.util.spec_from_file_location("generated_module", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    
        sol = module.sol()
        if sol == "No Solution":
            return Response({
                'solution' : 'No solution'
            },
            status=status.HTTP_200_OK)
        elif sol == None:
            return Response({
                'solution' : 'Unknown'
            }, status=status.HTTP_200_OK)
        
        content = {
            'budget' : request.data['budget'],
            'target' : request.data['target'],
            'size' : request.data['size'],
            'threshold' : request.data['threshold'],
            'deterministic' : True if request.data['deterministic'] else False,
            'sensor_selection' : True if 'sensor_selection' in request.data else False,
            'solution': Z3Serializer(sol),
        }
        
        return Response(content,
        status=status.HTTP_200_OK)
    else:
        return Response(form.errors,
        status=status.HTTP_400_BAD_REQUEST)

        
    

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