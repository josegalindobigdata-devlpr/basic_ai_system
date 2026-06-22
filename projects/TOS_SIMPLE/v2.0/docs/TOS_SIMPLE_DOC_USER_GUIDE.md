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
Secuencia obligatoria de gobierno:
TRUTH -> EVALUATION -> POSITIONING -> EXECUTION
--- 
## Comandos fundamentales

### 1. Comandos de Inicialización y Verdad (TOS_1_BPA)
Uso: Establecer o validar tu identidad, experiencia real y perímetro de credibilidad sin distorsiones.

INITIALIZE_PROFILE: Arranca el sistema cargando tu perfil profesional básico.

VALIDATE_TRUTH: Contrasta tu currículum o perfil actual contra el archivo TOS_1_BPA.md para buscar inconsistencias, lagunas o inflación de títulos.

SET_TARGET: Define o recalibra tu rol objetivo, nivel de liderazgo y expectativas de compensación base.

### 2. Comandos de Evaluación de Oportunidades (TOS_2_OME)
Uso: Filtrar posiciones de forma fría y estratégica antes de comprometer esfuerzo. Evita decisiones reactivas.

EVALUATE_OPPORTUNITY [Datos de la vacante]: Ejecuta el motor de puntuación cruzando la oferta con tu verdad de perfil (BPA). Genera un dictamen obligatorio de GO / NO-GO.

ASSESS_ALIGNMENT: Analiza específicamente la brecha entre el alcance real del puesto propuesto y tus objetivos no negociables.

RECALIBRATE_OME: Actualiza la puntuación si cambian las condiciones iniciales (ej. descubres el rango salarial real o cambia el alcance del rol).

### 3. Comandos de Posicionamiento y Narrativa (TOS_3_CPE)
Uso: Adaptar tu verdad de perfil a la oportunidad aprobada, maximizando la relevancia sin inventar capacidades.

GENERATE_NARRATIVE: Diseña tu propuesta de valor ejecutiva ajustada al modo de posicionamiento óptimo para la vacante activa.

MAP_DIFFERENTIATORS: Destaca tus fortalezas críticas frente a las necesidades específicas descritas por la empresa.

RESOLVE_GAPS: Construye la lógica defensiva para mitigar riesgos detectados en tu perfil (ej. giros de industria o falta de una certificación específica).

### 4. Comandos de Ejecución de Entrevistas (TOS_4_IPE)
Uso: Preparación fina para las distintas fases del proceso de selección y conversión final de ofertas.

PREPARE_ROUND [Tipo de entrevista / Stakeholder]: Genera la estrategia de respuesta, preguntas clave e historias de evidencia (BPA) optimizadas para el entrevistador (ej. Recursos Humanos, Futuro Jefe, Panel Técnico).

MANAGE_OBJECTIONS [Objeción]: Activa el registro de defensa ante preguntas difíciles o ataques directos a tus puntos débiles.

EVALUATE_OFFER [Detalles de la oferta]: Activa el soporte de decisión de oferta analizando leverage de negociación, compensación, alcance y riesgos a largo plazo.

### 5. Comandos de Control de Estado y Contexto (TOS_SHARED_CONTEXT)
Uso: Mantener la sincronización del sistema y prevenir la degradación de la estrategia entre interacciones.

REFRESH_CONTEXT: Revisa el estado actual y emite el paquete mínimo actualizado de TOS_SHARED_CONTEXT. Debe ejecutarse tras cualquier transición de fase.

CHECK_DRIFT: Rastrea inconsistencias entre lo que dices en las entrevistas (IPE) y tu verdad validada (BPA).

LOG_CHANGE [Detalle del cambio]: Indica la modificación estructural o de versión realizada para su registro manual obligatorio en CHANGELOG.md.

Nota de Operación: Para ejecutar cualquier comando de forma efectiva, añade la información o texto correspondiente a continuación del comando para que el sistema procese el módulo exacto requerido.
---
## EJEMPLOS DE USO
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
--- 