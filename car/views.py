from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Person, Car
from .serializers import PersonSerializer, CarSerializer, CarReadSerializer

@api_view(['GET', 'POST'])
def person_view(request):
    if request.method == "GET":
        person = Person.objects.all()
        return Response(PersonSerializer(person, many=True).data,
                        status=status.HTTP_200_OK)

    elif request.method == "POST":
        ser = PersonSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)       


@api_view(['GET', 'POST'])
def car_view(request):
    if request.method == "GET":
        car = Car.objects.all()
        return Response(CarSerializer(car, many=True).data,
                        status=status.HTTP_200_OK)

    elif request.method == "POST":
        ser = CarSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(["GET"])
def information_view(request):
    car = Car.objects.all()
    return Response(CarReadSerializer(car, many=True).data, 
                    status=status.HTTP_200_OK)

