import random
import ipaddress
from scapy.all import IPv6, ICMPv6EchoRequest, Raw, send

def generar_ipv6_falsa():
    """
    Genera una dirección IPv6 global unicast aleatoria.
    """

    return ":".join(f"{random.randint(0, 65535):x}" for _ in range(8))

def validar_ipv6(ip_str):

    try:
        ipaddress.IPv6Address(ip_str)
        return True
    except ipaddress.AddressValueError:
        return False

def enviar_paquete_spoof_ipv6(ipv6_destino, ipv6_falsa):
    # --- MENSAJE PERSONALIZADO ---
    # Crea un payload único que puedas buscar fácilmente en Wireshark.
    payload_personalizado = "PAQUETE_ADRIAN_2025_TEST"
    
    if not validar_ipv6(ipv6_falsa) or not validar_ipv6(ipv6_destino):
        print("Error: Una de las direcciones IP no es válida.")
        return

    print(f"Intentando enviar paquete con payload: '{payload_personalizado}'")

    # --- CONSTRUCCIÓN DEL PAQUETE CON PAYLOAD ---
    # Añadimos la capa Raw() al final para incluir nuestro mensaje.
    paquete = IPv6(src=ipv6_falsa, dst=ipv6_destino) / ICMPv6EchoRequest() / Raw(load=payload_personalizado)
    
    # Muestra un resumen del paquete que se va a enviar
    print("Resumen del paquete a enviar:")
    paquete.show()
    
    try:
        send(paquete, verbose=False)
        print(f"\nPaquete enviado a {ipv6_destino} desde la IP falsa {ipv6_falsa}")
    except OSError as e:
        print(f"Error de sistema al enviar el paquete: {e}")
        print("Asegúrate de ejecutar este script con privilegios de administrador (sudo).")


# --- Ejemplo de uso ---
ipv6_de_prueba_en_tu_red = "::1"
ipv6_falsa = generar_ipv6_falsa()
print(f"IP Falsa Generada: {ipv6_falsa}")

enviar_paquete_spoof_ipv6(ipv6_de_prueba_en_tu_red, ipv6_falsa)