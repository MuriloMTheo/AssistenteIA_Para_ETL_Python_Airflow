# 🤖 METL AI Coder — Assistente de Programação ETL & Python Avançado

![Interface do Assistente](https://github.com/user-attachments/assets/d0932f52-69f4-44d8-9f6a-95e6dcdada38)

> Assistente de IA especializado em **Python** e **pipelines ETL**, construído com Groq API + Streamlit. Tire dúvidas sobre extração, transformação e carga de dados, além de sintaxe Python, funções built-in, boas práticas e muito mais — tudo em tempo real via LLM.

---

## ✨ Funcionalidades

- 💬 Chat interativo com LLM via **Groq API** (baixa latência)
- 🐍 Foco em **Python** para engenharia e análise de dados
- 🔄 Suporte a dúvidas de **ETL**: extração, transformação e carga
- ⚡ Interface web leve e responsiva com **Streamlit**
- 🧠 Respostas contextuais com exemplos de código

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Função |
|---|---|
| Python 3.13 | Linguagem principal |
| Streamlit | Interface web |
| Groq API | Backend LLM (inferência rápida) |
| Conda | Gerenciamento de ambiente |

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/MuriloMTheo/AssistenteIA_Para_ETL_Python_Airflow.git
cd AssistenteIA
```

### 2. Crie e ative o ambiente virtual

```bash
conda create --name assistenteia python=3.13
conda activate dsaec1
```

> No Linux/macOS, use `source activate assistenteia` se necessário.

### 3. Instale as dependências

```bash
conda install pip
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
streamlit run assistente.py
```

A interface abrirá automaticamente no seu navegador em `http://localhost:8501`.

### 5. Insira sua chave da Groq API

Na própria interface da aplicação, há um campo dedicado para inserir sua **Groq API Key**. Basta colá-la lá e começar a usar.

> Obtenha sua chave gratuita em [console.groq.com](https://console.groq.com)

---

## 💡 Exemplos de uso

Experimente perguntar ao assistente:

- `Como crio um hello world em Python?`
- `Qual a sintaxe de um loop for em Python?`
- `Como eu uso a função map em Python? Me dê um exemplo com lambda.`
- `Como fazer uma conexão com banco de dados PostgreSQL usando SQLAlchemy?`
- `Qual a diferença entre ETL e ELT? Me dê um exemplo prático em Python.`
- `Como usar pandas para transformar e limpar dados de um CSV?`
- `Como paralelizar um pipeline ETL com Python?`

---

## 🗂️ Estrutura do projeto

```
📁 seu-repositorio/
├── dsa_assistente.py      # Aplicação principal (Streamlit)
├── requirements.txt       # Dependências do projeto    
└── README.md
```

---


## 🧹 Desativando e removendo o ambiente

```bash
conda deactivate
conda remove --name assistenteia --all
```

---

## 📚 Referências

- [Documentação Streamlit](https://docs.streamlit.io)
- [Groq API Docs](https://console.groq.com/docs)
- [Python Docs](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

> Projeto desenvolvido como estudo de caso no curso **DSA — Data Science Academy**.
