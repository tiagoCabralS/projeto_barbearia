# 💈 Projeto Barbearia

Sistema web de **agendamento de horários para uma barbearia**, desenvolvido com **Django**. Resolve o problema clássico de marcação de cortes por WhatsApp/telefone: mensagens perdidas, horários batendo entre clientes e falta de organização da agenda.

## ✨ Funcionalidades

- **Cadastro e autenticação de usuários** — registro, login e logout, com criação automática de um perfil (incluindo telefone) para cada cliente.
- **Agendamento por serviço** — o cliente escolhe a categoria do serviço (cada uma com sua duração padrão), a data e o horário desejado.
- **Validação automática contra conflitos de horário** — antes de confirmar o agendamento, o sistema verifica se a data já passou e se o horário escolhido se sobrepõe a algum agendamento existente, calculando o horário de término com base na duração do serviço.
- **Gerenciamento de agendamentos (CRUD)** — visualização de detalhes, atualização e cancelamento (com confirmação) dos próprios agendamentos.
- **Painel pessoal (Home)** — lista separada de agendamentos futuros e passados do cliente logado.

## 🛠️ Tecnologias utilizadas

- **Python** + **Django** (arquitetura MVT)
- **MySQL** como banco de dados, rodando localmente via **WAMP Server**
- **Django ORM** — modelagem de dados (`Category`, `Perfil`, `Agendamento`) e relacionamentos (`ForeignKey`, `OneToOneField`)
- **Django Forms** com validações customizadas (`clean()`) para regras de negócio, como a sobreposição de horários
- **Sistema de autenticação nativo do Django** (login, logout, registro, `@login_required`)
- **Django Messages Framework** para feedback ao usuário (sucesso/erro)
- **Templates Django** com herança de templates (`base_templates`)
- **HTML, CSS e JavaScript** no front-end

## 📁 Estrutura do projeto

```
projeto_barbearia/
├── barbearia/              # App principal
│   ├── models.py           # Category, Perfil, Agendamento
│   ├── forms.py            # AgendamentoForm, UserRegistrationForm
│   ├── views.py            # Regras de agendamento, autenticação
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/barbearia/
├── base_templates/global/  # Templates base (header, rodapé, layout)
├── base_static/global/     # CSS, JS e imagens
├── project/                # Configurações do projeto Django
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## 🚀 Como rodar o projeto localmente

### Pré-requisitos

- Python 3.10+
- MySQL (recomendado via [WAMP Server](https://www.wampserver.com/) no Windows, mas pode ser qualquer instância MySQL local)
- pip

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/tiagoCabralS/projeto_barbearia.git
   cd projeto_barbearia
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux/Mac
   ```

3. **Instale as dependências**
   ```bash
   pip install django mysqlclient
   ```

4. **Configure o banco de dados**

   Com o WAMP Server (ou outro serviço MySQL) rodando, crie o banco de dados:
   ```sql
   CREATE DATABASE barbearia;
   ```

   As credenciais de conexão em `project/settings.py` já estão configuradas para um ambiente local padrão (`root`, sem senha, `localhost:3306`). Ajuste conforme sua instalação, se necessário.

5. **Aplique as migrações**
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional, para acessar o admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Rode o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

8. Acesse `http://127.0.0.1:8000/` no navegador.

## 🔮 Possíveis melhorias futuras

- Integração de login com Google (ou outros provedores de autenticação social)
- Notificações automáticas por e-mail/WhatsApp lembrando o cliente do agendamento
- Painel administrativo específico para o barbeiro gerenciar a agenda
- Deploy em ambiente de produção

Sugestões são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou *pull request*.

## 📄 Licença

Este projeto está disponível livremente para fins de estudo e aprendizado.
