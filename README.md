# Router Manager 📡

Sistema web para gerenciamento e monitoramento de roteadores e dispositivos IoT. Desenvolvido para facilitar o controle de ativos de rede, permitindo a verificação de status em tempo real e gestão administrativa de usuários.

## 🚀 Funcionalidades

* **Dashboard Interativo:** Visão geral com KPIs de dispositivos totais, online e offline.
* **Monitoramento em Tempo Real:** Verificação automática de status (Online/Offline/Alerta) através de requisições HTTP aos dispositivos.
* **Gestão de Dispositivos:** Adicionar, editar e excluir roteadores com informações de local, modelo, serial e links de acesso.
* **Controle de Acesso:** Sistema de login seguro com níveis de permissão (Administrador e Visualizador).
* **Gestão de Usuários:** Painel administrativo para cadastro e controle de usuários do sistema.
* **Interface Responsiva:** Design adaptável para desktop e mobile, incluindo suporte a **Modo Escuro**.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Flask** (Framework Web)
* **SQLAlchemy** (ORM / Banco de Dados SQLite)
* **Flask-Login** (Autenticação)
* **HTML5 / CSS3 / JavaScript**
* **FontAwesome** (Ícones)

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter o **Python 3.x** e o **Git** instalados em sua máquina.

## 📦 Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/HenriqueLiuti5/router_manager.git](https://github.com/HenriqueLiuti5/router_manager.git)
    cd router_manager
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # Linux/Mac
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuração de Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz do projeto seguindo o modelo abaixo (ou renomeie o existente):

    ```env
    SECRET_KEY=sua_chave_secreta_aqui
    DATABASE_URL=sqlite:///database.db
    ```

5.  **Inicialize o Banco de Dados:**
    O sistema utiliza SQLite. Certifique-se de que a pasta `instance` existe ou será criada automaticamente pelo SQLAlchemy na primeira execução.

## ▶️ Como Executar

Para iniciar o servidor de desenvolvimento local:

```bash
python app.py
```

O sistema estará acessível em: http://127.0.0.1:5000

## 🔐 Acesso Padrão
Caso esteja utilizando o banco de dados pré-configurado, utilize as credenciais de administrador criadas ou registre uma nova conta na tela de login.

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📝 Licença
Este projeto está sob a licença MIT.
