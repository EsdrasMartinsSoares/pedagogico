# Função para verificar os critérios de Framingham
def verificar_insuficiencia_cardiaca(criterios_maiores, criterios_menores):
    # Contar os critérios maiores e menores
    contagem_maiores = sum(criterios_maiores.values())
    contagem_menores = sum(criterios_menores.values())
    
    # Verificar se atende aos critérios de Framingham
    if contagem_maiores >= 2 or (contagem_maiores >= 1 and contagem_menores >= 2):
        return "O paciente tem insuficiência cardíaca."
    else:
        return "O paciente não tem insuficiência cardíaca."

# Informações do paciente (exemplo)
criterios_maiores = {
    "Dispneia paroxística noturna": True,
    "Turgência jugular": True,
    "Cardiomegalia à radiografia de tórax": False,
    "Edema agudo de pulmão": True,
    "Terceira bulha (galope)": False,
    "Aumento da pressão venosa central (> 16 cm H2O no átrio direito)": False,
    "Refluxo hepatojugular": False,
    "Perda de peso > 4,5 kg em 5 dias em resposta ao tratamento": False
}

criterios_menores = {
    "Edema de tornozelos bilateral": True,
    "Tosse noturna": False,
    "Dispneia a esforços ordinários": True,
    "Hepatomegalia": False,
    "Derrame pleural": False,
    "Diminuição da capacidade funcional em um terço da máxima registrada previamente": False,
    "Taquicardia (FC > 120 bpm)": False
}

# Verificar insuficiência cardíaca
resultado = verificar_insuficiencia_cardiaca(criterios_maiores, criterios_menores)
print(resultado)





# Aqui é o fromulário
import tkinter as tk
from tkinter import messagebox

def verificar_insuficiencia_cardiaca():
    criterios_maiores = {
        "Dispneia paroxística noturna": var_dispneia.get(),
        "Turgência jugular": var_turgencia.get(),
        "Cardiomegalia à radiografia de tórax": var_cardiomegalia.get(),
        "Edema agudo de pulmão": var_edema.get(),
        "Terceira bulha (galope)": var_bulha.get(),
        "Aumento da pressão venosa central (> 16 cm H2O no átrio direito)": var_pressao.get(),
        "Refluxo hepatojugular": var_refluxo.get(),
        "Perda de peso > 4,5 kg em 5 dias em resposta ao tratamento": var_perda_peso.get()
    }

    criterios_menores = {
        "Edema de tornozelos bilateral": var_edema_tornozelos.get(),
        "Tosse noturna": var_tosse.get(),
        "Dispneia a esforços ordinários": var_dispneia_esforcos.get(),
        "Hepatomegalia": var_hepatomegalia.get(),
        "Derrame pleural": var_derrame.get(),
        "Diminuição da capacidade funcional em um terço da máxima registrada previamente": var_capacidade.get(),
        "Taquicardia (FC > 120 bpm)": var_taquicardia.get()
    }

    contagem_maiores = sum(criterios_maiores.values())
    contagem_menores = sum(criterios_menores.values())

    if contagem_maiores >= 2 or (contagem_maiores >= 1 and contagem_menores >= 2):
        messagebox.showinfo("Resultado", "O paciente tem insuficiência cardíaca.")
    else:
        messagebox.showinfo("Resultado", "O paciente não tem insuficiência cardíaca.")

# Interface gráfica
root = tk.Tk()
root.title("Diagnóstico de Insuficiência Cardíaca")

# Variáveis
var_dispneia = tk.BooleanVar()
var_turgencia = tk.BooleanVar()
var_cardiomegalia = tk.BooleanVar()
var_edema = tk.BooleanVar()
var_bulha = tk.BooleanVar()
var_pressao = tk.BooleanVar()
var_refluxo = tk.BooleanVar()
var_perda_peso = tk.BooleanVar()

var_edema_tornozelos = tk.BooleanVar()
var_tosse = tk.BooleanVar()
var_dispneia_esforcos = tk.BooleanVar()
var_hepatomegalia = tk.BooleanVar()
var_derrame = tk.BooleanVar()
var_capacidade = tk.BooleanVar()
var_taquicardia = tk.BooleanVar()

# Criação dos campos do formulário
tk.Checkbutton(root, text="Dispneia paroxística noturna", variable=var_dispneia).pack()
tk.Checkbutton(root, text="Turgência jugular", variable=var_turgencia).pack()
tk.Checkbutton(root, text="Cardiomegalia à radiografia de tórax", variable=var_cardiomegalia).pack()
tk.Checkbutton(root, text="Edema agudo de pulmão", variable=var_edema).pack()
tk.Checkbutton(root, text="Terceira bulha (galope)", variable=var_bulha).pack()
tk.Checkbutton(root, text="Aumento da pressão venosa central (> 16 cm H2O no átrio direito)", variable=var_pressao).pack()
tk.Checkbutton(root, text="Refluxo hepatojugular", variable=var_refluxo).pack()
tk.Checkbutton(root, text="Perda de peso > 4,5 kg em 5 dias em resposta ao tratamento", variable=var_perda_peso).pack()

tk.Checkbutton(root, text="Edema de tornozelos bilateral", variable=var_edema_tornozelos).pack()
tk.Checkbutton(root, text="Tosse noturna", variable=var_tosse).pack()
tk.Checkbutton(root, text="Dispneia a esforços ordinários", variable=var_dispneia_esforcos).pack()
tk.Checkbutton(root, text="Hepatomegalia", variable=var_hepatomegalia).pack()
tk.Checkbutton(root, text="Derrame pleural", variable=var_derrame).pack()
tk.Checkbutton(root, text="Diminuição da capacidade funcional em um terço da máxima registrada previamente", variable=var_capacidade).pack()
tk.Checkbutton(root, text="Taquicardia (FC > 120 bpm)", variable=var_taquicardia).pack()

tk.Button(root, text="Verificar Insuficiência Cardíaca", command=verificar_insuficiencia_cardiaca).pack()

root.mainloop()
