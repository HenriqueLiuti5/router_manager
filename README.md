# Router Manager

Sistema web para gerenciamento e monitoramento de roteadores e dispositivos IoT. Desenvolvido em Python com Flask, permite o cadastro de equipamentos, verificação de status online/offline e gestão de usuários com níveis de acesso.

## 🚀 Funcionalidades

- **Dashboard Interativo**: Visão geral da rede com KPIs (Total, Online, Offline).
- **Monitoramento em Tempo Real**: Verificação automática de status de conectividade (ping/request) dos dispositivos cadastrados.
- **Gestão de Dispositivos**: CRUD (Criar, Ler, Atualizar, Deletar) de roteadores.
- **Controle de Acesso**:
  - **Administrador**: Gerenciamento total (usuários e dispositivos).
  - **Visualizador**: Apenas visualização do dashboard.
- **Autenticação**: Sistema de Login e Registro seguro.
- **Interface Responsiva**: Design moderno com suporte a **Modo Escuro (Dark Mode)**.
- **Gerenciamento de Usuários**: Painel administrativo para controle de contas.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3, Flask
- **Banco de Dados**: SQLite (SQLAlchemy)
- **Frontend**: HTML5, CSS3, JavaScript
- **Autenticação**: Flask-Login, Werkzeug Security
- **Outros**: Flask-CORS, python-dotenv

## 📂 Estrutura do Projeto

```text
router-manager/
├── app.py                 # Aplicação principal e rotas
├── requirements.txt       # Dependências do projeto
├── .env                   # Variáveis de ambiente
├── instance/
│   └── database.db        # Banco de dados SQLite
├── static/
│   ├── css/               # Estilos (style.css, style-dashboard.css)
│   └── assets/            # Imagens e ícones
└── templates/             # Templates HTML (Jinja2)
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── admin_dashboard.html
    └── settings.html
