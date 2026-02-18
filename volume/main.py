import tkinter as tk
from tkinter import ttk
import numpy as np
import sounddevice as sd
import threading

# Função para tocar o som
def play_sound():
    try:
        duration = int(duration_entry.get())
    except ValueError:
        return

    freq = freq_slider.get()
    volume = volume_slider.get() / 100.0

    fs = 44100  # taxa de amostragem
    t = np.linspace(0, duration, int(fs * duration), False)
    tone = np.sin(2 * np.pi * freq * t) * volume

    sd.play(tone, fs)
    sd.wait()

# Executa o som em thread separada para não travar a UI
def play_thread():
    threading.Thread(target=play_sound, daemon=True).start()

# Validação para aceitar apenas inteiros
def only_int(P):
    return P.isdigit() or P == ""

# Janela principal
root = tk.Tk()
root.title("Gerador de Som")
root.geometry("400x300")

# Volume
volume_label = ttk.Label(root, text="Volume")
volume_label.pack()

volume_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal")
volume_slider.set(50)
volume_slider.pack(fill="x", padx=20)

# Frequência
freq_label = ttk.Label(root, text="Frequência (Hz)")
freq_label.pack()

freq_slider = ttk.Scale(root, from_=50, to=10000, orient="horizontal")
freq_slider.set(440)
freq_slider.pack(fill="x", padx=20)

# Duração
validate_cmd = root.register(only_int)

duration_label = ttk.Label(root, text="Duração (segundos)")
duration_label.pack()

duration_entry = ttk.Entry(root, validate="key", validatecommand=(validate_cmd, "%P"))
duration_entry.insert(0, "1")
duration_entry.pack()

# Botão Play
play_button = ttk.Button(root, text="Play", command=play_thread)
play_button.pack(pady=20)

root.mainloop()
