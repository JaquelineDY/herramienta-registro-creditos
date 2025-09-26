import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_routes():
    print("=== Probando las correcciones de la API ===\n")
    
    # Probar ruta raíz (antes daba 404)
    print("1. Probando ruta raíz (/):")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Probar POST válido a /creditos
    print("2. Probando POST válido a /creditos:")
    credito_data = {
        "cliente": "Juan Pérez",
        "monto": 10000.50,
        "tasa_interes": 12.5,
        "plazo": 24,
        "fecha_otorgamiento": "2025-09-23"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/creditos", json=credito_data)
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Probar POST inválido a /creditos (campos faltantes)
    print("3. Probando POST inválido a /creditos (campos faltantes):")
    credito_invalido = {
        "cliente": "María García",
        "monto": 5000
        # Faltan: tasa_interes, plazo, fecha_otorgamiento
    }
    
    try:
        response = requests.post(f"{BASE_URL}/creditos", json=credito_invalido)
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Probar GET /creditos
    print("4. Probando GET /creditos:")
    try:
        response = requests.get(f"{BASE_URL}/creditos")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")

if __name__ == "__main__":
    test_routes()