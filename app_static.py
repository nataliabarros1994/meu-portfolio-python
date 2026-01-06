"""
Aplicação Flask para geração de site estático
Versão otimizada para Frozen-Flask e GitHub Pages

Autor: Natália Barros
"""

import os
import json
from flask import Flask, render_template
from datetime import datetime

# ============================================
# APP
# ============================================

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
            return json.load(f)
    except Exception as e:
        print(f"Erro ao carregar projetos: {e}")
        return {'projects': [], 'stats': {}}

# ============================================
# CONTEXT PROCESSORS
# ============================================

@app.context_processor
def inject_portfolio_info():
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
    data = load_projects_data()
    return {
        'total_projetos': data.get('stats', {}).get('total_projects', 0)
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

    # IDs vindos do JSON (mais estrelas / definidos manualmente)
    featured_ids = stats.get('featured_projects', [])

    # IDs que DEVEM aparecer em destaque (forçados)
    required_featured_ids = [
        1119999999  # NPX-PDF-BRASIL (ID REAL)
    ]

    # Combinar e remover duplicados
    all_featured_ids = list(dict.fromkeys(featured_ids + required_featured_ids))

    # Mapear projetos por ID
    projects_by_id = {p['id']: p for p in projects}

    featured_projects = [
        projects_by_id[pid]
        for pid in all_featured_ids
        if pid in projects_by_id
    ]

    # Completar até 6 projetos
    if len(featured_projects) < 6:
        remaining = [
            p for p in projects
            if p['id'] not in [fp['id'] for fp in featured_projects]
        ]
        featured_projects.extend(remaining[:6 - len(featured_projects)])

    # Fallback absoluto
    if not featured_projects:
        featured_projects = projects[:6]

    return render_template(
        'index_static.html',
        projetos=featured_projects,
        stats=stats
    )

@app.route('/projetos/')
@app.route('/projetos/index.html')
def projetos():
    data = load_projects_data()
    projects = data.get('projects', [])
    stats = data.get('stats', {})

    linguagens = sorted(
        {lang for p in projects for lang in p.get('languages', [])}
    )

    tecnologias = sorted(
        {tech for p in projects for tech in p.get('technologies', [])}
    )

    return render_template(
        'projetos_static.html',
        projetos=projects,
        stats=stats,
        linguagens=linguagens,
        tecnologias=tecnologias
    )

@app.route('/sobre/')
@app.route('/sobre/index.html')
def sobre():
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

    return render_template(
        'sobre.html',
        habilidades=habilidades,
        experiencias=experiencias,
        educacao=educacao
    )

@app.route('/contato/')
@app.route('/contato/index.html')
def contato():
    return render_template('contato.html')

# ============================================
# ERROR HANDLER
# ============================================

@app.errorhandler(404)
def handle_404(e):
    return render_template('errors/404.html'), 404

# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
