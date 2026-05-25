# TOS_SIMPLE_USER_GUIDE
## Proyecto Principal: TOS_SIMPLE
Dentro del proyecto subirías:

TOS_MASTER.md
TOS_SHARED_CONTEXT.md
TOS_1_BPA.md
TOS_2_OME.md
TOS_3_CPE.md
TOS_4_IPE.md
CHANGELOG.md

Y adicionalmente:

CV_MASTER.md
LINKEDIN_MASTER.md
TARGET_ROLES.md
ACTIVE_OPPORTUNITIES.md
INTERVIEW_LOG.md
--- 
 
## Arquitectura Optima de Chats
No mezcles todo en una única conversación infinita.

Mejor:

|Chat |	Función | Elementos |
|---|---|---|
|BPA Session | Validación perfil | validar perfil, construir Profile_Master, detectar gaps |
|OME Session | Evaluación oportunidades | valoración oportunidades |
|CPE Session | Adaptación CV | adaptar CV, recruiter pitch, storytelling |
|IPE Session | Preparación entrevistas | simulación entrevistas, defense, narrative |
|Governance Session	| Cambios arquitectura | versionado, cambios estructurales, evolución |

---
## Arquitectura operativa recomendada (final)
TOS_SIMPLE
│
├── TOS_MASTER.md
├── TOS_SHARED_CONTEXT.md
├── TOS_1_BPA.md
├── TOS_2_OME.md
├── TOS_3_CPE.md
├── TOS_4_IPE.md
├── CHANGELOG.md
│
├── CV_MASTER.md
├── LINKEDIN_MASTER.md
├── ACTIVE_OPPORTUNITIES.md
└── INTERVIEW_LOG.md
│
├── Chat: BPA_CORE
├── Chat: OME_PIPELINE
├── Chat: CPE_FACTORY
├── Chat: IPE_PREP
└── Chat: GOVERNANCE
---
## Flujo Recomendado
### PASO 1 — Construcción PROFILE_MASTER
Usa TOS_1_BPA para construir mi PROFILE_MASTER validado.

Analiza:
- coherencia cronológica,
- seniority real,
- capacidad defensible,
- fortalezas estratégicas,
- gaps,
- positioning ceiling,
- riesgos de credibilidad.

No optimices narrativa todavía.
Solo valida verdad profesional.

### PASO 2 - Auditoria de Inconsistencias
Realiza una auditoría BPA completa.

Detecta:
- inconsistencias entre CV y LinkedIn,
- title inflation,
- claims débiles,
- gaps mal explicados,
- problemas ATS,
- seniority ambiguity,
- riesgos de percepción recruiter.

Clasifica:
- riesgo bajo,
- medio,
- alto.
