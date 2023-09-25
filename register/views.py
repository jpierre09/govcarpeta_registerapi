from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserRegister
import requests


from .serializers import UserSerializer

def send_data_to_other_endpoint(data):
    # La URL del endpoint
    url = "https://govcarpeta-76300fb42a5a.herokuapp.com/apis/registerCitizen"

    # Los datos que se enviarán en la petición
    data = {
        "id": data["id"],
        "name": data["name"],
        "address": data["address"],
        "email": data["email"],
        "operatorId": data["operatorId"],
        "operatorName": data["operatorName"],
    }

    # Envía la petición
    response = requests.post(url, json=data)

    # Verifica el estado de la respuesta
    if response.status_code == 200:
        pass
    else:
        pass

class RegisterView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        # print(data)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            # Verifica si el usuario existe en la base de datos
            if UserRegister.objects.filter(id=data["id"]).exists():
                # El usuario ya existe
                return Response(
                    status=400,
                    data={"detail": f"El usuario con el id {data['id']} ya existe en la base de datos local"},
                )
            else:
                user, created = UserRegister.objects.get_or_create(
                    id=data["id"],
                    name=data["name"],
                    address=data["address"],
                    email=data["email"],
                    operatorId=data["operatorId"],
                    operatorName=data["operatorName"],
                )

                # Envía los datos al otro endpoint
                send_data_to_other_endpoint(data)
                # print(data)

                return Response(status=201, data=serializer.data)
        else:
            return Response(status=400, data=serializer.errors)
        
    

    # def get(self, request, id):
    #     user = UserRegister.objects.filter(id=id).first()

    #     if user is None:
    #         return Response(status=404, data={"detail": "El usuario no existe"})

    #     serializer = UserSerializer(user)

    #     return Response(status=200, data=serializer.data)

