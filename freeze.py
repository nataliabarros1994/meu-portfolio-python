"""
Freeze Script - Gera site estático para GitHub Pages
Converte aplicação Flask em HTML/CSS/JS estático

Autor: Natália Barros
"""

import os
import shutil
from flask_frozen import Freezer
from app_static import app

# Configurar Freezer
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
# Não definir FREEZER_BASE_URL para usar URLs relativas que funcionam localmente e no GitHub Pages

freezer = Freezer(app)


# Não gerar 404.html via generator - será criado manualmente


def clean_docs():
    """
    Limpa diretório docs antes de gerar novo build
    """
    if os.path.exists('docs'):
        print("🗑️  Limpando diretório docs...")
        shutil.rmtree('docs')
        print("✅ Diretório limpo")


def copy_static_files():
    """
    Copia arquivos estáticos adicionais
    """
    print("📁 Copiando arquivos estáticos...")

    # Criar diretório se não existir
    os.makedirs('docs/static/data', exist_ok=True)

    # Copiar projects.json se existir
    if os.path.exists('static/data/projects.json'):
        shutil.copy('static/data/projects.json', 'docs/static/data/projects.json')
        print("✅ projects.json copiado")

    # Copiar CNAME para GitHub Pages (se existir)
    if os.path.exists('CNAME'):
        shutil.copy('CNAME', 'docs/CNAME')
        print("✅ CNAME copiado")


def create_nojekyll():
    """
    Cria arquivo .nojekyll para desabilitar Jekyll no GitHub Pages
    """
    nojekyll_path = 'docs/.nojekyll'
    with open(nojekyll_path, 'w') as f:
        f.write('')
    print("✅ .nojekyll criado")


def create_404():
    """
    Cria página 404 para GitHub Pages
    """
    import os
    from flask import Flask
    from app_static import app as flask_app

    print("📄 Gerando página 404...")

    with flask_app.test_client() as client:
        response = client.get('/sobre/')  # Qualquer página válida
        # Criar 404.html manual
        with open('docs/404.html', 'w', encoding='utf-8') as f:
            f.write('''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Página Não Encontrada</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
</head>
<body>
    <div class="container min-vh-100 d-flex align-items-center justify-content-center">
        <div class="text-center">
            <h1 class="display-1 fw-bold text-primary">404</h1>
            <h2 class="mb-3">Página Não Encontrada</h2>
            <p class="lead text-muted mb-4">A página que você procura não existe.</p>
            <a href="/portfolio-python/" class="btn btn-primary">Voltar ao Início</a>
        </div>
    </div>
</body>
</html>''')
    print("✅ 404.html criado")


def build():
    """
    Função principal de build
    """
    print("\n" + "="*60)
    print("❄️  FREEZING FLASK APP → STATIC SITE")
    print("="*60 + "\n")

    try:
        # Limpar diretório docs
        clean_docs()

        # Gerar site estático
        print("🔨 Gerando site estático...")
        freezer.freeze()
        print("✅ Site estático gerado em docs/")

        # Copiar arquivos adicionais
        copy_static_files()

        # Criar .nojekyll
        create_nojekyll()

        # Estatísticas
        total_files = sum([len(files) for _, _, files in os.walk('docs')])
        total_size = sum([
            os.path.getsize(os.path.join(root, file))
            for root, _, files in os.walk('docs')
            for file in files
        ])

        print("\n" + "="*60)
        print("✨ BUILD ESTÁTICO CONCLUÍDO!")
        print("="*60)
        print(f"\n📊 Estatísticas:")
        print(f"  • Total de arquivos: {total_files}")
        print(f"  • Tamanho total: {total_size / 1024:.2f} KB")
        print(f"  • Diretório: docs/")
        print("\n" + "="*60 + "\n")

        print("💡 Próximos passos:")
        print("  1. Teste localmente: python -m http.server --directory docs 8000")
        print("  2. Acesse: http://localhost:8000")
        print("  3. Deploy: git add docs/ && git commit -m 'Update site' && git push")
        print("  4. Configure GitHub Pages para usar /docs")
        print("\n")

        return True

    except Exception as e:
        print(f"\n❌ Erro durante o build: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    import sys

    success = build()
    sys.exit(0 if success else 1)
