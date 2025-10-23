"""
Aplicação Flask - Portfólio Profissional
Autor: Natália Barros
Descrição: Sistema completo de portfólio com gestão de projetos e integração Heroku
"""

import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename

# Configuração da aplicação Flask
app = Flask(__name__)

# Configurações de segurança
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configuração do Database
# Usa PostgreSQL em produção (Heroku) e SQLite em desenvolvimento
if os.environ.get('DATABASE_URL'):
    # Heroku fornece DATABASE_URL mas precisa de ajuste para SQLAlchemy
    database_url = os.environ.get('DATABASE_URL')
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Ambiente local - usa SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização de extensões
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# =============================================================================
# MODELOS DE DATABASE
# =============================================================================

class Projeto(db.Model):
    """Modelo para armazenar projetos do portfólio"""
    __tablename__ = 'projetos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    descricao_curta = db.Column(db.String(200))
    tecnologias = db.Column(db.String(200), nullable=False)
    github_url = db.Column(db.String(200))
    demo_url = db.Column(db.String(200))
    imagem = db.Column(db.String(200), default='projeto-default.jpg')
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    destaque = db.Column(db.Boolean, default=False)
    categoria = db.Column(db.String(50), default='Web')

    def __repr__(self):
        return f'<Projeto {self.titulo}>'

    def to_dict(self):
        """Converte objeto para dicionário (útil para API)"""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'descricao_curta': self.descricao_curta,
            'tecnologias': self.tecnologias.split(','),
            'github_url': self.github_url,
            'demo_url': self.demo_url,
            'imagem': self.imagem,
            'data_criacao': self.data_criacao.strftime('%Y-%m-%d'),
            'destaque': self.destaque,
            'categoria': self.categoria
        }


class Contato(db.Model):
    """Modelo para armazenar mensagens de contato"""
    __tablename__ = 'contatos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    assunto = db.Column(db.String(200), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow)
    lido = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Contato {self.nome} - {self.assunto}>'


# =============================================================================
# ROTAS PRINCIPAIS
# =============================================================================

@app.route('/')
def index():
    """Homepage - Mostra projetos em destaque"""
    projetos_destaque = Projeto.query.filter_by(destaque=True).order_by(
        Projeto.data_criacao.desc()
    ).limit(6).all()

    total_projetos = Projeto.query.count()

    return render_template('index.html',
                         projetos=projetos_destaque,
                         total_projetos=total_projetos)


@app.route('/projetos')
def projetos():
    """Página com todos os projetos - suporta filtros e busca"""
    # Filtros
    categoria = request.args.get('categoria')
    tecnologia = request.args.get('tecnologia')
    busca = request.args.get('busca')

    # Query base
    query = Projeto.query

    # Aplicar filtros
    if categoria and categoria != 'todas':
        query = query.filter_by(categoria=categoria)

    if tecnologia:
        query = query.filter(Projeto.tecnologias.contains(tecnologia))

    if busca:
        query = query.filter(
            db.or_(
                Projeto.titulo.contains(busca),
                Projeto.descricao.contains(busca),
                Projeto.tecnologias.contains(busca)
            )
        )

    # Ordenar por data
    projetos_lista = query.order_by(Projeto.data_criacao.desc()).all()

    # Obter categorias únicas
    categorias = db.session.query(Projeto.categoria).distinct().all()
    categorias = [c[0] for c in categorias]

    return render_template('projetos.html',
                         projetos=projetos_lista,
                         categorias=categorias,
                         categoria_atual=categoria,
                         busca=busca)


@app.route('/projeto/<int:id>')
def projeto_detalhe(id):
    """Página de detalhes de um projeto específico"""
    projeto = Projeto.query.get_or_404(id)

    # Projetos relacionados (mesma categoria, exceto o atual)
    projetos_relacionados = Projeto.query.filter(
        Projeto.categoria == projeto.categoria,
        Projeto.id != projeto.id
    ).order_by(db.func.random()).limit(3).all()

    return render_template('projeto-detalhe.html',
                         projeto=projeto,
                         projetos_relacionados=projetos_relacionados)


