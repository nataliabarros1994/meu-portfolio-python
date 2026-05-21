export type Lang = 'pt' | 'en';

export const translations = {
  pt: {
    nav: {
      experience: 'Experiência',
      about: 'Sobre',
      projects: 'Projetos',
      contact: 'Contato',
    },
    hero: {
      status: 'Disponível para novos projetos',
      greeting: 'Olá, eu sou Natália Barros',
      title: 'Desenvolvedora',
      titleAccent: 'Full Stack',
      subtitle:
        'Construo aplicações web modernas com <span class="hl">Python, TypeScript e Go</span> — do back ao front, do MVP à escala.',
      ctaProjects: 'Ver Projetos',
      ctaContact: 'Conversar',
    },
    experience: {
      eyebrow: 'trajetória',
      title: 'Experiência',
      titleAccent: 'Profissional',
      subtitle:
        'Construindo produtos digitais de ponta a ponta — do back-end Python ao front-end Next.js.',
      items: [
        {
          role: 'Desenvolvedora Full Stack — Senior',
          period: '2024 — Presente',
          company: 'Golden Glow IT Solutions · Freelance',
          desc: 'Desenvolvimento end-to-end de SaaS multi-tenant, sites institucionais e MVPs para clientes em saúde, e-commerce e turismo. Stack heterogêneo: Python/Django/FastAPI no back-end, Go (Fiber) para serviços de alta concorrência, Next.js + TypeScript no front. Integrações Stripe, Resend, PIX, Discord. Deploy via Docker e infra própria.',
        },
        {
          role: 'Desenvolvedora Full Stack — Independente',
          period: '2023 — 2024',
          company: 'Projetos próprios & contratos pontuais',
          desc: 'Construção de plataformas SaaS completas (Discord SaaS, MicroStack), aplicações de visão computacional (EstiMate MVP) e arquiteturas de microserviços com filas (Celery), cache (Redis) e bancos relacionais. Foco em production-readiness desde o primeiro commit.',
        },
        {
          role: 'Desenvolvedora Python',
          period: '2022 — 2023',
          company: 'Início da carreira · projetos de formação',
          desc: 'APIs RESTful, automação de processos, primeiros sistemas multi-tenant e exploração de robótica com ROS2 (Athena Robotic Framework). Aprofundamento em Python, Flask, Django e fundamentos de engenharia de software.',
        },
      ],
    },
    about: {
      eyebrow: 'sobre mim',
      title: 'Resolvendo problemas com',
      titleAccent: 'código que dura.',
      p1: 'Sou desenvolvedora <strong>Full Stack</strong>. Trabalho confortavelmente nos dois lados da stack — back-end em <strong>Python (Django, FastAPI)</strong>, <strong>Go</strong> e <strong>Node.js</strong>; front-end em <strong>Next.js</strong>, <strong>React</strong> e <strong>TypeScript</strong>.',
      p2: 'Faço produto: do esboço da arquitetura à integração de pagamento, do schema do banco ao deploy. Não tenho preferência religiosa por linguagem — uso o que faz sentido para o problema.',
      p3: 'Já entreguei MVPs em visão computacional, plataformas SaaS multi-tenant em produção, microserviços com filas e cache, e sites institucionais com performance impecável. Foco em código limpo, observável e que outras pessoas conseguem ler depois.',
      stats: {
        experience: 'anos de experiência',
        projects: 'projetos entregues',
        languages: 'linguagens & frameworks',
        delivery: 'comprometimento',
      },
    },
    skills: { backend: 'Back-end', frontend: 'Front-end', data: 'Dados & infra' },
    projects: {
      eyebrow: 'portfólio',
      title: 'Projetos em',
      titleAccent: 'destaque',
      subtitle:
        'Uma seleção dos trabalhos mais recentes — SaaS, agendamento com IA, ciência de dados, visão computacional, microserviços, site institucional e robótica.',
      featured: 'em destaque',
      viewCode: 'Ver no GitHub',
      descriptions: {
        'npx-pdf-brasil':
          'Plataforma SaaS de manipulação de PDFs com pagamento PIX nativo, semelhante ao iLovePDF mas pensada para o mercado brasileiro. Monorepo Nx com Go 1.22+ (Fiber) no backend, Next.js 14 com TypeScript no frontend, PostgreSQL 16 e Redis. Arquitetura production-ready com Docker.',
        veluri:
          'SaaS multi-tenant de agendamento para PMEs brasileiras (salões, clínicas estéticas, personal trainers, psicólogos). Booking público em 4 passos, painel premium e atendente IA "Aura" em português com 7 tools (Claude tool-use). Lembretes por email via Resend + BullMQ, backend Fastify, Next.js 15, PostgreSQL com Prisma, Redis e Docker em produção.',
        customerpulse:
          'Projeto de Ciência de Dados que prevê o risco de cancelamento de clientes (churn) com Machine Learning. Modelo Random Forest treinado com Scikit-learn, análise exploratória com Pandas, NumPy, Seaborn e Matplotlib, e dashboard interativo em Streamlit para visualizar as variáveis mais importantes (salário, tempo como cliente) e o score de churn de cada cliente.',
        imobia:
          'Projeto end-to-end de Ciência de Dados que prevê preços de imóveis no Rio de Janeiro com MAPE de 13.6% (R² = 0.910). Pipeline completo de coleta, limpeza, feature engineering, modelagem supervisionada (Linear, Random Forest, Gradient Boosting, XGBoost, LightGBM) e não-supervisionada (KMeans + PCA), tuning com Optuna e dashboard interativo em Streamlit. Enriquecimento com dados socioeconômicos do IBGE (IDH + renda) explica 54% da variação de preços.',
        cheesedate:
          'Ferramenta de automação de planilhas Excel que transforma dados brutos de produção de queijos em relatório profissional com 5 abas formatadas, indicadores e gráficos nativos editáveis. Pipeline completo em Python: geração da base, limpeza/validação, análise (produção mensal, ranking de queijos, consumo de matéria-prima, sazonalidade) e exportação automática do .xlsx.',
        pousada:
          'Site institucional para pousada em Cabo Frio. Hero com animações sutis de vento, seções de suítes, experiências e depoimentos, e formulário de reserva integrado ao WhatsApp. Tipografia editorial, paleta sereno/areia/terracota, totalmente responsivo e otimizado para SEO local.',
        cleantrack:
          'Plataforma SaaS multi-tenant em Django para rastreamento de limpeza de equipamentos médicos. Registro via QR code, integrações Stripe e Resend, dashboard em tempo real, relatórios auditáveis e suporte a impressoras térmicas (Brother, Zebra, DYMO). Arquitetura HIPAA-safe.',
        estimate:
          'Aplicação de visão computacional que estima materiais de construção a partir de fotos com objetos de referência (cartão, porta) para detecção automática de escala. Detecção via OpenCV, seleção interativa de área e cálculo de tinta/azulejos.',
        discord:
          'Plataforma SaaS completa em Next.js 15 com autenticação Clerk, pagamentos Stripe (PRO/FREE), notificações Discord em tempo real e dashboard responsivo de categorias, eventos e quotas. Arquitetura production-ready com TypeScript e Prisma.',
        microstack:
          'Plataforma SaaS com arquitetura de microserviços, design responsivo, integrações de pagamento (cartão, débito, PayPal, Payoneer), notificações automáticas e dashboard administrativo em tempo real.',
        athena:
          'Framework modular de robótica em ROS2 Jazzy Jalisco, desenvolvido para Ubuntu 24.04 LTS. Controle e simulação de sistemas robóticos avançados.',
        fraud:
          'Detecção de fraudes em tempo real com Inteligência Artificial — machine learning para identificar padrões suspeitos e prevenir transações fraudulentas.',
      },
    },
    contact: {
      eyebrow: 'vamos conversar',
      title: 'Tem um projeto em',
      titleAccent: 'mente?',
      subtitle:
        'Estou aceitando novos projetos a partir do próximo mês. Respondo todas as mensagens em até 24 horas.',
      btnWhatsapp: 'Falar no WhatsApp',
      btnEmail: 'Enviar e-mail',
    },
    footer: {
      rights: 'todos os direitos reservados',
      built: 'construído com',
    },
  },
  en: {
    nav: {
      experience: 'Experience',
      about: 'About',
      projects: 'Projects',
      contact: 'Contact',
    },
    hero: {
      status: 'Available for new projects',
      greeting: "Hi, I'm Natália Barros",
      title: 'Full Stack',
      titleAccent: 'Developer',
      subtitle:
        'I build modern web applications with <span class="hl">Python, TypeScript and Go</span> — from back to front, from MVP to scale.',
      ctaProjects: 'View Projects',
      ctaContact: 'Get in Touch',
    },
    experience: {
      eyebrow: 'journey',
      title: 'Professional',
      titleAccent: 'Experience',
      subtitle: 'Building digital products end-to-end — from Python back-end to Next.js front-end.',
      items: [
        {
          role: 'Senior Full Stack Developer',
          period: '2024 — Present',
          company: 'Golden Glow IT Solutions · Freelance',
          desc: 'End-to-end development of multi-tenant SaaS, institutional websites and MVPs for clients in healthcare, e-commerce and tourism. Heterogeneous stack: Python/Django/FastAPI on the backend, Go (Fiber) for high-concurrency services, Next.js + TypeScript on the front. Stripe, Resend, PIX and Discord integrations. Deploys via Docker and own infra.',
        },
        {
          role: 'Independent Full Stack Developer',
          period: '2023 — 2024',
          company: 'Personal projects & contract work',
          desc: 'Built complete SaaS platforms (Discord SaaS, MicroStack), computer vision applications (EstiMate MVP) and microservice architectures with queues (Celery), cache (Redis) and relational databases. Focused on production-readiness from commit one.',
        },
        {
          role: 'Python Developer',
          period: '2022 — 2023',
          company: 'Early career · training projects',
          desc: 'RESTful APIs, process automation, first multi-tenant systems and robotics exploration with ROS2 (Athena Robotic Framework). Deepened skills in Python, Flask, Django and software engineering fundamentals.',
        },
      ],
    },
    about: {
      eyebrow: 'about me',
      title: 'Solving problems with',
      titleAccent: 'code that lasts.',
      p1: "I'm a <strong>Full Stack</strong> developer. I work comfortably on both sides of the stack — back-end in <strong>Python (Django, FastAPI)</strong>, <strong>Go</strong> and <strong>Node.js</strong>; front-end in <strong>Next.js</strong>, <strong>React</strong> and <strong>TypeScript</strong>.",
      p2: 'I build product: from the architecture sketch to payment integration, from the database schema to the deploy. I have no religious preference for any language — I use what makes sense for the problem.',
      p3: "I've shipped computer-vision MVPs, multi-tenant SaaS platforms in production, microservices with queues and cache, and institutional websites with impeccable performance. Focused on clean, observable code that other people can read later.",
      stats: {
        experience: 'years of experience',
        projects: 'projects delivered',
        languages: 'languages & frameworks',
        delivery: 'commitment',
      },
    },
    skills: { backend: 'Back-end', frontend: 'Front-end', data: 'Data & infra' },
    projects: {
      eyebrow: 'portfolio',
      title: 'Featured',
      titleAccent: 'projects',
      subtitle:
        'A selection of recent work — SaaS, AI scheduling, data science, computer vision, microservices, institutional sites and robotics.',
      featured: 'featured',
      viewCode: 'View on GitHub',
      descriptions: {
        'npx-pdf-brasil':
          'PDF-manipulation SaaS with native PIX payments, similar to iLovePDF but tailored for the Brazilian market. Nx monorepo with Go 1.22+ (Fiber) on the backend, Next.js 14 with TypeScript on the frontend, PostgreSQL 16 and Redis. Production-ready architecture with Docker.',
        veluri:
          'Multi-tenant scheduling SaaS for Brazilian SMBs (beauty salons, aesthetic clinics, personal trainers, therapists). 4-step public booking, premium dashboard and an in-Portuguese AI assistant "Aura" with 7 tools (Claude tool-use). Email reminders via Resend + BullMQ, Fastify backend, Next.js 15, PostgreSQL with Prisma, Redis and Docker in production.',
        customerpulse:
          "Data Science project that predicts customer churn risk with Machine Learning. Random Forest model trained with Scikit-learn, exploratory analysis with Pandas, NumPy, Seaborn and Matplotlib, and an interactive Streamlit dashboard to visualize the most important features (salary, tenure) and each customer's churn score.",
        imobia:
          'End-to-end Data Science project that predicts real-estate prices in Rio de Janeiro with 13.6% MAPE (R² = 0.910). Full pipeline of collection, cleaning, feature engineering, supervised modeling (Linear, Random Forest, Gradient Boosting, XGBoost, LightGBM) and unsupervised modeling (KMeans + PCA), hyperparameter tuning with Optuna and an interactive Streamlit dashboard. Enrichment with IBGE socioeconomic data (HDI + income) explains 54% of price variation.',
        cheesedate:
          'Excel automation tool that turns raw cheese production data into a professional report with 5 formatted tabs, KPIs and editable native charts. Full Python pipeline: dataset generation, cleaning/validation, analysis (monthly production, cheese ranking, raw-material consumption, seasonality) and automatic .xlsx export.',
        pousada:
          'Institutional website for an inn in Cabo Frio. Hero with subtle wind animations, sections for suites, experiences and testimonials, and a reservation form integrated with WhatsApp. Editorial typography, serene/sand/terracotta palette, fully responsive and optimized for local SEO.',
        cleantrack:
          'Multi-tenant Django SaaS platform for tracking medical equipment cleaning. QR code registration, Stripe and Resend integrations, real-time dashboard, auditable reports and thermal printer support (Brother, Zebra, DYMO). HIPAA-safe architecture.',
        estimate:
          'Computer vision app that estimates construction materials from photos using reference objects (credit card, door) for automatic scale detection. OpenCV detection, interactive area selection and paint/tile calculation.',
        discord:
          'Full SaaS platform in Next.js 15 with Clerk auth, Stripe payments (PRO/FREE), real-time Discord notifications and a responsive dashboard for categories, events and quotas. Production-ready with TypeScript and Prisma.',
        microstack:
          'SaaS platform with microservices architecture, responsive design, payment integrations (card, debit, PayPal, Payoneer), automatic notifications and real-time admin dashboard.',
        athena:
          'Modular robotics framework in ROS2 Jazzy Jalisco, built for Ubuntu 24.04 LTS. Control and simulation of advanced robotic systems.',
        fraud:
          'Real-time fraud detection with AI — machine learning to identify suspicious patterns and prevent fraudulent transactions.',
      },
    },
    contact: {
      eyebrow: "let's talk",
      title: 'Got a project in',
      titleAccent: 'mind?',
      subtitle:
        "I'm taking on new projects starting next month. I respond to all messages within 24 hours.",
      btnWhatsapp: 'Talk on WhatsApp',
      btnEmail: 'Send an email',
    },
    footer: {
      rights: 'all rights reserved',
      built: 'built with',
    },
  },
} as const;
