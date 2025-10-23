"""
Build Portfolio - Script Principal
Busca projetos automaticamente do GitHub e constrói o site estático

Autor: Natália Barros
GitHub: nataliabarros1994
"""

import os
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import time

# ============================================
# CONFIGURAÇÕES
# ============================================

GITHUB_USERNAME = "nataliabarros1994"
GITHUB_API_URL = "https://api.github.com"
CACHE_FILE = "projects_data.json"
CACHE_DURATION = timedelta(hours=1)  # Cache válido por 1 hora

# Mapeamento de linguagens para tecnologias/frameworks
TECH_MAPPING = {
    'Python': ['Python', 'Flask', 'Django', 'FastAPI', 'Pandas'],
    'JavaScript': ['JavaScript', 'Node.js', 'React', 'Vue.js'],
    'TypeScript': ['TypeScript', 'Angular', 'Next.js'],
    'Java': ['Java', 'Spring Boot'],
    'Go': ['Go', 'Gin'],
    'Ruby': ['Ruby', 'Rails'],
    'PHP': ['PHP', 'Laravel'],
    'C#': ['C#', '.NET'],
    'HTML': ['HTML5', 'CSS3', 'Bootstrap'],
    'CSS': ['CSS3', 'Sass'],
    'Jupyter Notebook': ['Python', 'Jupyter', 'Data Science'],
    'R': ['R', 'Data Analysis'],
    'Rust': ['Rust'],
    'C++': ['C++'],
    'C': ['C'],
}

# Cores para badges de tecnologias
TECH_COLORS = {
    'Python': '#3776ab',
    'JavaScript': '#f7df1e',
    'TypeScript': '#3178c6',
    'Java': '#007396',
    'Go': '#00add8',
    'Ruby': '#cc342d',
    'PHP': '#777bb4',
    'C#': '#239120',
    'HTML': '#e34f26',
    'CSS': '#1572b6',
    'Rust': '#000000',
}


# ============================================
# FUNÇÕES DE LOGGING
# ============================================

def log_info(message: str):
    """Log informação"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] ℹ️  {message}")


def log_success(message: str):
    """Log sucesso"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] ✅ {message}")


def log_error(message: str):
    """Log erro"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] ❌ {message}")


def log_warning(message: str):
    """Log aviso"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] ⚠️  {message}")


# ============================================
# FUNÇÕES DA GITHUB API
# ============================================

def fetch_github_repos(username: str) -> List[Dict]:
    """
    Busca todos os repositórios públicos de um usuário do GitHub

    Args:
        username: Nome de usuário do GitHub

    Returns:
        Lista de repositórios
    """
    log_info(f"Buscando repositórios de {username}...")

    repos = []
    page = 1
    per_page = 100

    while True:
        url = f"{GITHUB_API_URL}/users/{username}/repos"
        params = {
            'page': page,
            'per_page': per_page,
            'sort': 'updated',
            'direction': 'desc'
        }

        try:
            response = requests.get(url, params=params, timeout=10)

            # Verificar rate limit
            remaining = response.headers.get('X-RateLimit-Remaining')
            if remaining:
                log_info(f"Rate limit restante: {remaining}")

            response.raise_for_status()
            page_repos = response.json()

            if not page_repos:
                break

            repos.extend(page_repos)
            log_info(f"Página {page}: {len(page_repos)} repositórios")

            page += 1
            time.sleep(0.5)  # Evitar rate limit

        except requests.exceptions.RequestException as e:
            log_error(f"Erro ao buscar repositórios: {e}")
            break

    log_success(f"Total de repositórios encontrados: {len(repos)}")
    return repos


