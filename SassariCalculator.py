import os
import sys

import customtkinter as ctk
from PIL import Image

# ---------------------------------------------------------------
# Paleta (cor no tema claro, cor no tema escuro), baseada no logo
# ---------------------------------------------------------------
VERDE = "#00BF63"
VERDE_HOVER = "#00A356"
LIMAO = "#C1FF72"
TEXTO_SOBRE_VERDE = "#04230F"

COR_FUNDO = ("#F2FAF5", "#11171C")
COR_CARD = ("#FFFFFF", "#1A222A")
COR_BORDA = ("#BFE8D0", "#2A3A33")
COR_TEXTO = ("#14261C", "#E8F1EC")
COR_TEXTO_SEC = ("#4A6556", "#9DB5A7")
COR_DESTAQUE = ("#00763B", LIMAO)
COR_ERRO = ("#C62828", "#FF6B6B")

# Fonte do Windows. Em outros sistemas (ex.: Linux Mint) o Tk usa uma padrão.
FONTE = "Segoe UI"

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


def ler_numero(texto):
    """Converte texto em número aceitando vírgula ou ponto como decimal."""
    return float(texto.strip().replace(",", "."))


def formata(valor):
    """Formata no padrão brasileiro: 1.234,56"""
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def caminho_recurso(nome):
    """Localiza arquivos tanto rodando o .py quanto dentro do .exe."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, nome)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sassari Calculator")
        try:
            self.iconbitmap(caminho_recurso("SassariIcon.ico"))
        except Exception:
            pass
        self.geometry("420x740")
        self.resizable(False, False)
        self.configure(fg_color=COR_FUNDO)

        # Fontes (precisam ser criadas depois da janela principal)
        self.f_sub = ctk.CTkFont(family=FONTE, size=15)
        self.f_rotulo = ctk.CTkFont(family=FONTE, size=13)
        self.f_entrada = ctk.CTkFont(family=FONTE, size=15)
        self.f_botao = ctk.CTkFont(family=FONTE, size=15, weight="bold")
        self.f_juros = ctk.CTkFont(family=FONTE, size=18)
        self.f_montante = ctk.CTkFont(family=FONTE, size=26, weight="bold")
        self.f_erro = ctk.CTkFont(family=FONTE, size=12)

        self._logo()

        ctk.CTkLabel(
            self, text="Calculadora de Juros",
            font=self.f_sub, text_color=COR_TEXTO_SEC,
        ).pack(pady=(4, 14))

        self.tipo = ctk.CTkSegmentedButton(
            self, values=["Juros Simples", "Juros Compostos"],
            font=self.f_botao, height=36,
            fg_color=COR_BORDA,
            selected_color=(VERDE, "#00894A"),
            selected_hover_color=(VERDE_HOVER, "#007A41"),
            unselected_color=("#D6EDDF", "#222C34"),
            unselected_hover_color=("#C4E3D2", "#2C3943"),
            text_color=(TEXTO_SOBRE_VERDE, "#FFFFFF"),
        )
        self.tipo.set("Juros Simples")
        self.tipo.pack(pady=(0, 16))

        self.capital = self._campo("Capital (R$)")
        self.taxa = self._campo("Taxa de juros (% ao mês)")
        self.tempo = self._campo("Tempo/período (meses)")

        botoes = ctk.CTkFrame(self, fg_color="transparent")
        botoes.pack(pady=(10, 6))
        ctk.CTkButton(
            botoes, text="Calcular", command=self.calcular,
            width=150, height=40, corner_radius=10, font=self.f_botao,
            fg_color=VERDE, hover_color=VERDE_HOVER, text_color=TEXTO_SOBRE_VERDE,
        ).grid(row=0, column=0, padx=6)
        ctk.CTkButton(
            botoes, text="Limpar", command=self.limpar,
            width=150, height=40, corner_radius=10, font=self.f_botao,
            fg_color="transparent", border_width=2, border_color=VERDE,
            text_color=COR_TEXTO, hover_color=("#DDF3E6", "#1F2B26"),
        ).grid(row=0, column=1, padx=6)

        self.erro = ctk.CTkLabel(
            self, text="", font=self.f_erro, text_color=COR_ERRO, wraplength=340
        )
        self.erro.pack(pady=(4, 0))

        quadro = ctk.CTkFrame(
            self, fg_color=COR_CARD, border_width=2,
            border_color=COR_BORDA, corner_radius=14,
        )
        quadro.pack(padx=40, pady=14, fill="x")

        ctk.CTkLabel(
            quadro, text="Juros", font=self.f_rotulo, text_color=COR_TEXTO_SEC
        ).pack(pady=(14, 0))
        self.res_juros = ctk.CTkLabel(
            quadro, text="R$ —", font=self.f_juros, text_color=COR_TEXTO
        )
        self.res_juros.pack()

        ctk.CTkLabel(
            quadro, text="Montante", font=self.f_rotulo, text_color=COR_TEXTO_SEC
        ).pack(pady=(10, 0))
        self.res_montante = ctk.CTkLabel(
            quadro, text="R$ —", font=self.f_montante, text_color=COR_DESTAQUE
        )
        self.res_montante.pack(pady=(0, 14))

        self.chave_tema = ctk.CTkSwitch(
            self, text="Modo escuro", command=self._alternar_tema,
            font=self.f_rotulo, text_color=COR_TEXTO_SEC, progress_color=VERDE,
        )
        if ctk.get_appearance_mode() == "Dark":
            self.chave_tema.select()
        self.chave_tema.pack(pady=(4, 16))

        self.bind("<Return>", lambda _e: self.calcular())

    def _logo(self):
        """Mostra o logo no topo. Se o arquivo não existir, segue sem ele."""
        try:
            img = Image.open(caminho_recurso("SassariLogo.png"))
            largura = 280
            altura = round(largura * img.height / img.width)
            self.logo = ctk.CTkImage(
                light_image=img, dark_image=img, size=(largura, altura)
            )
            ctk.CTkLabel(self, image=self.logo, text="").pack(pady=(18, 0))
        except Exception:
            pass

    def _campo(self, rotulo):
        ctk.CTkLabel(
            self, text=rotulo, anchor="w",
            font=self.f_rotulo, text_color=COR_TEXTO_SEC,
        ).pack(padx=40, fill="x")
        entrada = ctk.CTkEntry(
            self, width=340, height=38, font=self.f_entrada,
            corner_radius=10, border_width=2,
            fg_color=COR_CARD, border_color=COR_BORDA, text_color=COR_TEXTO,
        )
        entrada.pack(padx=40, pady=(2, 12))
        return entrada

    def _alternar_tema(self):
        ctk.set_appearance_mode("dark" if self.chave_tema.get() else "light")

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

        self.res_juros.configure(text=f"R$ {formata(juros)}")
        self.res_montante.configure(text=f"R$ {formata(montante)}")

    def limpar(self):
        for campo in (self.capital, self.taxa, self.tempo):
            campo.delete(0, "end")
        self.erro.configure(text="")
        self.res_juros.configure(text="R$ —")
        self.res_montante.configure(text="R$ —")
        self.capital.focus()


if __name__ == "__main__":
    App().mainloop()
