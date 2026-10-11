import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


def ler_numero(texto):
    """Converte texto em número aceitando vírgula ou ponto como decimal."""
    return float(texto.strip().replace(",", "."))


def formata(valor):
    """Formata no padrão brasileiro: 1.234,56"""
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sassari Calculator")
        self.geometry("420x560")
        self.resizable(False, False)

        ctk.CTkLabel(
            self, text="Calculadora de Juros",
            font=ctk.CTkFont(size=22, weight="bold"),
        ).pack(pady=(24, 12))

        self.tipo = ctk.CTkSegmentedButton(
            self, values=["Juros Simples", "Juros Compostos"]
        )
        self.tipo.set("Juros Simples")
        self.tipo.pack(pady=(0, 16))

        self.capital = self._campo("Capital (R$)")
        self.taxa = self._campo("Taxa de juros (% por período)")
        self.tempo = self._campo("Tempo (nº de períodos)")

        botoes = ctk.CTkFrame(self, fg_color="transparent")
        botoes.pack(pady=(8, 4))
        ctk.CTkButton(botoes, text="Calcular", command=self.calcular, width=140).grid(
            row=0, column=0, padx=6
        )
        ctk.CTkButton(
            botoes, text="Limpar", command=self.limpar, width=140,
            fg_color="gray40", hover_color="gray30",
        ).grid(row=0, column=1, padx=6)

        self.erro = ctk.CTkLabel(self, text="", text_color="#e5484d")
        self.erro.pack(pady=(4, 0))

        quadro = ctk.CTkFrame(self)
        quadro.pack(padx=30, pady=16, fill="x")
        self.res_juros = ctk.CTkLabel(
            quadro, text="Juros: —", font=ctk.CTkFont(size=16)
        )
        self.res_juros.pack(pady=(14, 4))
        self.res_montante = ctk.CTkLabel(
            quadro, text="Montante: —", font=ctk.CTkFont(size=16, weight="bold")
        )
        self.res_montante.pack(pady=(4, 14))

        self.bind("<Return>", lambda _e: self.calcular())

    def _campo(self, rotulo):
        ctk.CTkLabel(self, text=rotulo, anchor="w").pack(padx=40, fill="x")
        entrada = ctk.CTkEntry(self, width=340)
        entrada.pack(padx=40, pady=(2, 12))
        return entrada

    def calcular(self):
        self.erro.configure(text="")
        try:
            cap = ler_numero(self.capital.get())
            taxa = ler_numero(self.taxa.get()) / 100
            tempo = ler_numero(self.tempo.get())
        except ValueError:
            self.erro.configure(text="Preencha todos os campos com números (ex.: 1500 ou 2,5).")
            return

        if cap < 0 or tempo < 0:
            self.erro.configure(text="Capital e tempo não podem ser negativos.")
            return

        if self.tipo.get() == "Juros Simples":
            juros = cap * taxa * tempo
            montante = cap + juros
        else:
            montante = cap * pow(1 + taxa, tempo)
            juros = montante - cap

        self.res_juros.configure(text=f"Juros: R$ {formata(juros)}")
        self.res_montante.configure(text=f"Montante: R$ {formata(montante)}")

    def limpar(self):
        for campo in (self.capital, self.taxa, self.tempo):
            campo.delete(0, "end")
        self.erro.configure(text="")
        self.res_juros.configure(text="Juros: —")
        self.res_montante.configure(text="Montante: —")
        self.capital.focus()


if __name__ == "__main__":
    App().mainloop()

