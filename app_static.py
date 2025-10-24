"""
Aplicação Flask para geração de site estático
Versão otimizada para Frozen-Flask e GitHub Pages

Autor: Natália Barros
"""

import os
import json
from flask import Flask, render_template, url_for
from datetime import datetime

# Criar aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'static-site-key'

# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def load_projects_data():
    """
    Carrega dados dos projetos do arquivo JSON
    """
    json_path = 'static/data/projects.json'

    if not os.path.exists(json_path):
        return {'projects': [], 'stats': {}}

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Erro ao carregar projetos: {e}")
        return {'projects': [], 'stats': {}}


# ============================================
# CONTEXT PROCESSORS
# ============================================

@app.context_processor
def inject_portfolio_info():
    """
    Injeta informações do portfólio em todos os templates
    """
    return {
        'nome_portfolio': 'Natália Barros',
        'titulo_portfolio': 'Desenvolvedora Python Full Stack',
        'github_username': 'nataliabarros1994',
        'github_link': 'https://github.com/nataliabarros1994',
        'linkedin_link': 'https://www.linkedin.com/in/nataliachagas1994/',
        'email_contato': 'natalia.goldenglowitsolutions@gmail.com',
        'telefone_contato': '+55 22 98150-7669',
        'telefone_formatado': '+55 (22) 98150-7669',
        'ano_atual': datetime.now().year
    }


@app.context_processor
def inject_projects_count():
    """
    Injeta contagem de projetos
    """
    data = load_projects_data()
    return {
        'total_projetos': data['stats'].get('total_projects', 0)
    }


# ============================================
# ROTAS
# ============================================

@app.route('/')
def index():
    """Homepage com projetos em destaque"""
    data = load_projects_data()
    projects = data.get('projects', [])
    stats = data.get('stats', {})

    # Projetos em destaque (IDs dos projetos com mais stars)
    featured_ids = stats.get('featured_projects', [])
    featured_projects = [p for p in projects if p['id'] in featured_ids][:6]

    # Se não houver featured, pegar os 6 primeiros
    if not featured_projects:
        featured_projects = projects[:6]

    return render_template('index_static.html',
                         projetos=featured_projects,
                         stats=stats)


@app.route('/projetos/')
@app.route('/projetos/index.html')
def projetos():
    """Página com todos os projetos"""
    data = load_projects_data()
    projects = data.get('projects', [])
    stats = data.get('stats', {})

    # Extrair todas as linguagens únicas
    all_languages = set()
    for project in projects:
        all_languages.update(project.get('languages', []))

    # Extrair todas as tecnologias únicas
    all_technologies = set()
    for project in projects:
        all_technologies.update(project.get('technologies', []))

    return render_template('projetos_static.html',
                         projetos=projects,
                         stats=stats,
                         linguagens=sorted(list(all_languages)),
                         tecnologias=sorted(list(all_technologies)))


@app.route('/sobre/')
@app.route('/sobre/index.html')
def sobre():
    """Página sobre mim"""
    habilidades = {
        'Backend': ['Python', 'Flask', 'Django', 'FastAPI', 'SQLAlchemy'],
        'Frontend': ['HTML5', 'CSS3', 'JavaScript', 'Bootstrap', 'jQuery'],
        'Data Science': ['Pandas', 'NumPy', 'Matplotlib', 'Jupyter', 'Scikit-learn'],
        'Database': ['PostgreSQL', 'SQLite', 'MySQL', 'MongoDB'],
        'DevOps': ['Git', 'GitHub', 'Heroku', 'Docker', 'Linux'],
        'Outros': ['REST APIs', 'Jinja2', 'Testing', 'Agile']
    }

    experiencias = [
        {
            'cargo': 'Desenvolvedora Python',
            'empresa': 'Tech Company',
            'periodo': '2023 - Presente',
            'descricao': 'Desenvolvimento de aplicações web com Flask e Django'
        },
        {
            'cargo': 'Desenvolvedora Junior',
            'empresa': 'StartUp Tech',
            'periodo': '2022 - 2023',
            'descricao': 'Criação de APIs RESTful e automação de processos'
        }
    ]

    educacao = [
        {
            'curso': 'Análise e Desenvolvimento de Sistemas',
            'instituicao': 'Universidade Federal',
            'periodo': '2020 - 2023',
            'status': 'Concluído'
        }
    ]

    return render_template('sobre.html',
                         habilidades=habilidades,
                         experiencias=experiencias,
                         educacao=educacao)


@app.route('/contato/')
@app.route('/contato/index.html')
def contato():
    """Página de contato"""
    return render_template('contato.html')


# Página 404 será criada manualmente no freeze.py


# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def handle_404(e):
    """Handler para erro 404"""
    return render_template('errors/404.html'), 404


# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    # Para desenvolvimento local
    app.run(host='0.0.0.0', port=5000, debug=True)
