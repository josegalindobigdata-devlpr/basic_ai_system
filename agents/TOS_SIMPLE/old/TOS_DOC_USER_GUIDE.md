# 📖 TALENT OPERATING SYSTEM (TOS) — USER GUIDE & OPERATIONAL PROTOCOL
**System:** TOS_SIMPLE (Architecture: Markdown-First / Prompt-Orchestrated)  
**Version:** SIMPLE_1.0  
**Domain:** Career Optimization, Opportunity Evaluation, Positioning & Interview Conversion  

---

## 1. PRINCIPIO OPERATIVO DE CONCORDANCIA
El sistema `TOS_SIMPLE` se rige por una jerarquía estricta e irreversible:
$$\text{TRUTH (BPA)} \longrightarrow \text{EVALUATION (OME)} \longrightarrow \text{POSITIONING (CPE)} \longrightarrow \text{EXECUTION (IPE)}$$

Ninguna acción posterior puede violar una verdad o restricción establecida en los módulos previos. Tú eres el administrador del estado; para evitar la degradación del contexto (*prompt drift*), debes mantener sincronizada la memoria activa utilizando esta guía.

---

## 2. FLUJO DE ESTADOS DEL SISTEMA
El sistema pasa por 7 estados secuenciales obligatorios definidos en `TOS_MASTER`:

* **STATE 1:** `PROFILE_INITIALIZED` (Verdad profesional validada y asentada).
* **STATE 2:** `OPPORTUNITY_RECEIVED` (Nueva vacante detectada, lista para filtrar).
* **STATE 3:** `EVALUATION_COMPLETED` (Puntuación OME y decisión GO/NO-GO calculada).
* **STATE 4:** `POSITIONING_READY` (Narrativa adaptada a la vacante sin distorsionar la verdad).
* **STATE 5:** `INTERVIEW_PREPARED` (Simulaciones y estrategias de respuesta fijadas).
* **STATE 6:** `OFFER_CONVERTED` (Oferta recibida y bajo análisis estratégico).
* **STATE 7:** `CONTRACT_SIGNED` (Cierre de proceso y actualización final).

---

## 3. CATÁLOGO DE COMANDOS EXACTOS

Activa las capacidades indexadas en la sección de *Knowledge* de la Gema invocando estos comandos específicos:

| Comando | Módulo Principal | Estado Requerido | Acción Operativa |
| :--- | :--- | :--- | :--- |
| `/bpa-iniciar` | `TOS_1_BPA.md` | Ninguno (Arranque) | Inicializa el perfil, valida hitos reales y detecta vulnerabilidades cronológicas. |
| `/evaluar` | `TOS_2_OME.md` | `STATE 1` o `2` | Ejecuta la matriz de evaluación y genera la puntuación de encaje (Score 0-100). |
| `/posicionar` | `TOS_3_CPE.md` | `STATE 3` (Requiere GO) | Genera la propuesta de valor adaptada y el framework narrativo (CV/LinkedIn/Pitch). |
| `/entrevista` | `TOS_4_IPE.md` | `STATE 4` | Configura la estrategia de respuesta (STAR), mapa de objeciones y contra-preguntas. |
| `/simular` | `TOS_4_IPE.md` | `STATE 5` | Activa el simulador de presión extrema (3 preguntas hostiles/incómodas del rol). |
| `/actualizar-contexto` | `TOS_SHARED_CONTEXT` | Cualquiera | Fuerza a la Gema a consolidar el estado actual en un nuevo snapshot de memoria. |

---

## 4. CABECERA UNIVERSAL REQUERIDA (MANDATORY HEADER)
Para evitar que Gemini olvide las restricciones globales con el paso del tiempo en chats largos, **todo comando operativo** que envíes a mitad del proceso debe comenzar con esta estructura de datos:

```markdown
[TOS_HEADER]
- OPPORTUNITY_ID: [Inserte ID ej: OME_001_AMAZON]
- CURRENT_STATE: [Inserte Estado actual ej: STATE 3]
- ACTIVE_MODULE: [Inserte Módulo activo ej: TOS_3_CPE]
- STRATEGIC_OBJECTIVE: [Tu meta profesional principal y límite salarial]
- ACTIVE_BLOCKERS: [Cualquier riesgo o limitación activa actual]
```
---

## 5. PROTOCOLO DE ACTUACIÓN PASO A PASO (EJEMPLOS DE USO)
** PASO 1: Inicialización del Sistema (Creación del Núcleo de Verdad)
Cuando abras un chat limpio con la Gema por primera vez, define tu base científica.

Prompt de entrada del usuario:

```markdown
/bpa-iniciar

[INPUT DATA]
A continuación te proporciono mi historial profesional real, datos duros y objetivos de mercado:
- CV / LinkedIn: [Pega aquí tu trayectoria detallada, fechas y logros cuantitativos]
- Expectativa Económica: [Ej: Base 95k + Variable 20k]
- Rol Objetivo: Director de Operaciones IT / Engineering Manager
- Certificaciones Reales: [Ej: PMP, AWS Cloud Practitioner]
```

Salida esperada de la Gema: Procesará los datos bajo las reglas de TOS_1_BPA.md. Devolverá la lista de hitos validados (Level A/B/C), los vacíos identificados que requieren defensa y el primer snapshot completo de TOS_SHARED_CONTEXT listo para usar.

** PASO 2: Evaluación Estratégica de Vacantes
Has encontrado una oferta o un reclutador te ha contactado. No avances sin medir el encaje matemático.

Prompt de entrada del usuario:

