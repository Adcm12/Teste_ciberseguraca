# servidor_gui.py
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
HOST = ''
PORTA = 4444

def iniciar_servidor():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORTA))
    log.insert(tk.END, f"[+] Servidor escutando na porta {PORTA}\n")
    
    while True:
        dados, endereco = s.recvfrom(1024)
        mensagem = dados.decode()
        log.insert(tk.END, f"[{endereco}] {mensagem}\n")
        log.see(tk.END)
    
# Criar janela
janela = tk.Tk()
janela.title("Servidor UDP - Segurança da Informação")
log = scrolledtext.ScrolledText(janela, width=60, height=20)
log.pack(padx=10, pady=10)
thread = threading.Thread(target=iniciar_servidor, daemon=True)
thread.start()
janela.mainloop()