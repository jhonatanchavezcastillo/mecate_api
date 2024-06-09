from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .services import get_stackexchange
from django.db.models import Count
from .models import Vuelos, Aeropuertos, Aerolineas
from .serializers import AerolineasSerializer


class ExternalDataView(APIView):
    def get(self, request, *args, **kwargs):
        
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        data_url = get_stackexchange(url)

        if data_url is None:
            return Response({"error": "Error al obtener datos externos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Filtrar los datos si es necesario
        #filtered_data = self.filter_data(data_url)
        #return Response(filtered_data, status=status.HTTP_200_OK)

        return Response(data_url, status=status.HTTP_200_OK)

    def filter_data(self, data):
        # Implementa aquí tu lógica de filtrado
        filtered_data = [item for item in data if item['some_key'] == 'some_value']
        return filtered_data

#1\. Obtener el número de respuestas contestadas y no contestadas
class TotalAnsweredView(APIView):
    def get(self, request, *args, **kwargs):
        
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        data_url = get_stackexchange(url)

        if data_url is None:
            return Response({"error": "Error al obtener datos externos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        filtered_data = self.filter_data(data_url)
        return Response(filtered_data, status=status.HTTP_200_OK)

    def filter_data(self, data):
        #Obtener el número de respuestas contestadas 
        #Sumo todos los elementos en donde is_answered sea igual a true
        answered_count = sum(1 for item in data['items'] if item['is_answered'])
        #Obtener el número de respuestas no contestadas
        #Obtengo la longitud de items y lo resto con el total de respuestas contestadas
        #Por lógica el total de items menos el de respuestas contestadas nos dará como resultado las respuestas no contestadas
        unanswered_count = len(data['items']) - answered_count

        #Generamos el array de salida
        result = {
            "total_answered": answered_count,
            "total_unanswered": unanswered_count
        }

        return result

#2\. Obtener la respuesta con mayor reputación
class MaxReputationView(APIView):
    def get(self, request, *args, **kwargs):
        
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        data_url = get_stackexchange(url)

        if data_url is None:
            return Response({"error": "Error al obtener datos externos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        filtered_data = self.filter_data(data_url)
        return Response(filtered_data, status=status.HTTP_200_OK)

    def filter_data(self, data):
       max_reputation = max(data['items'], key=lambda x: x['owner']['reputation'])
       return max_reputation

#3\. Obtener la respuesta con menor número de vistas
class MinViewCountView(APIView):
    def get(self, request, *args, **kwargs):
        
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        data_url = get_stackexchange(url)

        if data_url is None:
            return Response({"error": "Error al obtener datos externos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        filtered_data = self.filter_data(data_url)
        return Response(filtered_data, status=status.HTTP_200_OK)

    def filter_data(self, data):
       min_view = min(data['items'], key=lambda x: x['view_count'])
       return min_view

#4\. Obtener la respuesta más vieja y más actual
class AnswerTimeView(APIView):
    def get(self, request, *args, **kwargs):
        
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        data_url = get_stackexchange(url)

        if data_url is None:
            return Response({"error": "Error al obtener datos externos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        filtered_data = self.filter_data(data_url)
        return Response(filtered_data, status=status.HTTP_200_OK)

    def filter_data(self, data):
       current = max(data['items'], key=lambda x: x['creation_date'])
       old = min(data['items'], key=lambda x: x['creation_date'])
       
       #Generamos el array de salida
       result = []
       result.append({"answer_current":current})
       result.append({"answer_old":old})
       return result

#1\. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento
#durante el año?
class VuelosConAeropuertosView(APIView):
    def get(self, request, *args, **kwargs):
        #Obtenemos el id del aeropuerto con más movimientos
        most_common_aeropuerto = (
            Vuelos.objects.values('id_aeropuerto')
            .annotate(aeropuerto_count=Count('id_aeropuerto'))
            .order_by('-aeropuerto_count')
            .first()
        )
        #Obtenemos el nombre del aeropuerto con más movimiento
        name_aeropuerto = (
            Aeropuertos.objects.values("nombre_aeropuerto")
            .filter(id_aeropuerto=most_common_aeropuerto['id_aeropuerto'])
            .first()
        )
        #Generamos la salida de datos
        if most_common_aeropuerto:
            result = {
                'id_aeropuerto': most_common_aeropuerto['id_aeropuerto'],
                'vuelos_count': most_common_aeropuerto['aeropuerto_count'],
                'nombre_aeropuerto': name_aeropuerto['nombre_aeropuerto'],
            }
            return Response(result)
        else:
            return Response({"error": "No hay vuelos en la base de datos."}, status=404)

#2\. ¿Cuál es el nombre aerolínea que ha realizado mayor número de
#vuelos durante el año?
class AerolineaMasVuelosView(APIView):
    def get(self, request, *args, **kwargs):
        #Obtenemos el id del aeropuerto con más movimientos
        most_common_aerolinea = (
            Vuelos.objects.values('id_aerolinea')
            .annotate(aerolinea_count=Count('id_aerolinea'))
            .order_by('-aerolinea_count')
            .first()
        )
        #Obtenemos el nombre de la aerolinea con más movimiento
        name_aerolinea = (
            Aerolineas.objects.values("nombre_aerolinea")
            .filter(id_aerolinea=most_common_aerolinea['id_aerolinea'])
            .first()
        )
        #Generamos la salida de datos
        if most_common_aerolinea:
            result = {
                'id_aerolinea': most_common_aerolinea['id_aerolinea'],
                'vuelos_count': most_common_aerolinea['aerolinea_count'],
                'nombre_aerolinea': name_aerolinea['nombre_aerolinea'],
            }
            return Response(result)
        else:
            return Response({"error": "No hay vuelos en la base de datos."}, status=404)

#3\. ¿En qué día se ha tenido mayor número de vuelos?
class DiasConMayorVuelosView(APIView):
    def get(self, request, *args, **kwargs):
        #Obtenemos la fecha con más movimientos de vuelo
        most_common_vuelos = (
            Vuelos.objects.values('dia')
            .annotate(aerolinea_count=Count('dia'))
            .order_by('-dia')
            .first()
        )
        #Generamos la salida de datos
        if most_common_vuelos:
            result = {
                'dia_mayor_vuelos': most_common_vuelos['dia'],
            }
            return Response(result)
        else:
            return Response({"error": "No hay vuelos en la base de datos."}, status=404)

#4\. 4\. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?
class MasDeDosVuelosPorDiaView(APIView):
    def get(self, request, *args, **kwargs):
        #Obtener ID de Aerolineas con más de dos vuelos al día
        queryset = Vuelos.objects.values('id_aerolinea')\
            .annotate(vuelo_count=Count('id_aerolinea'))\
            .filter(vuelo_count__gt=2)
        #Convertimos a tipo lista para que los ids
        aerolineas_con_mas_de_dos_registros = list(queryset.values_list('id_aerolinea', flat=True).distinct())


        #Agregamos los Id de los Aeropuertos enla consulta
        aerolinea_ids = request.query_params.getlist('aerolinea_ids', aerolineas_con_mas_de_dos_registros)
        if not aerolinea_ids:
            return Response({"error": "Se deben proporcionar IDs de aerolíneas"}, status=400)
        
        # Convertir los IDs a enteros
        aerolinea_ids = [int(id) for id in aerolinea_ids]

        # Filtrar los vuelos
        aerolineas = Aerolineas.objects.filter(id_aerolinea__in=aerolinea_ids)
        serializer = AerolineasSerializer(aerolineas, many=True)

        return Response(serializer.data)