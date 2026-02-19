import os
import streamlit as st
from groq import Groq

# Configuracao de estrutura do site
st.set_page_config(
    page_title='METL AI Coder',
    page_icon='ⓜ',
    layout='wide',
    initial_sidebar_state='expanded'
)

CUSTOM_PROMPT = """"
Você é um Assistente Especialista em Desenvolvimento ETL, com foco principal em SQL Server e integração de dados corporativos, 
além de possuir um vasto conhecimento e prática com desenvolvimento em Python e Airflow.
Você atua como um engenheiro de dados sênior, com experiência sólida em ambientes corporativos, ERPs e grandes volumes de dados.

🧠 Conhecimentos obrigatórios:
SQL Server (T-SQL avançado, CTEs, Window Functions, índices, planos de execução, performance tuning)
ETL / ELT (extração, transformação e carga de dados)
SSIS / Azure Data Factory (ou equivalentes)
Modelagem de dados (OLTP, OLAP, Star Schema, Snowflake)
Data Warehouse e Data Mart
Qualidade de dados, validações e tratamento de erros
Controle de cargas (full, incremental, CDC, SCD tipos 1, 2 e 3)
Logs, auditoria e rastreabilidade
Versionamento e governança de dados
Boas práticas de segurança (acessos, dados sensíveis, LGPD)

🧾 Conhecimento em ERP:
Entendimento de processos de negócio:
Financeiro (contas a pagar/receber, faturamento, impostos)
Compras e estoque
Vendas
Produção
Cadastros mestres (clientes, fornecedores, produtos)
Capacidade de interpretar tabelas de ERP, mesmo sem documentação clara
Experiência com integrações entre ERP, Data Warehouse e BI

🛠️ Forma de atuação:
Sempre que possível, sugira soluções práticas e aplicáveis
Priorize performance, clareza e manutenção
Explique o porquê das decisões técnicas
Quando fizer sentido, apresente:
SQL otimizado
Estrutura de tabelas
Fluxos ETL
Diagramas lógicos (descritos em texto)
Alerte sobre riscos comuns (joins errados, duplicidade, impacto no ERP)

🗣️ Comunicação:
Linguagem clara, técnica e objetiva
Pode usar exemplos reais de cenários corporativos
Ajuste o nível de explicação conforme o usuário (iniciante, pleno ou sênior)
Faça perguntas apenas quando necessário para entender regras de negócio

🎯 Objetivo final:
Ajudar a resolver problemas reais de ETL e dados corporativos, garantindo:
Integridade dos dados
Performance
Escalabilidade
Alinhamento com processos de ERP e negócio

🔥 Estilo de resposta:
Sempre dê uma resposta explicativa ao usuário e somente depois pergunte se ele precisa de ajuda ou se quer que você gere o código.
"""

# sidebar
with st.sidebar:
    st.title()
    st.markdown()

    # Inserir a chave API Groq
    groq_api_key = st.text_input(
        'Insira sua API Key Groq',
        type="password",
        help="Adquira sua API Key em https://console.groq.com/keys"
    )

    st.markdown("---")
    st.markdown(
        "Projeto desenvolvido com o objetivo de estudo sobre Streamlit e criação de um agente de IA!")

    st.markdown("---")
    st.markdown("🐱 [Acesse meu GitHub](https://github.com/MuriloMTheo)")

# titulo
st.title('METL AI CODER')
st.title('Seu Assistente Pessoal em Desenvolvimento ETL 🎲')
# texto auxiliar
st.caption('Faça sua pergunta sobre algum processamento ETL e obtenha código, explicações e referências.')

# iniciar histórico de msgs na sessão, SE não existir
if "messages" not in st.session_state:
    st.session_state.messages = []
# exibir msgs armazenadas na session
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

client = None

# user enviou a api key
if groq_api_key:
    try:  # funcao Groq
        client = Groq(api_key=groq_api_key)

    except Exception as e:
        st.sidebar.error(f'Erro ao inicializar o cliente Groq: {e}')
        st.stop()
elif st.session_state.messages:
    st.warning('Por favor, insira sua API Key da Groq na barra lateral!')

if prompt := st.chat_input('Digite aqui sua dúvida sobre Python, SQL, ou outros processamentos ETL.'):
    if not client:  # ou seja, nao colocou a chave da api ainda
        st.warning(
            'Por favor, insira sua API Key da Groq na barra lateral para começar!')
        st.stop()

    st.session_state.messages.append(
        {"role": "user", "content": prompt})  # armazena a msg do user

    with st.chat_message("user"):
        st.markdown(prompt)  # exibindo msg do user

    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        # para cada msg digitada pelo user, adicione ela ao prompt definido inicialmente
        messages_for_api.append(msg)

    with st.chat_message("assistant"):
        with st.spinner("Analisando perguntando..."):
            try:
                # chamado da api groq pra gerar resposta
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model="openai/gpt-oss-20b",
                    temperature=0.7,
                    max_tokens=2048
                )
                # extraindo resposta
                AI_resposta = chat_completion.choices[0].message.content

                st.markdown(AI_resposta)  # exibe no streamlit
                st.session_state.messages.append(
                    # armazena resposta
                    {"role": "assistent", "content": AI_resposta})

            except Exception as e:
                st.error(
                    f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")
