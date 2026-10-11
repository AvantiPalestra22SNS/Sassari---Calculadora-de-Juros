<p align="center">
  <img src="SassariLogo.png" alt="Sassari Calculator" width="320">
</p>

<p align="center">
  Calculadora de <b>juros simples e compostos</b> para Windows, feita em Python.
</p>

<p align="center">
  <img src="docs/screenshot.png" alt="Tela do Sassari Calculator" width="360">
</p>

## Sobre o projeto

A **Sassari Calculator** calcula o valor dos juros e o montante final de uma aplicação ou dívida, tanto no regime de **juros simples** quanto de **juros compostos**. Nasceu como um script de console e evoluiu para um aplicativo desktop com interface gráfica, ícone próprio, tema claro/escuro e instalador para Windows.

## Funcionalidades

- Cálculo de juros simples e compostos, com alternância em um clique
- Aceita vírgula ou ponto como separador decimal (ex.: `2,5` ou `2.5`)
- Validação dos campos, com mensagens de erro na própria janela
- Resultados formatados no padrão brasileiro (`R$ 1.234,56`)
- Tema claro e escuro, com botão para alternar
- Instalador `Setup.exe` gerado automaticamente

## Como instalar

1. Acesse a página de [Releases](../../releases).
2. Baixe o arquivo `SassariCalculator-Setup.exe` da versão mais recente.
3. Execute o instalador e siga as instruções.

> O Windows pode exibir um aviso de "aplicativo desconhecido", porque o instalador não possui assinatura digital. Clique em **Mais informações → Executar assim mesmo**.

## Como funciona o cálculo

| Regime | Montante | Juros |
|---|---|---|
| Simples | `M = C × (1 + i × t)` | `J = M − C` |
| Compostos | `M = C × (1 + i)^t` | `J = M − C` |

Onde `C` é o capital, `i` é a taxa (em decimal), `t` é o tempo e `M` é o montante. A taxa e o tempo devem estar na mesma unidade (por exemplo, taxa ao mês e tempo em meses).

## Rodando o código-fonte

Requisitos: Python 3.10 ou superior.

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd https://github.com/AvantiPalestra22SNS/Sassari---Calculadora-de-Juros
pip install customtkinter pillow
python SassariCalculator.py
```

No Linux, pode ser necessário instalar o Tkinter antes: `sudo apt install python3-tk`.

## Tecnologias

- [Python](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) para a interface
- [Pillow](https://python-pillow.org/) para as imagens
- [PyInstaller](https://pyinstaller.org/) para gerar o executável
- [Inno Setup](https://jrsoftware.org/isinfo.php) para gerar o instalador
- [GitHub Actions](https://docs.github.com/actions) para compilar tudo automaticamente

## Estrutura do projeto

```
├── SassariCalculator.py      # código do aplicativo
├── SassariCalculator.iss     # script do instalador (Inno Setup)
├── SassariIcon.ico           # ícone do aplicativo
├── SassariLogo.png           # logo exibido na interface
├── docs/screenshot.png       # imagem usada neste README
└── .github/workflows/
    └── build.yml             # gera o .exe e o instalador
```

## Autor

Desenvolvido por **AvantiPalestra22SNS**.
