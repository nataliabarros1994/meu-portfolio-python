export interface Experience {
  role: string;
  period: string;
  company: string;
  description: string;
  stack: string[];
}

export const experiences: Experience[] = [
  {
    role: 'Desenvolvedora Full Stack — Senior',
    period: '2024 — Presente',
    company: 'Golden Glow IT Solutions · Freelance',
    description:
      'Desenvolvimento end-to-end de SaaS multi-tenant, sites institucionais e MVPs para clientes em saúde, e-commerce e turismo. Stack heterogêneo: Python/Django/FastAPI no back-end, Go (Fiber) para serviços de alta concorrência, Next.js + TypeScript no front. Integrações Stripe, Resend, PIX, Discord. Deploy via Docker e infra própria.',
    stack: ['Python', 'Django', 'FastAPI', 'Go', 'Next.js', 'TypeScript', 'PostgreSQL', 'Docker', 'Stripe'],
  },
  {
    role: 'Desenvolvedora Full Stack — Independente',
    period: '2023 — 2024',
    company: 'Projetos próprios & contratos pontuais',
    description:
      'Construção de plataformas SaaS completas (Discord SaaS, MicroStack), aplicações de visão computacional (EstiMate MVP) e arquiteturas de microserviços com filas (Celery), cache (Redis) e bancos relacionais. Foco em production-readiness desde o primeiro commit.',
    stack: ['Next.js 15', 'TypeScript', 'Prisma', 'FastAPI', 'OpenCV', 'Redis', 'Celery'],
  },
  {
    role: 'Desenvolvedora Python',
    period: '2022 — 2023',
    company: 'Início da carreira · projetos de formação',
    description:
      'APIs RESTful, automação de processos, primeiros sistemas multi-tenant e exploração de robótica com ROS2 (Athena Robotic Framework). Aprofundamento em Python, Flask, Django e fundamentos de engenharia de software.',
    stack: ['Python', 'Flask', 'Django', 'PostgreSQL', 'ROS2', 'Linux'],
  },
];