def fetch_repo_languages(languages_url: str) -> Dict[str, int]:
    """
    Busca as linguagens de um repositório

    Args:
        languages_url: URL da API de linguagens

    Returns:
        Dicionário com linguagens e bytes de código
    """
    try:
        response = requests.get(languages_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except:
        return {}


def fetch_repo_topics(owner: str, repo: str) -> List[str]:
    """
    Busca os topics de um repositório

    Args:
        owner: Dono do repositório
        repo: Nome do repositório

    Returns:
        Lista de topics
    """
    try:
        url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/topics"
        headers = {'Accept': 'application/vnd.github.mercy-preview+json'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('names', [])
    except:
        return []


# ============================================
# PROCESSAMENTO DE DADOS
# ============================================

def should_include_repo(repo: Dict) -> bool:
    """
    Verifica se o repositório deve ser incluído no portfólio

    Args:
        repo: Dados do repositório

    Returns:
        True se deve incluir, False caso contrário
    """
    # Excluir forks
    if repo.get('fork', False):
        return False

    # Excluir repositórios arquivados
    if repo.get('archived', False):
        return False

    # Excluir repositórios vazios (sem código)
    if repo.get('size', 0) == 0:
        return False

    # Excluir repositórios sem descrição (opcional)
    # if not repo.get('description'):
    #     return False

    return True


def determine_technologies(languages: Dict[str, int]) -> List[str]:
    """
    Determina as tecnologias baseado nas linguagens

    Args:
        languages: Dicionário com linguagens e bytes

    Returns:
        Lista de tecnologias
    """
    technologies = set()

    # Ordenar linguagens por quantidade de bytes (mais usada primeiro)
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)

    for language, _ in sorted_languages[:3]:  # Top 3 linguagens
        if language in TECH_MAPPING:
            # Adicionar linguagem principal
            technologies.add(language)
            # Adicionar framework comum (se houver)
            if len(TECH_MAPPING[language]) > 1:
                technologies.add(TECH_MAPPING[language][1])

    return sorted(list(technologies))


def get_demo_url(repo: Dict) -> Optional[str]:
    """
    Tenta encontrar URL de demonstração do projeto

    Args:
        repo: Dados do repositório

    Returns:
        URL de demo ou None
    """
    # Homepage do repositório
    if repo.get('homepage') and repo['homepage'].startswith('http'):
        return repo['homepage']

    # GitHub Pages
    if repo.get('has_pages', False):
        owner = repo['owner']['login']
        name = repo['name']
        return f"https://{owner}.github.io/{name}"

    return None


def format_repo_title(name: str) -> str:
    """
    Formata o nome do repositório para um título legível

    Args:
        name: Nome do repositório

    Returns:
        Título formatado
    """
    # Substituir hífens e underscores por espaços
    title = name.replace('-', ' ').replace('_', ' ')
    # Capitalizar cada palavra
    title = ' '.join(word.capitalize() for word in title.split())
    return title


def process_repository(repo: Dict) -> Dict:
    """
    Processa um repositório e extrai informações relevantes

    Args:
        repo: Dados brutos do repositório

    Returns:
        Dados processados do projeto
    """
    log_info(f"Processando: {repo['name']}")

    # Buscar linguagens
    languages = fetch_repo_languages(repo['languages_url'])

    # Buscar topics
    topics = fetch_repo_topics(repo['owner']['login'], repo['name'])

    # Determinar tecnologias
    technologies = determine_technologies(languages)

    # Se não encontrou tecnologias e tem language principal
    if not technologies and repo.get('language'):
        technologies = [repo['language']]

    # Processar datas
    created_at = datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    updated_at = datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ')

    # Verificar se foi atualizado recentemente (últimos 30 dias)
    is_recent = (datetime.now() - updated_at).days <= 30

    project = {
        'id': repo['id'],
        'name': repo['name'],
        'title': format_repo_title(repo['name']),
        'description': repo.get('description', 'Projeto desenvolvido com dedicação'),
        'language': repo.get('language', 'Outras'),
        'languages': list(languages.keys()),
        'technologies': technologies,
        'github_url': repo['html_url'],
        'demo_url': get_demo_url(repo),
        'stars': repo['stargazers_count'],
        'forks': repo['forks_count'],
        'watchers': repo['watchers_count'],
        'created_at': created_at.strftime('%Y-%m-%d'),
        'updated_at': updated_at.strftime('%Y-%m-%d'),
        'topics': topics,
        'has_wiki': repo.get('has_wiki', False),
        'has_pages': repo.get('has_pages', False),
        'is_recent': is_recent,
        'size': repo.get('size', 0),
    }

    time.sleep(0.3)  # Pequeno delay entre requisições

    return project


# ============================================
# CACHE
# ============================================

def load_cache() -> Optional[Dict]:
    """
    Carrega cache de projetos se existir e for válido

    Returns:
        Dados do cache ou None
    """
    if not os.path.exists(CACHE_FILE):
        return None

    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            cache = json.load(f)

        # Verificar se cache ainda é válido
        cached_time = datetime.fromisoformat(cache['timestamp'])
        if datetime.now() - cached_time < CACHE_DURATION:
            log_success(f"Cache válido encontrado ({cache['timestamp']})")
            return cache
        else:
            log_warning("Cache expirado")
            return None

    except Exception as e:
        log_error(f"Erro ao carregar cache: {e}")
        return None


def save_cache(projects: List[Dict], stats: Dict):
    """
    Salva projetos em cache

    Args:
        projects: Lista de projetos
        stats: Estatísticas gerais
    """
    cache = {
        'timestamp': datetime.now().isoformat(),
        'username': GITHUB_USERNAME,
        'projects': projects,
        'stats': stats,
        'count': len(projects)
    }

    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)
        log_success(f"Cache salvo: {len(projects)} projetos")
    except Exception as e:
        log_error(f"Erro ao salvar cache: {e}")


