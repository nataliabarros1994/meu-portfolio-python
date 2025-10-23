# 🚀 Portfólio Profissional Python/Flask

Portfólio profissional e moderno desenvolvido com Flask, Bootstrap 5 e PostgreSQL. Ideal para desenvolvedores Python que desejam mostrar seus projetos de forma elegante e profissional.

## ✨ Características

### Frontend
- 🎨 Design moderno e responsivo com Bootstrap 5
- 🌈 Animações suaves com AOS (Animate On Scroll)
- 📱 Mobile-first e totalmente responsivo
- ⚡ Performance otimizada
- 🎯 SEO-friendly

### Backend
- 🐍 Python 3.11+ e Flask
- 💾 SQLAlchemy ORM
- 🗄️ SQLite (dev) / PostgreSQL (prod)
- 🔒 Segurança com proteção CSRF e SQL Injection
- 📊 Sistema completo de gerenciamento de projetos

### Funcionalidades
- ✅ Sistema CRUD de projetos
- 🔍 Busca e filtros avançados
- 📝 Formulário de contato funcional
- 🌟 Projetos em destaque
- 🏷️ Sistema de categorias
- 📈 Estatísticas do portfólio
- 🤖 Importação automática de projetos do GitHub
- 🎨 Página de detalhes de cada projeto
- 📧 Sistema de mensagens de contato

## 📋 Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Conta no Heroku (para deploy)

## 🔧 Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/meu-portfolio-python.git
cd meu-portfolio-python
```

### 2. Crie um ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-super-segura-aqui
FLASK_ENV=development
DATABASE_URL=sqlite:///portfolio.db
```

### 5. Inicialize o banco de dados

```bash
python init_db.py
```

Responda as perguntas:
- Deseja criar projetos de exemplo? **s** (sim)
- Limpar dados existentes antes? **s** (sim, se for primeira vez)

### 6. Execute a aplicação

```bash
python app.py
```

Acesse: `http://localhost:5000`

## 🌐 Deploy no Heroku

### 1. Crie uma conta no Heroku

Acesse: https://heroku.com e crie uma conta gratuita

### 2. Instale o Heroku CLI

```bash
# Windows
# Baixe e instale: https://devcenter.heroku.com/articles/heroku-cli

# Mac
brew tap heroku/brew && brew install heroku

# Linux
curl https://cli-assets.heroku.com/install.sh | sh
```

### 3. Faça login no Heroku

```bash
heroku login
```

### 4. Crie um novo app

```bash
heroku create meu-portfolio-unico
```

**Nota:** O nome deve ser único globalmente. Se já existir, escolha outro nome.

### 5. Configure o banco de dados

```bash
# Adicionar PostgreSQL
heroku addons:create heroku-postgresql:essential-0

# Verificar
heroku config:get DATABASE_URL
```

### 6. Configure variáveis de ambiente

```bash
heroku config:set SECRET_KEY=sua-chave-secreta-aqui
heroku config:set DISABLE_COLLECTSTATIC=1
```

### 7. Faça o deploy

```bash
# Inicialize git (se ainda não tiver)
git init
git add .
git commit -m "Initial commit"

# Deploy
git push heroku main
```

Se estiver em outra branch:

```bash
git push heroku sua-branch:main
```

### 8. Inicialize o banco de dados no Heroku

```bash
heroku run python init_db.py
```

### 9. Abra seu portfólio

```bash
heroku open
```

## 📁 Estrutura do Projeto

```
meu-portfolio-python/
├── app.py                      # Aplicação Flask principal
├── init_db.py                  # Script de inicialização do DB
├── update_projects.py          # Importador de projetos do GitHub
├── requirements.txt            # Dependências Python
├── Procfile                    # Configuração Heroku
├── runtime.txt                 # Versão Python para Heroku
├── .gitignore                  # Arquivos ignorados pelo Git
├── README.md                   # Este arquivo
│
├── static/                     # Arquivos estáticos
│   ├── css/
│   │   └── style.css          # CSS customizado
│   ├── js/
│   │   └── script.js          # JavaScript
│   └── images/                 # Imagens
│
└── templates/                  # Templates HTML
    ├── base.html              # Template base
    ├── index.html             # Homepage
    ├── projetos.html          # Lista de projetos
    ├── projeto-detalhe.html   # Detalhes do projeto
    ├── sobre.html             # Página sobre
    ├── contato.html           # Página de contato
    ├── admin/
    │   └── add-project.html   # Formulário admin
    └── errors/
        ├── 404.html           # Página 404
        └── 500.html           # Página 500
```

