import requests

#Función base para hacer peticiones a servicios externos
def get_stackexchange(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error en la solicitud solicitud: {e}")
        return None