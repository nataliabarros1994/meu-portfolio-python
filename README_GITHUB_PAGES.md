# 🚀 Portfólio Automático com GitHub API + GitHub Pages

Portfólio profissional que sincroniza automaticamente com seus repositórios do GitHub e faz deploy automático via GitHub Actions.

## ✨ Características

### 🤖 Automação Total
- ✅ Busca automática de todos os repositórios públicos
- ✅ Atualização diária via GitHub Actions
- ✅ Deploy automático no GitHub Pages
- ✅ Sistema de cache inteligente
- ✅ Filtros e ordenação dinâmica

### 🎨 Design Profissional
- ✅ Responsivo (Bootstrap 5)
- ✅ Animações suaves (AOS)
- ✅ Badges de tecnologias
- ✅ Estatísticas em tempo real
- ✅ Indicadores de projetos recentes

### 📊 Integração GitHub API
- ✅ Busca paginada de repositórios
- ✅ Detecção automática de linguagens
- ✅ Mapeamento de tecnologias
- ✅ Stats (stars, forks, watchers)
- ✅ Topics e descrições
- ✅ URLs de demonstração

## 🔧 Configuração Inicial

### 1. Clone e Configure

```bash
# Clone o repositório
git clone https://github.com/nataliabarros1994/portfolio-python.git
cd portfolio-python

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale dependências
pip install -r requirements_github.txt
```

### 2. Configure seu GitHub Username

Edite `build_portfolio.py` linha 28:

```python
GITHUB_USERNAME = "nataliabarros1994"  # SEU USERNAME AQUI
```

### 3. Personalize suas Informações

Edite `app_static.py` (função `inject_portfolio_info`):

```python
return {
    'nome_portfolio': 'Seu Nome',
    'titulo_portfolio': 'Seu Título',
    'github_username': 'seu-usuario',
    'github_link': 'https://github.com/seu-usuario',
    'linkedin_link': 'https://linkedin.com/in/seu-perfil',
    'email_contato': 'seu@email.com',
}
```

## 🚀 Build e Deploy

### Build Local (Primeira Vez)

```bash
# 1. Buscar projetos do GitHub
python build_portfolio.py

# 2. Gerar site estático
python freeze.py

# 3. Testar localmente
python -m http.server --directory docs 8000
# Acesse: http://localhost:8000
```

### Deploy no GitHub Pages

```bash
# 1. Criar repositório no GitHub
git init
git add .
git commit -m "🎉 Initial commit: Portfolio automático"

# 2. Adicionar remote
git remote add origin https://github.com/nataliabarros1994/portfolio-python.git

# 3. Push
git push -u origin main

# 4. Configurar GitHub Pages
# Vá em Settings > Pages
# Source: Deploy from a branch
# Branch: gh-pages / (root)
# Salvar
```

### ⚠️ Importante: Configurar GitHub Actions

Para que a automação funcione, você precisa:

1. **Habilitar GitHub Actions** no repositório
2. **Configurar permissões de workflow**:
   - Settings > Actions > General
   - Workflow permissions: **Read and write permissions**
   - Marcar: **Allow GitHub Actions to create and approve pull requests**
   - Salvar

3. **Aguardar primeiro deploy**:
   - GitHub Actions rodará automaticamente
   - Primeiro build pode levar 2-3 minutos
   - Ver progresso em Actions tab

## 🤖 Automação Configurada

### Deploy Automático
- **Trigger**: Push para `main`
- **Ação**: Rebuild + deploy
- **Workflow**: `.github/workflows/deploy.yml`

### Atualização Diária
- **Trigger**: Diariamente à meia-noite (UTC)
- **Ação**: Busca novos projetos + rebuild + deploy
- **Workflow**: `.github/workflows/update-projects.yml`
- **Manual**: Actions tab > "Update Projects Daily" > Run workflow

## 📁 Estrutura de Arquivos

```
portfolio-python/
├── build_portfolio.py       # ⭐ Busca projetos do GitHub
├── freeze.py                 # ⭐ Gera site estático
├── app_static.py             # Flask app otimizada
├── requirements_github.txt   # Dependências
│
├── .github/workflows/        # ⭐ Automação
│   ├── deploy.yml           # Deploy no push
│   └── update-projects.yml  # Update diário
│
├── templates/                # Templates HTML
│   ├── base.html
│   ├── index_static.html    # Homepage
│   ├── projetos_static.html # ⭐ Galeria de projetos
│   ├── sobre_static.html
│   └── contato_static.html
│
├── docs/                     # ⭐ Site estático (gerado)
│   ├── index.html
│   ├── projetos/
│   ├── sobre/
│   ├── contato/
│   └── static/
│       └── data/
│           └── projects.json # Dados dos projetos
│
├── projects_data.json        # ⭐ Cache local
└── static/
    ├── css/style.css
    ├── js/script.js
    └── data/projects.json
```

## 🔄 Fluxo de Atualização