## 🔌 Importação de Projetos do GitHub

Para importar automaticamente seus projetos do GitHub:

```bash
python update_projects.py seu-usuario-github
```

O script irá:
- Buscar seus repositórios públicos
- Detectar linguagens e tecnologias
- Criar projetos automaticamente
- Definir categorias baseado nas linguagens

Exemplo:

```bash
python update_projects.py nataliabarros1994
```

## 🎨 Personalização

### Informações Pessoais

Edite o arquivo `app.py` na seção `@app.context_processor`:

```python
@app.context_processor
def inject_info_portfolio():
    return {
        'nome_portfolio': 'Seu Nome',
        'titulo_portfolio': 'Seu Título',
        'github_link': 'https://github.com/seu-usuario',
        'linkedin_link': 'https://linkedin.com/in/seu-perfil',
        'email_contato': 'seu@email.com'
    }
```

### Cores e Estilo

Edite o arquivo `static/css/style.css` nas variáveis CSS:

```css
:root {
    --primary-color: #007bff;  /* Sua cor primária */
    --primary-dark: #0056b3;
    /* ... */
}
```

### Conteúdo da Página Sobre

Edite a rota `/sobre` no arquivo `app.py` para adicionar suas informações:

```python
@app.route('/sobre')
def sobre():
    habilidades = {
        'Backend': ['Python', 'Flask', 'Django'],
        # Adicione suas habilidades
    }

    experiencias = [
        {
            'cargo': 'Seu Cargo',
            'empresa': 'Sua Empresa',
            'periodo': '2023 - Presente',
            'descricao': 'Sua descrição'
        }
    ]
    # ...
```

## 📊 Adicionar Projetos Manualmente

### Via Interface Web

Acesse: `http://localhost:5000/admin/add-project`

Preencha o formulário com:
- Título do projeto
- Descrição completa (suporta HTML)
- Descrição curta (para cards)
- Tecnologias (separadas por vírgula)
- URL do GitHub
- URL de demonstração
- Categoria
- Marcar como destaque (opcional)

### Via Código Python

```python
from app import app, db, Projeto
from datetime import datetime

with app.app_context():
    projeto = Projeto(
        titulo='Meu Novo Projeto',
        descricao='Descrição detalhada do projeto...',
        descricao_curta='Resumo curto',
        tecnologias='Python, Flask, PostgreSQL',
        github_url='https://github.com/user/repo',
        demo_url='https://demo.herokuapp.com',
        categoria='Web App',
        destaque=True
    )

    db.session.add(projeto)
    db.session.commit()
```

## 🛠️ Comandos Úteis

### Desenvolvimento

```bash
# Executar em modo debug
python app.py

# Resetar banco de dados
python init_db.py

# Importar projetos do GitHub
python update_projects.py seu-usuario
```

### Heroku

```bash
# Ver logs
heroku logs --tail

# Abrir console Python no Heroku
heroku run python

# Reiniciar aplicação
heroku restart

# Verificar status
heroku ps

# Abrir no navegador
heroku open
```

### Git

```bash
# Atualizar deploy
git add .
git commit -m "Sua mensagem"
git push heroku main

# Ver branches remotas
git remote -v
```

## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError"

```bash
pip install -r requirements.txt
```

### Erro: "Database not found"

```bash
python init_db.py
```

### Erro no Heroku: "Application Error"

```bash
# Ver logs
heroku logs --tail

# Verificar variáveis
heroku config

# Reiniciar
heroku restart
```

### Erro: "Port already in use"

```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [número] /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

## 📝 TODO / Melhorias Futuras

- [ ] Sistema de autenticação admin
- [ ] Upload de imagens
- [ ] Blog integrado
- [ ] Dark mode toggle
- [ ] Google Analytics
- [ ] Sistema de tags
- [ ] API REST pública
- [ ] Testes automatizados
- [ ] CI/CD com GitHub Actions

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

**Natália Barros**

- GitHub: [@nataliabarros1994](https://github.com/nataliabarros1994)
- LinkedIn: [nataliabarros](https://linkedin.com/in/nataliabarros)
- Email: natalia@exemplo.com

## 🙏 Agradecimentos

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [AOS](https://michalsnik.github.io/aos/)
- [Heroku](https://heroku.com/)

---

⭐ Se este projeto te ajudou, considere dar uma estrela no GitHub!

Feito com ❤️ e Python
