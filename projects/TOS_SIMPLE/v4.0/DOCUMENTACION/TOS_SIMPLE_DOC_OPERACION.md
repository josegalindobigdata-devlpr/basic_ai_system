# TOS_SIMPLE — GUÍA DE OPERACIÓN
<!-- TOS_SIMPLE v4.0 — Arquitectura de 4 capas -->

VERSION_DOC: 2.0
SYSTEM VERSION: SIMPLE_4.0
PLATFORM: Claude Projects
PURPOSE: Guía operativa completa — escenarios de ejecución, comandos y plantillas

---

## 1. MODELO OPERATIVO

TOS_SIMPLE opera dentro de un **Claude Project** único con todos los ficheros cargados en la base de conocimiento.
El asistente lee los módulos relevantes en cada invocación y produce outputs trazables a la CAPA DATO.

**Principio:** la sesión de chat es el orquestador. El usuario inicia; el sistema resuelve.

**Input mínimo garantizado por oportunidad:** `TÍTULO + DESCRIPCIÓN`. Cualquier dato adicional mejora la ejecución, pero su ausencia no bloquea.

---

## 2. PIPELINE Y SECUENCIA

```
BPA (una vez) ──> OME ──[GO/GO-ADJ]──> CPE ──[entrevista]──> IPE ──> CLOSE
```

| Paso | Módulo | Cuándo ejecutar | Prerequisito |
|---|---|---|---|
| Validación de perfil | TOS_1_BPA | Una sola vez (salvo cambio real de CV) | Ninguno |
| Evaluación de oportunidad | TOS_2_OME | Por cada oportunidad nueva | BPA ejecutado |
| Posicionamiento + CV | TOS_3_CPE | Solo si OME = GO o GO WITH ADJUSTMENT | OME con decisión |
| Preparación de entrevista | TOS_4_IPE | Solo si hay entrevista confirmada | CPE completado |
| Cierre | Manual | Al recibir oferta o descartar | IPE / OME NO GO |

**Reglas de secuencia (no se saltan):**
- No CPE sin OME = GO o GO WITH ADJUSTMENT.
- No IPE sin CPE completado.
- NO GO cierra la oportunidad. Sin avance.

---

## 3. ESCENARIOS DE EJECUCIÓN

---

### ESCENARIO A — VALIDACIÓN DE PERFIL (BPA)
**Objetivo:** establecer la verdad profesional base. Se ejecuta **una sola vez**.

**Cuándo repetir:** solo si el CV real cambia (nuevo rol, nueva certificación, nuevo cliente relevante).

**Prompt de activación:**
```
Ejecuta TOS_1_BPA.

Construye el PROFILE_MASTER validado analizando:
- coherencia cronológica
- seniority real y defensible
- capacidades trazables
- fortalezas estratégicas
- gaps y riesgos de credibilidad
- positioning ceiling

No optimices narrativa todavía. Solo valida verdad profesional.
```

**Output esperado:** PROFILE_MASTER con verdict BPA (VALIDATED / CONDITIONAL / BLOCKED).

---

### ESCENARIO B — EVALUACIÓN DE OPORTUNIDAD (OME)
**Objetivo:** decidir si la oportunidad merece esfuerzo. GO / GO WITH ADJUSTMENT / NO GO.

**Input mínimo:** título del puesto + descripción de la oferta.
**Input recomendado:** empresa, compensación, reporting, modalidad.

**Prompt de activación:**
```
Ejecuta TOS_2_OME para la siguiente oportunidad:

TÍTULO: [título del puesto]
EMPRESA: [empresa — si disponible]
DESCRIPCIÓN: [pegar JD completa]
COMPENSACIÓN: [si disponible]
REPORTING: [si disponible]

Produce el análisis completo con Anchor Resolution, FIT/GAP, scoring, RISK MATRIX y decisión GO/NO-GO.
```

**Output esperado:** decisión GO / GO WITH ADJUSTMENT / NO GO + ancla seleccionada + riesgos activos.

**Si NO GO:** oportunidad cerrada. No avanzar a CPE.

---

