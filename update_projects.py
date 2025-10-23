"""
Script para importar projetos automaticamente do GitHub
Autor: Natália Barros
Uso: python update_projects.py [username]
"""

import requests
import sys
from app import app, db, Projeto
from datetime import datetime

# Mapeamento de linguagens para tecnologias/frameworks comuns
TECH_MAPPING = {
    'Python': ['Python', 'Flask', 'Django', 'FastAPI'],
    'JavaScript': ['JavaScript', 'Node.js', 'Express', 'React'],
    'TypeScript': ['TypeScript', 'Angular', 'Vue.js'],
    'Java': ['Java', 'Spring Boot', 'Maven'],
    'Go': ['Go', 'Gin', 'Echo'],
    'Ruby': ['Ruby', 'Ruby on Rails'],
    'PHP': ['PHP', 'Laravel', 'Symfony'],
    'C#': ['C#', '.NET', 'ASP.NET'],
    'HTML': ['HTML5', 'CSS3', 'Bootstrap'],
    'CSS': ['CSS3', 'Sass', 'Tailwind'],
}

# Mapeamento de linguagens para categorias
CATEGORY_MAPPING = {
    'Python': 'Web App',
    'JavaScript': 'Web App',
    'TypeScript': 'Web App',
    'Java': 'Backend',
    'Go': 'Backend',
    'Jupyter Notebook': 'Data Science',
    'R': 'Data Science',
    'HTML': 'Frontend',
    'CSS': 'Frontend',
}

def buscar_repositorios_github(username):
    """
    Busca todos os repositórios públicos de um usuário do GitHub

    Args:
        username (str): Nome de usuário do GitHub

    Returns:
        list: Lista de repositórios
    """
    url = f'https://api.github.com/users/{username}/repos'
    params = {
        'sort': 'updated',
        'per_page': 100
    }

    try:
        print(f"🔍 Buscando repositórios de {username}...")
        response = requests.get(url, params=params)
        response.raise_for_status()

        repos = response.json()
        print(f"✅ Encontrados {len(repos)} repositórios!")
        return repos

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao buscar repositórios: {e}")
        return []

def obter_linguagens_repo(languages_url):
    """
    Obtém as linguagens usadas em um repositório

    Args:
        languages_url (str): URL da API de linguagens

    Returns:
        list: Lista de linguagens
    """
    try:
        response = requests.get(languages_url)
        response.raise_for_status()
        languages = response.json()
        return list(languages.keys())
    except:
        return []

def determinar_tecnologias(languages):
    """
    Determina as tecnologias baseado nas linguagens

    Args:
        languages (list): Lista de linguagens

    Returns:
        str: String de tecnologias separadas por vírgula
    """
    tecnologias = set()

    for lang in languages:
        if lang in TECH_MAPPING:
            # Adiciona a linguagem principal
            tecnologias.add(lang)
            # Adiciona frameworks comuns (primeiro da lista)
            if len(TECH_MAPPING[lang]) > 1:
                tecnologias.add(TECH_MAPPING[lang][1])

    return ', '.join(sorted(tecnologias)) if tecnologias else 'Outras tecnologias'

def determinar_categoria(languages):
    """
    Determina a categoria baseado nas linguagens

    Args:
        languages (list): Lista de linguagens

    Returns:
        str: Categoria do projeto
    """
    for lang in languages:
        if lang in CATEGORY_MAPPING:
            return CATEGORY_MAPPING[lang]

    return 'Outros'

def criar_descricao(repo):
    """
    Cria uma descrição formatada do projeto

    Args:
        repo (dict): Dados do repositório

    Returns:
        str: Descrição HTML formatada
    """
    descricao_base = repo.get('description', 'Projeto desenvolvido com dedicação e boas práticas.')

    descricao_html = f'''
    <p>{descricao_base}</p>

    <h5>Informações do Repositório:</h5>
    <ul>
        <li><strong>Stars:</strong> {repo.get('stargazers_count', 0)} ⭐</li>
        <li><strong>Forks:</strong> {repo.get('forks_count', 0)} 🍴</li>
        <li><strong>Última atualização:</strong> {repo.get('updated_at', 'N/A')}</li>
    </ul>

    <p>Este projeto demonstra conhecimento em desenvolvimento de software,
    seguindo padrões de qualidade e boas práticas de programação.</p>
    '''

    return descricao_html

def importar_projetos(username, limite=10, apenas_com_descricao=True):
    """
    Importa projetos do GitHub para o banco de dados

    Args:
        username (str): Nome de usuário do GitHub
        limite (int): Número máximo de projetos a importar
        apenas_com_descricao (bool): Importar apenas repos com descrição
    """
    repos = buscar_repositorios_github(username)

    if not repos:
        print("❌ Nenhum repositório encontrado.")
        return

    with app.app_context():
        projetos_importados = 0
        projetos_pulados = 0

        print(f"\n📦 Importando até {limite} projetos...")

        for repo in repos[:limite]:
            # Filtrar repositórios
            if apenas_com_descricao and not repo.get('description'):
                projetos_pulados += 1
                continue

            if repo.get('fork'):  # Pular forks
                projetos_pulados += 1
                continue

            # Verificar se já existe
            titulo = repo['name'].replace('-', ' ').replace('_', ' ').title()
            existe = Projeto.query.filter_by(titulo=titulo).first()

            if existe:
                print(f"  ⏭️  Pulado (já existe): {titulo}")
                projetos_pulados += 1
                continue

            # Obter linguagens
            languages = obter_linguagens_repo(repo['languages_url'])

            # Criar projeto
            try:
                projeto = Projeto(
                    titulo=titulo,
                    descricao=criar_descricao(repo),
                    descricao_curta=repo.get('description', 'Projeto do GitHub')[:200],
                    tecnologias=determinar_tecnologias(languages),
                    github_url=repo['html_url'],
                    demo_url=repo.get('homepage') if repo.get('homepage') else None,
                    categoria=determinar_categoria(languages),
                    destaque=repo.get('stargazers_count', 0) > 5,  # Destaque se tem 5+ stars
                    data_criacao=datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                )

                db.session.add(projeto)
                db.session.commit()

                print(f"  ✅ Importado: {titulo}")
                projetos_importados += 1

            except Exception as e:
                print(f"  ❌ Erro ao importar {titulo}: {e}")
                db.session.rollback()

        print(f"\n{'='*60}")
        print(f"✨ Importação concluída!")
        print(f"  • Projetos importados: {projetos_importados}")
        print(f"  • Projetos pulados: {projetos_pulados}")
        print(f"{'='*60}\n")

def main():
    """Função principal"""
    print("\n" + "="*60)
    print("🐙 IMPORTADOR DE PROJETOS DO GITHUB")
    print("="*60 + "\n")

    # Obter username
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Digite seu nome de usuário do GitHub: ").strip()

    if not username:
        print("❌ Nome de usuário inválido!")
        return

    # Configurações
    print("\n⚙️  Configurações:")
    limite_input = input("Quantos projetos importar? (padrão: 10): ").strip()
    limite = int(limite_input) if limite_input.isdigit() else 10

    apenas_com_desc = input("Importar apenas repos com descrição? (s/n, padrão: s): ").lower()
    apenas_com_descricao = apenas_com_desc != 'n'

    # Importar
    importar_projetos(username, limite, apenas_com_descricao)

    print("💡 Dica: Execute 'python app.py' para ver seus projetos no portfólio!\n")

if __name__ == '__main__':
    main()
