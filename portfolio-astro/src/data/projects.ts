export interface Project {
  slug: string;
  title: string;
  icon: string;
  featured: boolean;
  description: string;
  tags: string[];
  githubUrl: string;
}

export const projects: Project[] = [
  {
    slug: 'npx-pdf-brasil',
    title: 'NPX-PDF-BRASIL',
    icon: 'fas fa-file-pdf',
    featured: true,
    description:
      'Plataforma SaaS de manipulação de PDFs com pagamento PIX nativo, semelhante ao iLovePDF mas pensada para o mercado brasileiro. Monorepo Nx com Go 1.22+ (Fiber) no backend, Next.js 14 com TypeScript no frontend, PostgreSQL 16 e Redis. Arquitetura production-ready com Docker.',
    tags: ['Go', 'Fiber', 'Next.js 14', 'TypeScript', 'PostgreSQL', 'Redis', 'Docker'],
    githubUrl: 'https://github.com/nataliabarros1994/NPX-PDF-BRASIL',
  },
  {
    slug: 'veluri',
    title: 'Veluri — Plataforma de Agendamento com IA',
    icon: 'fas fa-calendar-check',
    featured: true,
    description:
      'SaaS multi-tenant de agendamento para PMEs brasileiras (salões, clínicas estéticas, personal trainers, psicólogos). Booking público em 4 passos, painel premium e atendente IA "Aura" em português com 7 tools (Claude tool-use). Lembretes por email via Resend + BullMQ, backend Fastify, Next.js 15, PostgreSQL com Prisma, Redis e Docker em produção.',
    tags: ['Next.js 15', 'TypeScript', 'Fastify', 'PostgreSQL', 'Prisma', 'Redis', 'BullMQ', 'Claude AI', 'Docker'],
    githubUrl: 'https://github.com/nataliabarros1994/plataforma-de-agendamento-com-IA',
  },
  {
    slug: 'customerpulse',
    title: 'CustomerPulse AI — Previsor de Churn',
    icon: 'fas fa-chart-line',
    featured: true,
    description:
      'Projeto de Ciência de Dados que prevê o risco de cancelamento de clientes (churn) com Machine Learning. Modelo Random Forest treinado com Scikit-learn, análise exploratória com Pandas, NumPy, Seaborn e Matplotlib, e dashboard interativo em Streamlit para visualizar as variáveis mais importantes (salário, tempo como cliente) e o score de churn de cada cliente.',
    tags: ['Python', 'Scikit-learn', 'Random Forest', 'Pandas', 'NumPy', 'Streamlit', 'Seaborn', 'Matplotlib'],
    githubUrl: 'https://github.com/nataliabarros1994/customerpulse-ai',
  },
  {
    slug: 'imobia',
    title: 'ImobIA — Mercado Imobiliário do Rio',
    icon: 'fas fa-house-chimney',
    featured: true,
    description:
      'Projeto end-to-end de Ciência de Dados que prevê preços de imóveis no Rio de Janeiro com MAPE de 13.6% (R² = 0.910). Pipeline completo de coleta, limpeza, feature engineering, modelagem supervisionada (Linear, Random Forest, Gradient Boosting, XGBoost, LightGBM) e não-supervisionada (KMeans + PCA), tuning com Optuna e dashboard interativo em Streamlit. Enriquecimento com dados socioeconômicos do IBGE (IDH + renda) explica 54% da variação de preços.',
    tags: ['Python 3.13', 'LightGBM', 'XGBoost', 'Scikit-learn', 'Optuna', 'Pandas', 'NumPy', 'Streamlit', 'KMeans + PCA'],
    githubUrl: 'https://github.com/nataliabarros1994/IMOBIA',
  },
  {
    slug: 'cheesedate',
    title: 'CheeseDate — Automação de Relatórios',
    icon: 'fas fa-file-excel',
    featured: false,
    description:
      'Ferramenta de automação de planilhas Excel que transforma dados brutos de produção de queijos em relatório profissional com 5 abas formatadas, indicadores e gráficos nativos editáveis. Pipeline completo em Python: geração da base, limpeza/validação, análise (produção mensal, ranking de queijos, consumo de matéria-prima, sazonalidade) e exportação automática do .xlsx.',
    tags: ['Python 3.13', 'pandas', 'openpyxl', 'matplotlib', 'pytest', 'ruff'],
    githubUrl: 'https://github.com/nataliabarros1994/cheese-date',
  },
  {
    slug: 'pousada',
    title: 'Pousada Praia do Forte',
    icon: 'fas fa-umbrella-beach',
    featured: false,
    description:
      'Site institucional para pousada em Cabo Frio. Hero com animações sutis de vento, seções de suítes, experiências e depoimentos, e formulário de reserva integrado ao WhatsApp. Tipografia editorial, paleta sereno/areia/terracota, totalmente responsivo e otimizado para SEO local.',
    tags: ['HTML5', 'CSS3', 'JavaScript', 'SVG Animation', 'Responsive', 'SEO'],
    githubUrl: 'https://github.com/nataliabarros1994',
  },
  {
    slug: 'cleantrack',
    title: 'CleanTrack',
    icon: 'fas fa-clipboard-check',
    featured: false,
    description:
      'Plataforma SaaS multi-tenant em Django para rastreamento de limpeza de equipamentos médicos. Registro via QR code, integrações Stripe e Resend, dashboard em tempo real, relatórios auditáveis e suporte a impressoras térmicas (Brother, Zebra, DYMO). Arquitetura HIPAA-safe.',
    tags: ['Python', 'Django', 'PostgreSQL', 'Stripe', 'Multi-tenant', 'HIPAA'],
    githubUrl: 'https://github.com/nataliabarros1994/CLEANTRACK',
  },
  {
    slug: 'estimate',
    title: 'EstiMate MVP',
    icon: 'fas fa-ruler-combined',
    featured: false,
    description:
      'Aplicação de visão computacional que estima materiais de construção a partir de fotos com objetos de referência (cartão, porta) para detecção automática de escala. Detecção via OpenCV, seleção interativa de área e cálculo de tinta/azulejos.',
    tags: ['Python', 'FastAPI', 'OpenCV', 'NumPy', 'React', 'Vite'],
    githubUrl: 'https://github.com/nataliabarros1994/Guided-MVP',
  },
  {
    slug: 'discord',
    title: 'Discord SaaS Platform',
    icon: 'fab fa-discord',
    featured: false,
    description:
      'Plataforma SaaS completa em Next.js 15 com autenticação Clerk, pagamentos Stripe (PRO/FREE), notificações Discord em tempo real e dashboard responsivo de categorias, eventos e quotas. Arquitetura production-ready com TypeScript e Prisma.',
    tags: ['Next.js 15', 'TypeScript', 'Stripe', 'Clerk', 'Prisma', 'Neon DB'],
    githubUrl: 'https://github.com/nataliabarros1994/DISCOR-SAAS',
  },
  {
    slug: 'microstack',
    title: 'MicroStack',
    icon: 'fas fa-layer-group',
    featured: false,
    description:
      'Plataforma SaaS com arquitetura de microserviços, design responsivo, integrações de pagamento (cartão, débito, PayPal, Payoneer), notificações automáticas e dashboard administrativo em tempo real.',
    tags: ['Microserviços', 'FastAPI', 'PostgreSQL', 'Redis', 'Celery', 'Docker'],
    githubUrl: 'https://github.com/nataliabarros1994/microstack',
  },
  {
    slug: 'athena',
    title: 'Athena Robotic Framework',
    icon: 'fas fa-robot',
    featured: false,
    description:
      'Framework modular de robótica em ROS2 Jazzy Jalisco, desenvolvido para Ubuntu 24.04 LTS. Controle e simulação de sistemas robóticos avançados.',
    tags: ['ROS2', 'Python', 'Robótica', 'Ubuntu'],
    githubUrl: 'https://github.com/nataliabarros1994/athena-robotic-framework',
  },
  {
    slug: 'fraud',
    title: 'Sistema de Detecção de Fraudes',
    icon: 'fas fa-shield-alt',
    featured: false,
    description:
      'Detecção de fraudes em tempo real com Inteligência Artificial — machine learning para identificar padrões suspeitos e prevenir transações fraudulentas.',
    tags: ['Python', 'Machine Learning', 'IA', 'Real-time'],
    githubUrl: 'https://github.com/nataliabarros1994/sistema-de-detec-o-de-fraudes-em-tempo-real',
  },
];