```markdown
/evaluar

[TOS_HEADER]
- OPPORTUNITY_ID: OME_2026_001
- CURRENT_STATE: STATE 2 (OPPORTUNITY_RECEIVED)
- ACTIVE_MODULE: TOS_2_OME
- STRATEGIC_OBJECTIVE: Rol de Director IT con enfoque internacional / Compensación > 100k Comp Total.
- ACTIVE_BLOCKERS: Sin experiencia directa gestionando equipos en remoto en LATAM.

[INPUT DATA]
Empresa: TechGlobal Corp
Puesto: Senior Engineering Manager
Job Description (JD): [Pegar aquí la descripción del puesto del portal de empleo]
Datos financieros/Scope: Reporta a VP de Europa. Salario estimado en banda: 105k base.
```

Salida esperada de la Gema: Ejecutará la lógica de TOS_2_OME.md. Calculará la matriz de encaje, restará penalizaciones si hay contradicciones estructurales y emitirá un veredicto explícito: GO, CONDITIONAL o NO-GO, junto al desglose de riesgos percibidos.

** PASO 3: Adaptación de la Narrativa (Posicionamiento)
Si el paso previo arrojó un veredicto GO, es hora de preparar tus cartas de presentación sin adulterar tu historia.

Prompt de entrada del usuario:

```markdown
/posicionar

[TOS_HEADER]
- OPPORTUNITY_ID: OME_2026_001
- CURRENT_STATE: STATE 3 (EVALUATION_COMPLETED)
- ACTIVE_MODULE: TOS_3_CPE
- STRATEGIC_OBJECTIVE: Senior Engineering Manager en TechGlobal Corp.
- ACTIVE_BLOCKERS: Gap detectado en gestión remota LATAM.

[ACTION REQ]
Genera el Pitch Ejecutivo de impacto para el reclutador y los ajustes de palabras clave para optimizar la conversión frente a sus ATS basándote en la evaluación previa.
```

Salida esperada de la Gema: Consultará TOS_3_CPE.md y traducirá tus fortalezas confirmadas del BPA a las necesidades de la oferta. Devolverá el Pitch de contacto, la reestructuración narrativa para destacar tu experiencia aplicable y el plan de mitigación para el gap identificado.

** PASO 4: Preparación y Ejecución de Entrevistas
Te han citado para la primera ronda con el Hiring Manager. Tienes que blindar la ejecución.

Prompt de entrada del usuario:

``` markdown
/entrevista

[TOS_HEADER]
- OPPORTUNITY_ID: OME_2026_001
- CURRENT_STATE: STATE 4 (POSITIONING_READY)
- ACTIVE_MODULE: TOS_4_IPE
- STRATEGIC_OBJECTIVE: Convencer al VP en la ronda técnica/estratégica.
- ACTIVE_BLOCKERS: Justificar adecuadamente el cambio de empresa tras solo 12 meses en el rol actual.

[INPUT DATA]
Tipo de Entrevista: Panel Técnico y de Liderazgo Estructural.
Perfil del Entrevistador: VP de Engineering (Perfil muy analítico, enfocado en métricas de eficiencia DORA).
```

Salida esperada de la Gema: Desplegará los vectores de TOS_4_IPE.md. Construirá tus historias de éxito en formato STAR adaptadas a métricas DORA, listará las 5 objeciones más probables que ese perfil te hará y detallará las contra-preguntas de alto nivel que debes lanzar al cierre de la sesión.

** PASO 5: Simulación de Alta Presión (Entrenamiento antes de salir al campo)
Estás a pocas horas de la entrevista real y necesitas calibrar reflejos bajo estrés cognitivo.

Prompt de entrada del usuario:

``` markdown
/simular

[TOS_HEADER]
- OPPORTUNITY_ID: OME_2026_001
- CURRENT_STATE: STATE 5 (INTERVIEW_PREPARED)
- ACTIVE_MODULE: TOS_4_IPE
- STRATEGIC_OBJECTIVE: Superar objeciones críticas del VP de Engineering.

[ACTION REQ]
Activa el apartado 11A (Pressure Simulation). Dispara una a una las 3 preguntas más hostiles e incómodas que este entrevistador podría hacerme basadas en mis debilidades. Espera mi respuesta a cada una para evaluarla de forma estricta.
```

Salida esperada de la Gema: Adoptará un rol inquisitivo y lanzará la primera pregunta compleja (ej: "Veo que solo duraste un año en tu último puesto, ¿cómo sé que no abandonarás nuestro proyecto a mitad de la migración crítica?"). Esperará tu entrada en texto para auditar la alineación con tu verdad profesional.

** 6. PROTOCOLO DE PERSISTENCIA Y SINCRONIZACIÓN MANUAL
Dado que el sistema opera de forma estrictamente determinista y local dentro de la interfaz de la Gema (Markdown-First sin bases de datos automáticas que hereden cambios estructurales entre sesiones limpias), el usuario debe garantizar la continuidad histórica aplicando estas tres reglas:

*** 1. Extracción de Snapshot: 
Al concluir una iteración importante (por ejemplo, tras pasar a la fase final de oferta), ejecuta el comando /actualizar-contexto.

*** 2. Copiar el Bloque: 
Copia el output formateado de TOS_SHARED_CONTEXT que la Gema imprimirá en pantalla.

*** 3. Inyección en Nuevos Chats: 
Si el chat actual se satura (Gemini empieza a ralentizarse o ignora reglas por exceso de tokens), abre una ventana de conversación nueva con la Gema, pega tu cabecera universal acompañada de ese snapshot de TOS_SHARED_CONTEXT y continúa operando al 100% de eficiencia.

*** 4. Uso de CHANGELOG: 
Si alteras conscientemente una variable macro (ej: elevas tu suelo salarial mínimo un 15% debido a una contraoferta), ordénale a la IA: "Registra esta recalibración estructural como un cambio Tipo B en el CHANGELOG" para mantener la trazabilidad de la arquitectura de tu carrera.
---