### ESCENARIO C — POSICIONAMIENTO Y CV (CPE)
**Objetivo:** adaptar narrativa y ensamblar CV para la oportunidad validada.

**Prerequisito:** OME = GO o GO WITH ADJUSTMENT.

**Prompt — análisis de posicionamiento:**
```
Ejecuta TOS_3_CPE para [título del puesto / empresa].

Ancla base (según OME): [SDM / GOV / DLV]
Decisión OME: [GO / GO WITH ADJUSTMENT]
Riesgos activos: [lista de riesgos del OME]

Produce: Positioning Summary, propuesta de valor, diferenciadores, mitigación de gaps
y estrategia de narrativa para esta oportunidad.
```

**Prompt — ensamblaje de CV:**
```
Con el posicionamiento definido, ensambla el CV ADAPTADO para [título / empresa].

Ancla base: CV_ANCLA_[SDM/GOV/DLV]_ESP
Operaciones del Contrato de Adaptación §4A a aplicar:
- [indicar: reordenación / énfasis / adición de piezas PORTFOLIO / matiz]

Produce el CV ADAPTADO completo (Tier 2 — efímero).
```

**Output esperado:** análisis de posicionamiento + CV ADAPTADO listo para envío.

**Nota:** el CV ADAPTADO es efímero. No se guarda como SSOT. Se descarta tras su uso.

---

### ESCENARIO D — PREPARACIÓN DE ENTREVISTA (IPE)
**Objetivo:** convertir el posicionamiento en rendimiento real en entrevista.

**Prerequisito:** CPE completado para esta oportunidad.

**Prompt de activación:**
```
Ejecuta TOS_4_IPE para [título / empresa].

Tipo de entrevista: [RRHH / Hiring Manager / Panel Técnico / SteerCo]
Etapa: [primera llamada / segunda ronda / final]
Riesgos activos a defender: [lista]
Preguntas esperadas: [si las conoces]

Produce: estrategia de respuesta, historias STAR prioritarias, gestión de objeciones
y preguntas de cierre.
```

**Output esperado:** kit completo de preparación para la ronda específica.

---

### ESCENARIO E — CIERRE (CLOSE)
**Objetivo:** evaluar oferta y tomar decisión final.

**Prompt — evaluación de oferta:**
```
Evalúa la siguiente oferta para [título / empresa]:

COMPENSACIÓN: [detalle]
ALCANCE DEL ROL: [descripción]
CONDICIONES: [contrato, modalidad, beneficios]
PALANCAS DE NEGOCIACIÓN DISPONIBLES: [otras ofertas, timing, etc.]

Produce: análisis de leverage, recomendación de negociación y decisión ACCEPT / REJECT / NEGOTIATE.
```

---

## 4. COMANDOS DE REFERENCIA

### Módulo BPA — Validación de Verdad

| Comando | Uso |
|---|---|
| `VALIDATE_PROFILE` | Validar coherencia, seniority y defensibilidad del perfil completo |
| `AUDIT_INCONSISTENCIES` | Detectar gaps, title inflation, claims débiles, riesgos ATS/recruiter |
| `RECALIBRATE_BPA` | Re-ejecutar BPA tras cambio real en el CV (nuevo rol, nueva certificación) |

### Módulo OME — Evaluación de Oportunidades

| Comando | Uso |
|---|---|
| `EVALUATE_OPPORTUNITY [JD]` | Evaluación GO/NO-GO con scoring, FIT/GAP y Anchor Resolution |
| `ASSESS_ALIGNMENT` | Analizar brecha entre la oferta y los no-negociables del titular |
| `RECALIBRATE_OME` | Actualizar scoring si cambian condiciones (compensación real, alcance revisado) |

### Módulo CPE — Posicionamiento y CV

| Comando | Uso |
|---|---|
| `GENERATE_NARRATIVE` | Propuesta de valor ejecutiva ajustada a la oportunidad activa |
| `MAP_DIFFERENTIATORS` | Fortalezas críticas vs necesidades específicas de la empresa |
| `RESOLVE_GAPS` | Lógica defensiva para mitigar riesgos detectados en OME |
| `ASSEMBLE_CV [ancla] [operaciones]` | Ensamblar CV ADAPTADO (Tier 2) según Contrato de Adaptación §4A |