@app.route('/sobre')
def sobre():
    """Página Sobre Mim - biografia, habilidades, experiência"""
    habilidades = {
        'Backend': ['Python', 'Flask', 'Django', 'FastAPI', 'SQLAlchemy'],
        'Frontend': ['HTML5', 'CSS3', 'JavaScript', 'Bootstrap', 'jQuery'],
        'Database': ['PostgreSQL', 'SQLite', 'MySQL', 'MongoDB'],
        'DevOps': ['Git', 'GitHub', 'Heroku', 'Docker', 'Linux'],
        'Data Science': ['Pandas', 'NumPy', 'Matplotlib', 'Jupyter'],
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


@app.route('/contato', methods=['GET', 'POST'])
def contato():
    """Página de contato com formulário funcional"""
    if request.method == 'POST':
        # Capturar dados do formulário
        nome = request.form.get('nome')
        email = request.form.get('email')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')

        # Validação básica
        if not all([nome, email, assunto, mensagem]):
            flash('Por favor, preencha todos os campos!', 'error')
            return redirect(url_for('contato'))

        # Criar novo contato
        novo_contato = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        try:
            db.session.add(novo_contato)
            db.session.commit()
            flash('Mensagem enviada com sucesso! Entrarei em contato em breve.', 'success')
            return redirect(url_for('contato'))
        except Exception as e:
            db.session.rollback()
            flash('Erro ao enviar mensagem. Tente novamente.', 'error')
            app.logger.error(f'Erro ao salvar contato: {e}')

    return render_template('contato.html')


# =============================================================================
# ROTAS DE ADMINISTRAÇÃO
# =============================================================================

@app.route('/admin/add-project', methods=['GET', 'POST'])
def add_project():
    """Formulário para adicionar novos projetos"""
    if request.method == 'POST':
        # Capturar dados do formulário
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        descricao_curta = request.form.get('descricao_curta')
        tecnologias = request.form.get('tecnologias')
        github_url = request.form.get('github_url')
        demo_url = request.form.get('demo_url')
        categoria = request.form.get('categoria', 'Web')
        destaque = request.form.get('destaque') == 'on'

        # Criar novo projeto
        novo_projeto = Projeto(
            titulo=titulo,
            descricao=descricao,
            descricao_curta=descricao_curta,
            tecnologias=tecnologias,
            github_url=github_url,
            demo_url=demo_url,
            categoria=categoria,
            destaque=destaque
        )

        try:
            db.session.add(novo_projeto)
            db.session.commit()
            flash('Projeto adicionado com sucesso!', 'success')
            return redirect(url_for('projetos'))
        except Exception as e:
            db.session.rollback()
            flash('Erro ao adicionar projeto.', 'error')
            app.logger.error(f'Erro ao adicionar projeto: {e}')

    return render_template('admin/add-project.html')


# =============================================================================
# API ENDPOINTS (Opcional - para uso futuro)
# =============================================================================

@app.route('/api/projetos')
def api_projetos():
    """Retorna todos os projetos em formato JSON"""
    projetos_lista = Projeto.query.all()
    return jsonify([p.to_dict() for p in projetos_lista])


@app.route('/api/projeto/<int:id>')
def api_projeto(id):
    """Retorna um projeto específico em formato JSON"""
    projeto = Projeto.query.get_or_404(id)
    return jsonify(projeto.to_dict())


# =============================================================================
# FILTROS JINJA CUSTOMIZADOS
# =============================================================================

@app.template_filter('formato_data')
def formato_data(data):
    """Formata data para exibição"""
    if isinstance(data, str):
        data = datetime.strptime(data, '%Y-%m-%d')
    return data.strftime('%d/%m/%Y')


# =============================================================================
# TRATAMENTO DE ERROS
# =============================================================================

@app.errorhandler(404)
def page_not_found(e):
    """Página personalizada para erro 404"""
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """Página personalizada para erro 500"""
    db.session.rollback()
    return render_template('errors/500.html'), 500


# =============================================================================
# CONTEXT PROCESSORS
# =============================================================================

@app.context_processor
def inject_ano_atual():
    """Injeta ano atual em todos os templates"""
    return {'ano_atual': datetime.now().year}


@app.context_processor
def inject_info_portfolio():
    """Injeta informações do portfólio em todos os templates"""
    return {
        'nome_portfolio': 'Natália Barros',
        'titulo_portfolio': 'Desenvolvedora Python Full Stack',
        'github_link': 'https://github.com/nataliabarros1994',
        'linkedin_link': 'https://linkedin.com/in/nataliabarros',
        'email_contato': 'natalia@exemplo.com'
    }


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

if __name__ == '__main__':
    # Criar tabelas se não existirem
    with app.app_context():
        db.create_all()

    # Executar aplicação
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
