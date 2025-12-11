"""
Script para inicializar o banco de dados e popular com dados de exemplo
Autor: Natália Barros
Uso: python init_db.py
"""

from app import app, db, Projeto
from datetime import datetime, timedelta
import random

def criar_tabelas():
    """Cria todas as tabelas do banco de dados"""
    with app.app_context():
        print("🔄 Criando tabelas do banco de dados...")
        db.create_all()
        print("✅ Tabelas criadas com sucesso!")

def limpar_dados():
    """Remove todos os dados existentes (cuidado!)"""
    with app.app_context():
        print("🗑️  Limpando dados existentes...")
        Projeto.query.delete()
        db.session.commit()
        print("✅ Dados limpos!")

def criar_projetos_exemplo():
    """Cria projetos de exemplo para o portfólio"""
    with app.app_context():
        print("📝 Criando projetos de exemplo...")

        projetos_exemplo = [
            {
                'titulo': 'Sistema de Gestão de Tarefas',
                'descricao': '''
                    <p>Sistema completo de gestão de tarefas desenvolvido com Flask e SQLAlchemy.
                    Permite criar, editar, deletar e organizar tarefas por prioridade e categoria.</p>

                    <h5>Funcionalidades Principais:</h5>
                    <ul>
                        <li>Autenticação de usuários com Flask-Login</li>
                        <li>CRUD completo de tarefas</li>
                        <li>Sistema de prioridades e categorias</li>
                        <li>Dashboard com estatísticas</li>
                        <li>API RESTful para integração</li>
                        <li>Interface responsiva com Bootstrap</li>
                    </ul>

                    <h5>Desafios e Soluções:</h5>
                    <p>Implementei cache com Redis para melhorar performance,
                    e utilizei Celery para processamento de tarefas assíncronas.</p>
                ''',
                'descricao_curta': 'Sistema completo de gestão de tarefas com Flask, SQLAlchemy e autenticação de usuários',
                'tecnologias': 'Python, Flask, SQLAlchemy, PostgreSQL, Bootstrap, Redis, Celery',
                'github_url': 'https://github.com/usuario/sistema-tarefas',
                'demo_url': 'https://tarefas-demo.herokuapp.com',
                'categoria': 'Web App',
                'destaque': True
            },
            {
                'titulo': 'API de E-commerce RESTful',
                'descricao': '''
                    <p>API completa para e-commerce desenvolvida com Flask-RESTful.
                    Inclui sistema de autenticação, gerenciamento de produtos, carrinho de compras e processamento de pedidos.</p>

                    <h5>Recursos:</h5>
                    <ul>
                        <li>Autenticação JWT</li>
                        <li>CRUD de produtos e categorias</li>
                        <li>Carrinho de compras persistente</li>
                        <li>Sistema de pedidos</li>
                        <li>Integração com gateway de pagamento</li>
                        <li>Documentação Swagger</li>
                    </ul>

                    <p>A API segue boas práticas REST e possui testes unitários e de integração completos.</p>
                ''',
                'descricao_curta': 'API RESTful completa para e-commerce com autenticação JWT e processamento de pedidos',
                'tecnologias': 'Python, Flask-RESTful, JWT, PostgreSQL, Swagger, Pytest',
                'github_url': 'https://github.com/usuario/ecommerce-api',
                'demo_url': 'https://ecommerce-api-demo.herokuapp.com/docs',
                'categoria': 'API',
                'destaque': True
            },
            {
                'titulo': 'Dashboard Analytics',
                'descricao': '''
                    <p>Dashboard interativo para visualização de dados de analytics
                    desenvolvido com Flask e bibliotecas de visualização.</p>

                    <h5>Tecnologias Utilizadas:</h5>
                    <ul>
                        <li>Flask para backend</li>
                        <li>Plotly para gráficos interativos</li>
                        <li>Pandas para processamento de dados</li>
                        <li>Chart.js para visualizações</li>
                        <li>WebSockets para atualizações em tempo real</li>
                    </ul>

                    <p>O dashboard processa grandes volumes de dados e apresenta
                    insights de forma clara e interativa.</p>
                ''',
                'descricao_curta': 'Dashboard interativo para analytics com visualizações em tempo real',
                'tecnologias': 'Python, Flask, Plotly, Pandas, Chart.js, WebSockets',
                'github_url': 'https://github.com/usuario/analytics-dashboard',
                'demo_url': 'https://analytics-dashboard-demo.herokuapp.com',
                'categoria': 'Data Science',
                'destaque': True
            },
            {
                'titulo': 'Bot de Automação Web',
                'descricao': '''
                    <p>Bot inteligente para automação de tarefas web desenvolvido com Python.
                    Utiliza Selenium e BeautifulSoup para scraping e automação.</p>

                    <h5>Funcionalidades:</h5>
                    <ul>
                        <li>Web scraping de múltiplos sites</li>
                        <li>Automação de formulários</li>
                        <li>Agendamento de tarefas</li>
                        <li>Notificações por email</li>
                        <li>Logs detalhados</li>
                    </ul>

                    <p>O bot economiza horas de trabalho manual e pode ser facilmente
                    configurado para diferentes necessidades.</p>
                ''',
                'descricao_curta': 'Bot inteligente para automação de tarefas web com Selenium e BeautifulSoup',
                'tecnologias': 'Python, Selenium, BeautifulSoup, Pandas, APScheduler',
                'github_url': 'https://github.com/usuario/web-automation-bot',
                'categoria': 'Automação',
                'destaque': False
            },
            {
                'titulo': 'Sistema de Blog com CMS',
                'descricao': '''
                    <p>Sistema de blog completo com CMS administrativo desenvolvido com Flask.
                    Permite criação, edição e publicação de posts com editor WYSIWYG.</p>

                    <h5>Recursos:</h5>
                    <ul>
                        <li>Editor de texto rico (CKEditor)</li>
                        <li>Sistema de categorias e tags</li>
                        <li>Comentários com moderação</li>
                        <li>Upload de imagens</li>
                        <li>SEO otimizado</li>
                        <li>RSS Feed</li>
                    </ul>
                ''',
                'descricao_curta': 'Sistema de blog profissional com CMS administrativo e editor WYSIWYG',
                'tecnologias': 'Python, Flask, SQLAlchemy, CKEditor, Bootstrap, PostgreSQL',
                'github_url': 'https://github.com/usuario/flask-blog-cms',
                'demo_url': 'https://blog-demo.herokuapp.com',
                'categoria': 'Web App',
                'destaque': False
            },
            {
                'titulo': 'Analisador de Sentimentos',
                'descricao': '''
                    <p>Aplicação de Machine Learning para análise de sentimentos em textos.
                    Utiliza técnicas de NLP e modelos treinados.</p>

                    <h5>Características:</h5>
                    <ul>
                        <li>Análise de sentimentos (positivo, negativo, neutro)</li>
                        <li>Interface web interativa</li>
                        <li>API para integração</li>
                        <li>Visualização de resultados</li>
                        <li>Suporte para múltiplos idiomas</li>
                    </ul>
                ''',
                'descricao_curta': 'Aplicação de ML para análise de sentimentos com interface interativa',
                'tecnologias': 'Python, Flask, NLTK, Scikit-learn, Pandas, NumPy',
                'github_url': 'https://github.com/usuario/sentiment-analyzer',
                'demo_url': 'https://sentiment-analyzer-demo.herokuapp.com',
                'categoria': 'Machine Learning',
                'destaque': True
            },
            {
                'titulo': 'Encurtador de URLs',
                'descricao': '''
                    <p>Serviço de encurtamento de URLs similar ao bit.ly,
                    desenvolvido com Flask e Redis para alta performance.</p>

                    <h5>Funcionalidades:</h5>
                    <ul>
                        <li>Encurtamento de URLs com códigos personalizados</li>
                        <li>Estatísticas de cliques</li>
                        <li>QR Code automático</li>
                        <li>API REST</li>
                        <li>Cache com Redis</li>
                    </ul>
                ''',
                'descricao_curta': 'Serviço rápido de encurtamento de URLs com estatísticas e QR codes',
                'tecnologias': 'Python, Flask, Redis, PostgreSQL, QRCode',
                'github_url': 'https://github.com/usuario/url-shortener',
                'demo_url': 'https://shorturl-demo.herokuapp.com',
                'categoria': 'Web App',
                'destaque': False
            },
            {
                'titulo': 'Chat em Tempo Real',
                'descricao': '''
                    <p>Aplicação de chat em tempo real utilizando WebSockets.
                    Suporta múltiplas salas e mensagens privadas.</p>

                    <h5>Recursos:</h5>
                    <ul>
                        <li>Mensagens em tempo real com Socket.IO</li>
                        <li>Salas de chat públicas e privadas</li>
                        <li>Indicador de digitação</li>
                        <li>Histórico de mensagens</li>
                        <li>Emojis e formatação</li>
                    </ul>
                ''',
                'descricao_curta': 'Chat em tempo real com WebSockets, salas e mensagens privadas',
                'tecnologias': 'Python, Flask, Socket.IO, JavaScript, Bootstrap',
                'github_url': 'https://github.com/usuario/realtime-chat',
                'demo_url': 'https://chat-demo.herokuapp.com',
                'categoria': 'Web App',
                'destaque': False
            },
            {
                'titulo': 'EstiMate MVP',
                'descricao': '''
                    <p>Aplicação de visão computacional que estima materiais de construção a partir de fotos,
                    usando objetos de referência para detecção de escala.</p>

                    <h5>Como Funciona:</h5>
                    <ol>
                        <li><strong>Upload:</strong> Tire ou faça upload de uma foto contendo um objeto de referência (cartão de crédito ou porta padrão)</li>
                        <li><strong>Detecção de Escala:</strong> O backend usa visão computacional para detectar a referência e calcular a escala</li>
                        <li><strong>Marcar Área:</strong> Desenhe um retângulo sobre a superfície que deseja medir</li>
                        <li><strong>Obter Estimativa:</strong> O app calcula dimensões reais e estima materiais necessários</li>
                    </ol>

                    <h5>Funcionalidades:</h5>
                    <ul>
                        <li>Detecção automática de escala com OpenCV</li>
                        <li>Seleção interativa de área por desenho de retângulos</li>
                        <li>Cálculo de dimensões em tempo real (pixels para metros)</li>
                        <li>Estimativa de materiais (litros de tinta, quantidade de azulejos)</li>
                        <li>Design responsivo mobile-first</li>
                        <li>Suporte completo a touch para dispositivos móveis</li>
                    </ul>

                    <h5>Objetos de Referência Suportados:</h5>
                    <ul>
                        <li><strong>Cartão de Crédito (ISO/IEC 7810 ID-1):</strong> 85.6mm x 53.98mm</li>
                        <li><strong>Porta Padrão:</strong> 80cm x 200cm</li>
                    </ul>

                    <h5>Arquitetura:</h5>
                    <p>Backend desenvolvido com FastAPI e OpenCV para processamento de imagens.
                    Frontend React com Vite para uma experiência de usuário fluida e responsiva.</p>
                ''',
                'descricao_curta': 'App de visão computacional que estima materiais de construção a partir de fotos usando detecção de escala',
                'tecnologias': 'Python, FastAPI, OpenCV, NumPy, React, Vite, CSS3',
                'github_url': 'https://github.com/nataliabarros1994/Guiado-MVP',
                'categoria': 'Machine Learning',
                'destaque': True
            }
        ]

        # Criar projetos com datas diferentes
        for i, projeto_data in enumerate(projetos_exemplo):
            # Datas variadas nos últimos 6 meses
            dias_atras = random.randint(0, 180)
            data_criacao = datetime.utcnow() - timedelta(days=dias_atras)

            projeto = Projeto(
                titulo=projeto_data['titulo'],
                descricao=projeto_data['descricao'],
                descricao_curta=projeto_data['descricao_curta'],
                tecnologias=projeto_data['tecnologias'],
                github_url=projeto_data['github_url'],
                demo_url=projeto_data.get('demo_url'),
                categoria=projeto_data['categoria'],
                destaque=projeto_data['destaque'],
                data_criacao=data_criacao
            )

            db.session.add(projeto)
            print(f"  ✓ Criado: {projeto.titulo}")

        db.session.commit()
        print(f"\n✅ {len(projetos_exemplo)} projetos criados com sucesso!")

def main():
    """Função principal"""
    print("\n" + "="*60)
    print("🚀 INICIALIZADOR DO BANCO DE DADOS - PORTFÓLIO")
    print("="*60 + "\n")

    try:
        # Criar tabelas
        criar_tabelas()

        # Perguntar se deseja popular com dados de exemplo
        resposta = input("\n❓ Deseja criar projetos de exemplo? (s/n): ").lower()

        if resposta == 's':
            # Limpar dados existentes
            limpar = input("⚠️  Limpar dados existentes antes? (s/n): ").lower()
            if limpar == 's':
                limpar_dados()

            # Criar projetos de exemplo
            criar_projetos_exemplo()

        print("\n" + "="*60)
        print("✨ Inicialização concluída com sucesso!")
        print("="*60)
        print("\n💡 Próximos passos:")
        print("  1. Execute: python app.py")
        print("  2. Acesse: http://localhost:5000")
        print("  3. Adicione seus próprios projetos!")
        print("\n")

    except Exception as e:
        print(f"\n❌ Erro ao inicializar banco de dados: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
