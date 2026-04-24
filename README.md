# 🔐 Gerador de Senhas Aleatórias

> Uma aplicação desktop moderna e segura para geração de senhas, construída com Python e CustomTkinter.

---

## 📸 Visão Geral

O **Gerador de Senhas Aleatórias** é uma ferramenta desktop com interface gráfica intuitiva que combina palavras-chave memoráveis com sequências aleatórias criptograficamente seguras — criando senhas fortes, mas humanas o suficiente para lembrar a origem.

---

## ✨ Funcionalidades

- 🎲 **Geração criptograficamente segura** — usa o módulo `secrets` do Python, adequado para fins de segurança real
- 🧩 **Senhas com palavra-chave** — cada senha é prefixada com uma palavra aleatória da lista `lista_palavras_chave`, tornando-as mais fáceis de identificar
- 📏 **Tamanho configurável** — slider de 8 a 32 caracteres para a parte aleatória da senha
- 🔠 **Composição personalizável** via switches:
  - Letras (maiúsculas e minúsculas)
  - Números
  - Símbolos / pontuações
- 📋 **Copiar com um clique** — copia a senha gerada diretamente para a área de transferência
- 💬 **Feedback visual** — confirmação instantânea ao copiar a senha

---

## 🧠 Como Funciona

A senha gerada segue o formato:

```
<palavra-chave>-<sequência-aleatória>
```

**Exemplo:**
```
montanha-aB3$kR9p
```

1. Uma **palavra aleatória** é escolhida da lista `lista_palavras_chave` usando `secrets.choice()`
2. Um **alfabeto** é montado dinamicamente com base nos switches ativados pelo usuário
3. A **sequência aleatória** é gerada caractere a caractere com `secrets.choice()` sobre o alfabeto
4. As duas partes são unidas com um hífen `-`

> ⚠️ Se nenhum switch estiver ativado, o gerador usa letras por padrão para evitar senhas vazias.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| `Python 3.x` | Linguagem base |
| `customtkinter` | Interface gráfica moderna |
| `secrets` | Geração criptograficamente segura |
| `string` | Conjuntos de caracteres (letras, números, símbolos) |
| `webbrowser` | Abertura de links externos |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- `customtkinter` instalado

### Instalação

```bash
# Clone o repositório
git clone https://github.com/miguelsfrds/Password_Generator.py.git
cd Password_Generator.py

# Instale as dependências
pip install customtkinter
```

### Execução

```bash
python Password_Generator.py
```

---

## 📁 Estrutura do Projeto

```
gerador-de-senhas/
│
├── password_generator.py    # Arquivo principal — interface e lógica
├── lista_palavras_chave.py  # Lista de palavras usadas como prefixo
└── README.md
```

---

## 🔒 Por que usar `secrets` em vez de `random`?

O módulo `random` do Python **não é adequado para criptografia** — ele usa um gerador pseudoaleatório previsível. O módulo `secrets` foi criado especificamente para geração de tokens, senhas e dados sensíveis, utilizando fontes de entropia do sistema operacional, tornando os resultados **imprevisíveis e seguros**.

---

## 📌 Melhorias Futuras

- [ ] Indicador visual de força da senha
- [ ] Histórico de senhas geradas na sessão
- [ ] Opção de exportar senhas para arquivo `.txt`
- [ ] Tema claro / escuro configurável
- [ ] Suporte a múltiplos idiomas para palavras-chave

---

## 👨‍💻 Autor

Desenvolvido por **[@miguelsfrds](https://github.com/miguelsfrds)**

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