# ============================================
# ESTATÍSTICAS
# ============================================

def calculate_stats(projects: List[Dict]) -> Dict:
    """
    Calcula estatísticas dos projetos

    Args:
        projects: Lista de projetos

    Returns:
        Dicionário com estatísticas
    """
    total_stars = sum(p['stars'] for p in projects)
    total_forks = sum(p['forks'] for p in projects)

    # Linguagens mais usadas
    languages = {}
    for project in projects:
        for lang in project['languages']:
            languages[lang] = languages.get(lang, 0) + 1

    top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]

    # Tecnologias mais usadas
    technologies = {}
    for project in projects:
        for tech in project['technologies']:
            technologies[tech] = technologies.get(tech, 0) + 1

    top_technologies = sorted(technologies.items(), key=lambda x: x[1], reverse=True)[:10]

    # Projetos em destaque (com mais stars)
    featured_projects = sorted(projects, key=lambda x: x['stars'], reverse=True)[:6]

    return {
        'total_projects': len(projects),
        'total_stars': total_stars,
        'total_forks': total_forks,
        'top_languages': [{'name': lang, 'count': count} for lang, count in top_languages],
        'top_technologies': [{'name': tech, 'count': count} for tech, count in top_technologies],
        'featured_projects': [p['id'] for p in featured_projects],
        'recent_projects': len([p for p in projects if p['is_recent']]),
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }


# ============================================
# BUILD PRINCIPAL
# ============================================

def build_portfolio(force_refresh: bool = False):
    """
    Função principal que constrói o portfólio

    Args:
        force_refresh: Se True, ignora cache e busca novos dados
    """
    print("\n" + "="*60)
    print("🚀 BUILD PORTFOLIO - INTEGRAÇÃO GITHUB")
    print("="*60 + "\n")

    # Tentar carregar cache
    if not force_refresh:
        cache = load_cache()
        if cache:
            log_success("Usando dados do cache")
            return cache

    # Buscar repositórios do GitHub
    repos = fetch_github_repos(GITHUB_USERNAME)

    if not repos:
        log_error("Nenhum repositório encontrado!")
        return None

    # Filtrar repositórios
    log_info("Filtrando repositórios...")
    filtered_repos = [repo for repo in repos if should_include_repo(repo)]
    log_success(f"Repositórios após filtros: {len(filtered_repos)}")

    # Processar cada repositório
    projects = []
    total = len(filtered_repos)

    print(f"\n📦 Processando {total} repositórios...\n")

    for i, repo in enumerate(filtered_repos, 1):
        print(f"[{i}/{total}] ", end='')
        try:
            project = process_repository(repo)
            projects.append(project)
        except Exception as e:
            log_error(f"Erro ao processar {repo['name']}: {e}")

    # Calcular estatísticas
    log_info("\n📊 Calculando estatísticas...")
    stats = calculate_stats(projects)

    # Salvar cache
    save_cache(projects, stats)

    # Salvar dados para frontend
    save_frontend_data(projects, stats)

    # Exibir resumo
    print("\n" + "="*60)
    print("✨ BUILD CONCLUÍDO COM SUCESSO!")
    print("="*60)
    print(f"\n📊 Resumo:")
    print(f"  • Total de projetos: {stats['total_projects']}")
    print(f"  • Total de stars: {stats['total_stars']}")
    print(f"  • Total de forks: {stats['total_forks']}")
    print(f"  • Projetos recentes: {stats['recent_projects']}")
    print(f"  • Última atualização: {stats['last_updated']}")
    print("\n" + "="*60 + "\n")

    return {'projects': projects, 'stats': stats}


def save_frontend_data(projects: List[Dict], stats: Dict):
    """
    Salva dados para uso no frontend

    Args:
        projects: Lista de projetos
        stats: Estatísticas
    """
    os.makedirs('static/data', exist_ok=True)

    data = {
        'projects': projects,
        'stats': stats,
        'generated_at': datetime.now().isoformat()
    }

    try:
        with open('static/data/projects.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        log_success("Dados salvos para frontend: static/data/projects.json")
    except Exception as e:
        log_error(f"Erro ao salvar dados do frontend: {e}")


# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    import sys

    force_refresh = '--force' in sys.argv or '-f' in sys.argv

    if force_refresh:
        log_info("Modo force refresh ativado")

    result = build_portfolio(force_refresh=force_refresh)

    if result:
        print("💡 Próximos passos:")
        print("  1. Execute: python freeze.py")
        print("  2. Teste: abra docs/index.html no navegador")
        print("  3. Deploy: git push origin main\n")
    else:
        log_error("Build falhou!")
        sys.exit(1)
