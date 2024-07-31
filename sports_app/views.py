from django.shortcuts import render
from .models import Customer
from .serializer import customer_serializer
from  rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(["POST"])
def create_customer(request):
    if request.method == "POST":
        serial = customer_serializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def read_customer(request):
    if request.method == "GET":
        customer = Customer.objects.all()
        serial = customer_serializer(customer,many = True)
        return Response(serial.data, status=status.HTTP_200_OK)



@api_view(["GET","PUT","DELETE"])
def api(request,id):
    try:
        customer= Customer.objects.get(id=id)
    except:
        return Response("Values not found", status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serial= customer_serializer(customer)
        return Response(serial.data)
    
    elif request.method == "PUT":
        serial = customer_serializer(customer,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        customer.delete()
        return Response(status=status.HTTP_410_GONE)







#  from .models import Customer
# from .serializer import customer_serializer
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view



# @api_view(["GET","POST"])

# def create_customer(request):
#     if request.method=="POST":
#         serial = customer_serializer(data=request.data)
#         if serial.is_valid:
#             serial.save()
#             return Response(serial.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == "GET":
#         customer=Customer.objects.all()
#         serial=customer_serializer(customer,many = True)
#         return Response(customer.data,status=status.HTTP_302_FOUND)
    



# @api_view(["GET","PUT","DELETE"])
# def api(request,id):
#     try:
#         customer = Customer.objects.filter(id = id)

#     except:
#         return Response("Values not found", status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "GET":
#         serial = customer_serializer(customer)
#         return Response(serial.data)
    
#     elif request.method == "PUT":
#         serial = customer_serializer(customer,data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data,status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == "DELETE":
#         customer.delete()
#         return Response(status=status.HTTP_410_GONE)








#  Create your views here.




# @api_view(["POST","POST"])
# def create_customer(request):
#     if request.method == "POST":
#         serial = customer_serializer(data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data,status=status.HTTP_201_CREATED,)
#         else :
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "GET":
#         customer = Customer.objects.all()
#         serial = customer_serializer(customer,many = True)
#         return Response(serial.data,status=status.HTTP_302_FOUND)
    






# @api_view(["PUT"])
# def update_customer(request,id):
#     if request.method == "PUT":
#         customer = Customer.objects.get(id = id)
#         serial = customer_serializer(customer,data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data ,status=status.HTTP_202_ACCEPTED)
#         else :
#             return Response(status=status.HTTP_404_NOT_FOUND)
    



# @api_view(["GET"])

# def read_one_customer(request,id):
#     if request.method == "GET":
#         customer = Customer.objects.get(id=id)
#         serial = customer_serializer(customer)
#         return Response(serial.data)


# @api_view(["DELETE"])

# def delete_customer(request,id):
#     if request.method == "DELETE":
#         customer = Customer.objects.get(id=id)
#         customer.delete()
#         return Response(customer,status=status.HTTP_410_GONE)



