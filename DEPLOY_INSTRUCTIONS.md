# 🚀 INSTRUÇÕES DE DEPLOY - GitHub Pages

## ✅ Status Atual

- ✅ Git inicializado
- ✅ Commit criado (30 arquivos)
- ✅ Branch `main` configurada
- ✅ Site estático gerado em `docs/`
- ✅ 6 projetos do GitHub sincronizados

---

## 📋 PASSO A PASSO - Deploy Completo

### 1️⃣ CRIAR REPOSITÓRIO NO GITHUB (2 minutos)

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name**: `portfolio-python` ⚠️ IMPORTANTE: use exatamente este nome
   - **Description**: "Portfólio automático com integração GitHub API"
   - **Public** ✅ (deixar público)
   - **NÃO** marque "Add a README file"
   - **NÃO** marque ".gitignore"
   - **NÃO** escolha licença agora
3. Clique em **"Create repository"**

---

### 2️⃣ CONECTAR E FAZER PUSH (1 minuto)

Copie e cole estes comandos **UM POR VEZ** no terminal:

```bash
# Navegar para o projeto
cd "/home/nataliabarros1994/Documents/meu portifolio"

# Adicionar remote do GitHub
git remote add origin https://github.com/nataliabarros1994/portfolio-python.git

# Fazer push
git push -u origin main
```

**Se pedir usuário e senha:**
- Usuário: `nataliabarros1994`
- Senha: Use um **Personal Access Token** (veja seção abaixo se necessário)

---

### 3️⃣ CONFIGURAR GITHUB PAGES (1 minuto)

1. No repositório, vá em: **Settings** (aba superior)
2. No menu lateral esquerdo: **Pages**
3. Em **"Source"**:
   - Selecione: **Deploy from a branch**
4. Em **"Branch"**:
   - Branch: **`gh-pages`**
   - Folder: **`/ (root)`**
5. Clique em **Save**

⚠️ **IMPORTANTE**: Escolha `gh-pages`, NÃO `main`!

---

### 4️⃣ HABILITAR GITHUB ACTIONS (1 minuto)

Para automação funcionar:

1. Vá em: **Settings** > **Actions** > **General**
2. Em **"Workflow permissions"**:
   - ✅ Selecione: **Read and write permissions**
   - ✅ Marque: **Allow GitHub Actions to create and approve pull requests**
3. Clique em **Save**

---

### 5️⃣ AGUARDAR BUILD (2-3 minutos)

1. Vá na aba **Actions** (topo do repositório)
2. Você verá: **"Deploy to GitHub Pages"** rodando
3. Aguarde aparecer ✅ (check verde)
4. Pode levar 2-3 minutos

---

### 6️⃣ ACESSAR SEU SITE! 🎉

Seu portfólio estará em:

```
https://nataliabarros1994.github.io/portfolio-python/
```

---

## 🔑 CRIAR PERSONAL ACCESS TOKEN (se necessário)

Se o GitHub pedir senha e não aceitar sua senha normal:

1. Vá em: https://github.com/settings/tokens
2. Clique em: **Generate new token** > **Classic**
3. Dê um nome: "Portfolio Deploy"
4. Selecione scopes:
   - ✅ `repo` (todos os sub-itens)
   - ✅ `workflow`
5. Clique em: **Generate token**
6. **COPIE O TOKEN** (só aparece uma vez!)
7. Use este token como senha no git push

---

## 🔄 COMO FUNCIONA A AUTOMAÇÃO

### Deploy Automático
Sempre que você fizer `git push`:
1. GitHub Actions roda automaticamente
2. Busca projetos novos do GitHub
3. Regenera o site
4. Faz deploy

### Atualização Diária
Todo dia à meia-noite (UTC):
1. GitHub Actions busca projetos automaticamente
2. Atualiza o site se houver mudanças

### Atualizar Manualmente
1. Vá em: **Actions** > **Update Projects Daily**
2. Clique em: **Run workflow**
3. Confirme: **Run workflow**

---

## ✏️ PERSONALIZAR INFORMAÇÕES

Edite o arquivo: `app_static.py` (linha 43)

```python
return {
    'nome_portfolio': 'Natália Barros',
    'titulo_portfolio': 'Desenvolvedora Python Full Stack',
    'github_username': 'nataliabarros1994',
    'github_link': 'https://github.com/nataliabarros1994',
    'linkedin_link': 'https://linkedin.com/in/SEU-PERFIL',  # ← EDITE AQUI
    'email_contato': 'seu@email.com',  # ← EDITE AQUI
}
```

Depois:
```bash
python build_portfolio.py
python freeze.py
git add .
git commit -m "Update: Personalizar informações"
git push
```

---

## 🐛 SOLUÇÃO DE PROBLEMAS

### Site não aparece (404)
- Aguarde 5 minutos após primeiro push
- Verifique se GitHub Actions rodou (aba Actions)
- Verifique se gh-pages branch foi criada (aba Branches)
- Verifique Settings > Pages se está configurado

### Push dá erro de autenticação
- Use Personal Access Token ao invés de senha
- Veja seção "Criar Personal Access Token" acima

### GitHub Actions falha
- Vá em Actions > workflow com erro
- Clique para ver logs
- Verifique se Workflow permissions está em "Read and write"

### Projetos não aparecem
- Execute localmente: `python build_portfolio.py`
- Verifique se `docs/static/data/projects.json` existe
- Commit e push novamente

---

## 📊 VERIFICAR STATUS

### Localmente (antes de fazer push):
```bash
cd "/home/nataliabarros1994/Documents/meu portifolio"
python -m http.server --directory docs 8000
# Acesse: http://localhost:8000
```

### No GitHub:
- **Code**: Ver arquivos
- **Actions**: Ver automação
- **Settings > Pages**: Ver configuração
- **Insights > Traffic**: Ver acessos

---

## 🎨 PRÓXIMOS PASSOS

Depois do deploy:

1. ✅ Compartilhe o link do portfólio
2. ✅ Adicione ao seu perfil do GitHub (bio)
3. ✅ Adicione ao LinkedIn
4. ✅ Continue criando projetos!
5. ✅ Automação cuida do resto

---

## 📞 LINKS IMPORTANTES

- **Seu Portfólio**: https://nataliabarros1994.github.io/portfolio-python/
- **Repositório**: https://github.com/nataliabarros1994/portfolio-python
- **GitHub API**: https://api.github.com/users/nataliabarros1994/repos
- **Documentação Completa**: README_GITHUB_PAGES.md

---

**PRONTO! SIGA OS PASSOS ACIMA E SEU PORTFÓLIO ESTARÁ NO AR! 🚀**