```
┌──────────────────┐
│ GitHub Repos     │
│ (Seus projetos)  │
└────────┬─────────┘
         │
         ↓ API Request
┌────────────────────┐
│ build_portfolio.py │
│ - Busca repos      │
│ - Filtra e processa│
│ - Gera JSON        │
└────────┬───────────┘
         │
         ↓ JSON Cache
┌────────────────────┐
│ freeze.py          │
│ - Renderiza HTML   │
│ - Gera /docs       │
└────────┬───────────┘
         │
         ↓ Static Site
┌────────────────────┐
│ GitHub Pages       │
│ (Site publicado)   │
└────────────────────┘
```

## 📊 Scripts Principais

### build_portfolio.py

**Função**: Busca projetos do GitHub via API

```bash
# Build normal (usa cache se válido)
python build_portfolio.py

# Force refresh (ignora cache)
python build_portfolio.py --force
# ou
python build_portfolio.py -f
```

**O que faz**:
1. Busca todos os repositórios públicos do usuário
2. Filtra forks, arquivados e vazios
3. Detecta linguagens e tecnologias
4. Calcula estatísticas
5. Salva cache (`projects_data.json`)
6. Gera JSON para frontend (`static/data/projects.json`)

### freeze.py

**Função**: Gera site estático para GitHub Pages

```bash
python freeze.py
```

**O que faz**:
1. Limpa diretório `docs/`
2. Renderiza todos os templates em HTML estático
3. Copia arquivos estáticos
4. Cria `.nojekyll`
5. Gera páginas de erro

## 🎨 Personalização Avançada

### Adicionar Seção "Sobre Mim"

Edite `app_static.py` função `sobre()`:

```python
habilidades = {
    'Backend': ['Python', 'Flask', 'Django'],
    'Frontend': ['HTML5', 'CSS3', 'JavaScript'],
    # Adicione mais...
}

experiencias = [
    {
        'cargo': 'Seu Cargo',
        'empresa': 'Sua Empresa',
        'periodo': '2023 - Presente',
        'descricao': 'Descrição do cargo'
    }
]
```

### Customizar Cores

Edite `static/css/style.css`:

```css
:root {
    --primary-color: #007bff;  /* Sua cor primária */
    --primary-dark: #0056b3;
    /* ... */
}
```

### Mapeamento de Tecnologias

Edite `build_portfolio.py` linha 35:

```python
TECH_MAPPING = {
    'Python': ['Python', 'Flask', 'Django', 'FastAPI'],
    # Adicione mais mapeamentos...
}
```

## 🐛 Solução de Problemas

### Build Falha

```bash
# Verificar erros
python build_portfolio.py --force

# Verificar API rate limit
# GitHub API: 60 requests/hora (não autenticado)
# Solução: Aguardar ou usar token
```

### Site Não Atualiza

```bash
# Rebuild completo
python build_portfolio.py --force
python freeze.py

# Commit e push
git add docs/
git commit -m "Rebuild site"
git push
```

### GitHub Actions Falha

1. Verificar logs: **Actions tab** > workflow com erro
2. Verificar permissões: Settings > Actions > General
3. Verificar secrets (se usar token)

### Cache Desatualizado

```bash
# Deletar cache e rebuild
rm projects_data.json
python build_portfolio.py
```

## 🔒 Usando GitHub Token (Opcional)

Para evitar rate limit (60 req/hora → 5000 req/hora):

### 1. Criar Token

1. GitHub > Settings > Developer settings
2. Personal access tokens > Tokens (classic)
3. Generate new token
4. Scopes: `public_repo`
5. Copiar token

### 2. Configurar Localmente

```bash
# Criar .env
echo "GITHUB_TOKEN=seu_token_aqui" > .env
```

### 3. Atualizar build_portfolio.py

```python
import os
from dotenv import load_dotenv

load_dotenv()

headers = {}
if os.getenv('GITHUB_TOKEN'):
    headers['Authorization'] = f"token {os.getenv('GITHUB_TOKEN')}"

response = requests.get(url, headers=headers, params=params)
```

## 📈 Monitoramento

### Ver Estatísticas

Acesse: `https://nataliabarros1994.github.io/portfolio-python`

- Total de projetos
- Total de stars
- Total de forks
- Projetos recentes

### Ver Builds

GitHub Actions tab:
- Deploy history
- Update history
- Build logs

## 🎯 Próximos Passos

Depois do deploy:

1. ✅ Compartilhe o link do portfólio
2. ✅ Adicione ao perfil do GitHub
3. ✅ Adicione ao LinkedIn
4. ✅ Continue criando projetos!
5. ✅ Automação cuida do resto

## 📝 Comandos Rápidos

```bash
# Build completo
python build_portfolio.py && python freeze.py

# Testar localmente
python -m http.server --directory docs 8000

# Deploy
git add . && git commit -m "Update" && git push

# Trigger update manual
# Actions > Update Projects Daily > Run workflow
```

## 🌐 URLs

- **Portfólio**: https://nataliabarros1994.github.io/portfolio-python
- **Repositório**: https://github.com/nataliabarros1994/portfolio-python
- **API GitHub**: https://api.github.com/users/nataliabarros1994/repos

## 📄 Licença

MIT License - Use livremente!

---

**Desenvolvido com** ❤️ **e Python**

⭐ Se este projeto te ajudou, considere dar uma estrela no GitHub!