### Módulo IPE — Ejecución de Entrevistas

| Comando | Uso |
|---|---|
| `PREPARE_ROUND [tipo / stakeholder]` | Estrategia, preguntas clave e historias STAR para la ronda específica |
| `MANAGE_OBJECTIONS [objeción]` | Defensa ante preguntas difíciles o ataques a puntos débiles |
| `EVALUATE_OFFER [detalle]` | Análisis de leverage, negociación y decisión final de oferta |

### Control de Estado y Contexto

| Comando | Uso |
|---|---|
| `REFRESH_CONTEXT` | Snapshot del contexto activo (SHARED_CONTEXT) tras cualquier transición de fase |
| `CHECK_DRIFT` | Verificar coherencia entre narrativa de entrevistas (IPE) y verdad validada (BPA) |
| `LOG_CHANGE [detalle]` | Registrar en CHANGELOG cualquier cambio estructural o de versión |

---

## 5. PLANTILLAS DE PROMPT

### Plantilla universal (inicio de sesión)

```
MÓDULO ACTIVO: [BPA / OME / CPE / IPE]
OPORTUNIDAD ACTIVA: [título — empresa]
DECISIÓN OME: [GO / GO WITH ADJUSTMENT / NO GO / pendiente]
ANCLA SELECCIONADA: [SDM / GOV / DLV / pendiente]
RIESGOS ACTIVOS: [lista corta]

TAREA:
[descripción de la tarea concreta]

CONTEXTO / INPUT:
[pegar JD, notas de entrevista, oferta o lo que aplique]
```

### Plantilla mínima (uso rápido)

```
[MÓDULO]: [tarea concreta]
[INPUT]: [datos relevantes]
```

---

## 6. ARQUITECTURA DE SESIONES (recomendada)

Dentro del Claude Project, organiza las sesiones por función. No mezcles módulos en una misma conversación cuando el contexto sea extenso.

| Sesión | Función | Módulo principal |
|---|---|---|
| `BPA_CORE` | Validación de perfil | TOS_1_BPA |
| `OME_PIPELINE` | Evaluación de oportunidades | TOS_2_OME |
| `CPE_FACTORY` | Posicionamiento + ensamblaje de CV | TOS_3_CPE |
| `IPE_PREP` | Preparación de entrevistas | TOS_4_IPE |
| `GOVERNANCE` | Cambios arquitectónicos, versionado | TOS_MASTER + CHANGELOG |

**Regla:** cada sesión comienza con la plantilla universal (§5) para sincronizar el contexto activo.

---

## 7. FLUJO MÍNIMO VIABLE

Si necesitas operar con el mínimo de fricción:

1. **BPA una vez** — construir y congelar la verdad del perfil.
2. **OME por cada oportunidad** — GO o descarte. Sin GO no hay esfuerzo.
3. **CPE solo para GO** — narrativa + CV ADAPTADO.
4. **IPE solo si hay entrevista confirmada** — preparación específica por ronda.

Cuatro pasos. Secuencia fija. Sin saltar.

---

## 8. REGLAS OPERATIVAS

- El sistema no inventa datos. Si un dato no existe en CAPA DATO → BLOQUEO.
- El CV ADAPTADO (Tier 2) es efímero. No se archiva, no se cita como verdad.
- Los CV Ancla (Tier 1) no se editan a mano. Solo se regeneran vía CPE.
- BPA no se re-ejecuta en cada oportunidad. Se ejecuta una vez y se reutiliza.
- OME = NO GO cierra la oportunidad. No hay vuelta a CPE sin nueva decisión OME.
- Todo cambio estructural al sistema se registra en CHANGELOG.

---

## 9. PRINCIPIO FINAL

```
Disciplina > Complejidad
```

El sistema convierte si:
- respetas la secuencia del pipeline,
- mantienes la verdad sin inflar,
- no saltas la evaluación por presión emocional.

---

TOS_SIMPLE · DOC_OPERACION · v2.0 · SIMPLE_4.0
