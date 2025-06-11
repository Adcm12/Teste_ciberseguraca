# cliente_gui.py
import socket
import tkinter as tk

def enviar_mensagem():
    destino = ip_entry.get()
    porta = int(porta_entry.get())
    mensagem = msg_entry.get()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(mensagem.encode(), (destino, porta))
    status_label.config(text="Mensagem enviada!", fg="green")
    msg_entry.delete(0, tk.END)
    
# Criar janela
janela = tk.Tk()
janela.title("Cliente UDP - Segurança da Informação")
tk.Label(janela, text="IP do Servidor:").pack()
ip_entry = tk.Entry(janela, width=30)
ip_entry.pack()
tk.Label(janela, text="Porta:").pack()
porta_entry = tk.Entry(janela, width=30)
porta_entry.insert(0, "4444")
porta_entry.pack()
tk.Label(janela, text="Mensagem:").pack()
msg_entry = tk.Entry(janela, width=50)
msg_entry.pack()
enviar_btn = tk.Button(janela, text="Enviar", command=enviar_mensagem)
enviar_btn.pack(pady=5)
status_label = tk.Label(janela, text="")
status_label.pack()
janela.mainloop()
# Nota: Certifique-se de que o servidor está rodando antes de executar este cliente.
# Nota: O IP do servidor deve ser acessível a partir do cliente