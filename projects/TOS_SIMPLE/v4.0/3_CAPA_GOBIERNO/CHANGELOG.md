# TALENT OPERATING SYSTEM (TOS) — CHANGELOG
<!-- TOS_SIMPLE v4.0 — Arquitectura de 4 capas (+ CAPA ENTREGABLE). Sustituye a v3.x. -->

MODULE: CHANGELOG
VERSION: SIMPLE_4.0
TYPE: GOVERNANCE
SYSTEM VERSION: SIMPLE_4.0 (4-LAYER ARCHITECTURE)
CHANGE CONTROL TYPE: MANUAL GOVERNANCE
PRIMARY FUNCTION: VERSION HISTORY, STRUCTURAL TRACEABILITY & EVOLUTION CONTROL
ARCHITECTURE: TOS_SIMPLE

# 1. SYSTEM PURPOSE

CHANGELOG is the canonical historical control module for TOS.

Its purpose is to:

- track all system changes,
- preserve architectural evolution,
- maintain version integrity,
- document structural decisions,
- control module revisions,
- provide rollback visibility,
- and prevent governance drift.

CHANGELOG is the historical memory of TOS architecture.

Without CHANGELOG:
System coherence degrades over time.

# 2. CORE OPERATING PRINCIPLE

DOCUMENT EVERY MATERIAL CHANGE

If a meaningful architectural, strategic, governance, or module update occurs:
IT MUST BE LOGGED


# 3. GOVERNANCE AUTHORITY

CHANGELOG operates under:

TOS_MASTER

CHANGELOG does not override modules.

Its role is:
Traceability  
Version control  
Historical accountability  


# 4. CHANGE CLASSIFICATION TYPES

## TYPE A — MAJOR VERSION
Structural redesign  
Module addition/removal  
Governance redesign  
State machine redesign  
Architecture simplification  


## TYPE B — MINOR VERSION
Module enhancement  
Prompt logic improvement  
Schema expansion  
New operational rules  
Execution optimization  


## TYPE C — PATCH VERSION
Bug fix  
Naming correction  
Formatting correction  
Logic clarification  
Prompt consistency repair  


# 5. VERSION FORMAT

MAJOR.MINOR.PATCH

Example:

1.0.0 → Initial production  
1.1.0 → Added new scoring framework  
1.1.1 → Fixed state typo  


# 6. REQUIRED CHANGE ENTRY SCHEMA

## VERSION:
## DATE:
## AUTHOR:
## CHANGE TYPE:
## AFFECTED MODULE(S):
## SUMMARY:
## REASON:
## OPERATIONAL IMPACT:
## BACKWARD COMPATIBILITY:
## REQUIRED USER ACTION:
## RISKS:
## ROLLBACK PATH:

## VERSION: 1.2.0
## DATE: 2026-06-10
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: MINOR
## AFFECTED MODULE(S): TOS_3_CPE, TOS_SHARED_CONTEXT
## SUMMARY: Creación del framework para el Anexo Modular de Proyectos por Dominios Estratégicos.
## REASON: Romper la ventana de 3 meses de inactividad en entrevistas mediante el aumento drástico del ratio señal/ruido en el CV Extenso solicitado por reclutadores.
## OPERATIONAL IMPACT: Evita la redundancia en documentos de +2 páginas. Permite al usuario intercambiar los bloques de proyectos adjuntos (SDM, GOV, DLV) según la naturaleza exacta de la oportunidad validada en TOS_2_OME.

---

## VERSION: 2.0.0
## DATE: 2026-06-17
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: MAJOR
## AFFECTED MODULE(S): INSTRUCCIONES_PERSONALIZADAS (proyecto), TOS_MASTER, TOS_1_BPA, TOS_SHARED_CONTEXT, CHANGELOG; integración formal de la CAPA DATO (FACT_SHEETS, MASTER_CV_RAW, TARGET_POSITIONS_PROFILE)
## SUMMARY: Refactor a arquitectura de 3 capas con responsabilidades disjuntas — DATA (SSOT) / METHOD (motores) / GOVERNANCE (control) — y jerarquía de autoridad inequívoca con la Regla de Oro "el DATO manda sobre el MÉTODO".
## REASON: Eliminar el deslizamiento causado por doble fuente de verdad: el BPA se declaraba "single source of truth" pero estaba vacío, mientras los ficheros de datos reales (FACTS/MASTER_CV/TARGET) competían como verdad sin figurar en la jerarquía de gobierno.
## OPERATIONAL IMPACT:
- Los 3 ficheros DATO entran formalmente en la jerarquía de autoridad de TOS_MASTER (§1A, §12, §13, §15).
- El BPA se reconvierte de "capa de verdad" a "método de validación que apunta a la CAPA DATO".
- Las instrucciones de proyecto pasan a orquestar las 3 capas y suspenden el comportamiento generalista en la producción de datos.
- Corrección de naming: FACT_SHEETS.md (antes referenciado como FACT_SHEETS.md).
- TOS_SHARED_CONTEXT desembebido de las instrucciones (eliminada duplicación de ~250 líneas); permanece como fichero de conocimiento.
- Sincronización de versión: SYSTEM VERSION = SIMPLE_3.0 (3-LAYER ARCHITECTURE) estampado en TODOS los módulos de sistema. VERSION de módulo subido a SIMPLE_3.0 en MASTER, BPA, OME, CPE, SHARED_CONTEXT y CHANGELOG. Se preservan los linajes propios: TOS_4_IPE (ANCHORED_OPTIMIZED_1.2) y la CAPA DATO (FACT_SHEETS v3.0, etc.) mantienen su versionado independiente.
## BACKWARD COMPATIBILITY: PARTIAL
## REQUIRED USER ACTION:
1. Reemplazar en el proyecto: INSTRUCCIONES_PERSONALIZADAS.md (v2.0), TOS_MASTER.md (SIMPLE_3.0), CHANGELOG.md.
2. (Recomendado) Reconvertir TOS_1_BPA a validador y alinear la jerarquía de TOS_SHARED_CONTEXT.md.
3. Verificar que FACT_SHEETS.md, MASTER_CV_RAW.md y TARGET_POSITIONS_PROFILE.md están cargados como conocimiento.
## RISKS: Entregables previos generados bajo v1.x pueden contener datos no trazables a la CAPA DATO; revalidar antes de reutilizar.
## ROLLBACK PATH: Versión estable previa 1.2.0 — restaurar INSTRUCCIONES_PERSONALIZADAS v1.0 y TOS_MASTER SIMPLE_1.0; readmitir el SHARED_CONTEXT embebido.

## MODULE COMPATIBILITY MATRIX (2.0.0)

| Module | Compatible | Action Required |
|---|---|---|
| INSTRUCCIONES_PERSONALIZADAS | BREAKING | Sustituir por v2.0 |
| TOS_MASTER | PARTIAL | Sustituir por SIMPLE_3.0 |
| TOS_1_BPA | FULL | Reconvertido a validador (hecho v2.0.1) |
| TOS_SHARED_CONTEXT | FULL | Jerarquía alineada y desembebido (hecho v2.0.1) |
| FACT_SHEETS / MASTER_CV_RAW / TARGET_POSITIONS | FULL | Confirmar carga como SSOT |
| TOS_2_OME / TOS_3_CPE / TOS_4_IPE | FULL | Solo re-estampado de versión (sin cambio de lógica) |
| CHANGELOG | FULL | Actualizado en esta entrada |

## VERSION: 2.0.1
## DATE: 2026-06-18
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: PATCH
## AFFECTED MODULE(S): TOS_1_BPA, TOS_SHARED_CONTEXT, TOS_MASTER, INSTRUCCIONES_PERSONALIZADAS
## SUMMARY: Cierre de migración 2.0.0 (BPA validador, SHARED desembebido) y unificación de nomenclatura de campos de contexto.
## REASON: La matriz 2.0.0 marcaba ítems pendientes ya ejecutados; además el campo de decisión OME (LAST_OME_DECISION) y POSITIONING_MODE divergían entre esquema, header y GEMA.
## OPERATIONAL IMPACT: Sin cambio de lógica. Campo canónico unificado a LAST_OME_DECISION y POSITIONING_MODE en todos los ficheros.
## BACKWARD COMPATIBILITY: FULL
## REQUIRED USER ACTION: Ninguna.
## RISKS: Ninguno.
## ROLLBACK PATH: 2.0.0.



# 7. CHANGE GOVERNANCE RULES

RULE 1  
Every major change requires rationale.

RULE 2  
Every structural change must identify affected modules.

RULE 3  
Every state logic change must update TOS_MASTER.

RULE 4  
Breaking changes must declare compatibility risk.

RULE 5  
Deprecated logic must remain visible until replaced.

RULE 6  
No silent governance drift.


# 8. BACKWARD COMPATIBILITY FRAMEWORK

## FULLY COMPATIBLE
No user migration required

## PARTIALLY COMPATIBLE
Manual updates recommended

## BREAKING
Prompt architecture requires revision

# 8A. MODULE COMPATIBILITY MATRIX

Every major or minor change must specify:

| Module | Compatible | Action Required |
|---|---|---|

Compatibility levels:

- FULL
- PARTIAL
- BREAKING

Purpose:
- reduce migration ambiguity
- improve upgrade safety
- prevent governance fragmentation


# 9. ROLLBACK FRAMEWORK

Every major or minor version must include:

PREVIOUS STABLE VERSION  
ROLLBACK CONDITIONS  
ROLLBACK STEPS  


# 10. CHANGE IMPACT CATEGORIES

## ARCHITECTURE
System structure

## GOVERNANCE
Rules / sequencing

## MODULE
Specific prompt module

## SCHEMA
Data structures

## STATE
State machine

## STRATEGIC
Decision frameworks


# 11. REQUIRED OUTPUT FORMAT

## CHANGE SUMMARY
What changed

## WHY IT CHANGED
Strategic or operational rationale

## IMPACT
Affected system areas

## COMPATIBILITY
Safe / caution / breaking

## REQUIRED ACTION
What user must update

## ROLLBACK
How to reverse


# 12. MASTER VERSION REGISTER

## CURRENT PRODUCTION VERSION
3.0.0 — Simplificación mono-usuario · migración en curso (TOS_2_OME entregado)

## LAST STABLE VERSION
2.0.1.

## CURRENT ARCHITECTURE
TOS_SIMPLE

## ACTIVE MODULES

### DATA LAYER (SSOT)
- FACT_SHEETS
- MASTER_CV_RAW
- TARGET_POSITIONS_PROFILE

### METHOD LAYER
- TOS_1_BPA
- TOS_2_OME
- TOS_3_CPE
- TOS_4_IPE

### GOVERNANCE LAYER
- TOS_MASTER
- TOS_SHARED_CONTEXT
- CHANGELOG


# 13. CHANGE ENTRY TEMPLATE


## VERSION:
X.X.X

## DATE:
YYYY-MM-DD

## AUTHOR:
[Name / Owner]

## CHANGE TYPE:
MAJOR / MINOR / PATCH

## AFFECTED MODULE(S):
[List]

## SUMMARY:
[Short description]

## REASON:
[Why change was required]

## OPERATIONAL IMPACT:
[What changes in execution]

## BACKWARD COMPATIBILITY:
FULL / PARTIAL / BREAKING

## REQUIRED USER ACTION:
[Manual steps]

## RISKS:
[Known concerns]

## ROLLBACK PATH:
[Previous stable version + steps]


# 14. INITIAL SYSTEM ENTRY

## VERSION:
1.1.0

## DATE:
YYYY-MM-DD

## AUTHOR:
System Owner

## CHANGE TYPE:
MINOR

## AFFECTED MODULE(S):
- TOS_MASTER
- TOS_1_BPA
- TOS_2_OME
- TOS_3_CPE
- TOS_4_IPE
- CHANGELOG
- TOS_SHARED_CONTEXT

## SUMMARY:
Added TOS_SHARED_CONTEXT operational continuity layer

## REASON:
Reduce context drift and improve interoperability across ChatGPT Projects and Gemini Gems

## OPERATIONAL IMPACT:
Improved shared state continuity
Improved module interoperability
Reduced prompt fragmentation

## BACKWARD COMPATIBILITY:
FULL

## REQUIRED USER ACTION:
Add TOS_SHARED_CONTEXT to all module read orders and input requirements

## RISKS:
Additional manual governance overhead

## ROLLBACK PATH:
Remove TOS_SHARED_CONTEXT references and revert to direct module-only orchestration


# 15. MAINTENANCE CADENCE

Recommended review:

MONTHLY:
Prompt optimization

QUARTERLY:
Strategic recalibration

MAJOR EVENTS:
Career pivots  
Certification  
Compensation shifts  
Architecture redesign


# 16. FAILURE CONDITIONS

CHANGELOG governance failure occurs if:

- Changes undocumented
- Module versions inconsistent
- State machine changed silently
- Rollback impossible
- Compatibility unclear
- Governance drift detected

# 16A. GOVERNANCE DRIFT DETECTION

Potential governance drift indicators:

- inconsistent states
- conflicting positioning
- duplicated profile versions
- incompatible scoring logic
- undocumented prompt changes
- missing handoff structures

If detected:
- pause downstream execution
- validate TOS_MASTER integrity
- reconcile module inconsistencies
- update CHANGELOG before continuation

Purpose:
- preserve architectural coherence
- prevent silent degradation
- maintain strategic consistency

# 17. SIMPLICITY MODEL

This module is markdown-first.

No:
- git integration,
- automated versioning,
- CI/CD,
- external logging,
- system diff tools.

All change governance is manual and user-controlled.

# 18. STRUCTURAL DEPENDENCIES

TOS_2_OME depends on:
- TOS_MASTER
- TOS_1_BPA
- TOS_SHARED_CONTEXT

TOS_3_CPE depends on:
- TOS_MASTER
- TOS_1_BPA
- TOS_2_OME
- TOS_SHARED_CONTEXT


# 19. FINAL EXECUTIVE PRINCIPLE

CHANGELOG protects TOS from silent degradation.

Without version control:
Systems fragment.

Without traceability:
Governance weakens.

Without disciplined updates:
Prompt ecosystems decay.


# OUTPUT DESIGNATION

# WIP — ENTRADA EN PREPARACIÓN (NO CERRADA)
<!-- No forma parte del registro de producción. Promocionar a §6 solo al cerrar v3.0. -->

## MÓDULOS YA RE-ESTAMPADOS A SIMPLE_3.0 (en migración, producción aún 2.0.1):
- TOS_2_OME

## BORRADOR 3.0.0:
## VERSION: 3.0.0
## DATE: 2026-06-18
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: MAJOR
## AFFECTED MODULE(S): TOS_2_OME (entregado). Pendientes en esta migración: TOS_MASTER, INSTRUCCIONES_PERSONALIZADAS (§5, §6), TOS_3_CPE, TOS_4_IPE, TOS_SHARED_CONTEXT, CHANGELOG (re-estampado de versión).
## SUMMARY: Simplificación mayor a perfil único fijo. Reducción de variables de entrada y de la máquina de estados, con foco en lo realmente disponible (TÍTULO + DESCRIPCIÓN). Rediseño del OME a entrada mínima tolerante con Anchor Resolution nativo, complemento cross-anchor y schema de salida fijo (FIT_AJUSTE_PERFIL_ANCLA / SCORE_GLOBAL / FIT-GAP / RISK MATRIX / DECISION / STRATEGY FOR POSITIONING).
## REASON: Las ofertas reales solo aportan título + descripción. Exigir múltiples variables y una máquina de 9 estados generaba bloqueos y ceremonia sin valor en un sistema mono-usuario con perfil y objetivos ya fijos.
## OPERATIONAL IMPACT:
- OME a entrada mínima: solo TÍTULO + DESCRIPCIÓN imprescindibles; el resto opcional y nunca bloqueante. Compensación deja de evaluarse como cifra y deja de ser causa de bloqueo; se reformula como estrategia de filtro salarial.
- OME resuelve el ancla automáticamente (SDM/GOV/DLV/"No aplica") y complementa con experiencia cross-anchor trazable al DATO.
- (Pendiente) TOS_MASTER → pipeline lineal de una sola guardia; perfil como constante fija; fin de la flexibilidad multi-perfil; cabeceras universales opcionales.
- (Pendiente) GEMA §5 (no preguntar rol) y §6 (solo DATO obligatorio + tolerancia de entrada).
## BACKWARD COMPATIBILITY: PARTIAL
## REQUIRED USER ACTION:
1. Reemplazar TOS_2_OME.md por SIMPLE_3.0.
2. (Siguiente) Reemplazar TOS_MASTER.md por la versión lean SIMPLE_3.0 y editar INSTRUCCIONES_PERSONALIZADAS §5 y §6.
3. (Siguiente) Alinear TOS_3_CPE / TOS_4_IPE / TOS_SHARED_CONTEXT al nuevo handoff y re-estampar SYSTEM VERSION = SIMPLE_3.0.
## RISKS: Durante la migración conviven módulos SIMPLE_2.0.1 y SIMPLE_3.0. Evaluar oportunidades con OME 3.0 ya es seguro (no depende de estado); no avanzar a CPE/IPE hasta alinearlos.
## ROLLBACK PATH: 2.0.1 — restaurar TOS_2_OME SIMPLE_2.0 y mantener TOS_MASTER 2.0.

## MODULE COMPATIBILITY MATRIX (3.0.0)

| Module | Compatible | Action Required |
|---|---|---|
| TOS_2_OME | PARTIAL | Sustituir por SIMPLE_3.0 (hecho) |
| TOS_MASTER | PARTIAL | Sustituir por lean SIMPLE_3.0 (pendiente) |
| INSTRUCCIONES_PERSONALIZADAS | PARTIAL | Editar §5 y §6 (pendiente) |
| TOS_3_CPE | PARTIAL | Alinear a handoff OME 3.0 (pendiente) |
| TOS_4_IPE | FULL | Re-estampado de versión (pendiente) |
| TOS_SHARED_CONTEXT | PARTIAL | Aligerar campos; cabecera opcional (pendiente) |
| CHANGELOG | FULL | Actualizado en esta entrada |
| FACT_SHEETS / MASTER_CV_RAW / TARGET_POSITIONS | FULL | Sin cambios |


---

## VERSION: 3.1.1
## DATE: 2026-06-19
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: PATCH
## AFFECTED MODULE(S): PORTFOLIO_CAPABILITIES, FACT_SHEETS, MASTER_CV_RAW, TOS_MASTER
## SUMMARY: Corrección de encuadres (framing) entre CAPA DATO y la proyección PORTFOLIO; sin alterar ninguna cifra canónica.
## REASON: Auditoría de coherencia tras incorporar PORTFOLIO a la CAPA DATO. Elimina lecturas ambiguas que se filtraban al entregable (CV/entrevista) y restaura la trazabilidad FACTS→MASTER del alcance de servicios (130K).
## OPERATIONAL IMPACT: DLV-08 deja de evocar "product management" (keyword L240); FACTS §6 desambigua "mayor programa" (RDA-BI pasa a "programa regulatorio insignia", L110); el alcance 130K queda fijado como horas/año de cuenta insignia en FACTS (L45/106/107) y en MASTER Bloque general (L831/832); PORTFOLIO §6 sustituye el rótulo "unión" por "presentación" para Ibermática (L277/281/283) y depura la nota de cierre (L289); TOS_MASTER §2 actualiza su rótulo (L18).
## BACKWARD COMPATIBILITY: FULL — solo redacción y precisión de alcance; ninguna cifra cambia.
## REQUIRED USER ACTION: Descargar y re-subir los ficheros editados en este lote (PORTFOLIO_CAPABILITIES, MASTER_CV_RAW) y este CHANGELOG. FACT_SHEETS y TOS_MASTER ya quedaron corregidos en el lote anterior.
## RISKS: Ninguno; cambios deterministas y locales.
## ROLLBACK PATH: Revertir las líneas indicadas a su estado v3.1.

---

## VERSION: 3.1.2
## DATE: 2026-06-19
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: PATCH
## AFFECTED MODULE(S): INSTRUCCIONES_PERSONALIZADAS, TOS_1_BPA, TOS_2_OME, TOS_MASTER, TARGET_POSITIONS_PROFILE, PORTFOLIO_CAPABILITIES, TOS_SHARED_CONTEXT
## SUMMARY: Reversión de naming de la CAPA DATO — corrección de FACTS_SHEET.md a FACT_SHEETS.md en 7 ficheros activos para alinear con el nombre físico real del archivo en el proyecto.
## REASON: La entrada v2.0.0 (ver línea 127 de este CHANGELOG) documentó una "corrección de naming" hacia FACTS_SHEET.md que en realidad invirtió el nombre respecto al archivo físico cargado en el proyecto, que siempre fue FACT_SHEETS.md. La discrepancia permaneció latente hasta ser detectada durante la auditoría de formato de salida de TOS_4_IPE, el único módulo que citaba el nombre correcto.
## OPERATIONAL IMPACT:
- Las 7 referencias activas a FACTS_SHEET.md se corrigen a FACT_SHEETS.md.
- TOS_4_IPE.md ya citaba el nombre correcto (FACT_SHEETS.md) y no requiere cambios en esta entrada.
- La entrada v2.0.0 (línea 127) NO se edita retroactivamente: permanece como registro histórico fiel de lo decidido en su momento. Esta entrada documenta la reversión, no sustituye el historial.
## BACKWARD COMPATIBILITY: FULL (cambio puramente referencial; ninguna cifra ni dato canónico se altera)
## REQUIRED USER ACTION:
1. Descargar y re-subir al proyecto: INSTRUCCIONES_PERSONALIZADAS.md, TOS_1_BPA.md, TOS_2_OME.md, TOS_MASTER.md, TARGET_POSITIONS_PROFILE.md, PORTFOLIO_CAPABILITIES.md, TOS_SHARED_CONTEXT.md.
2. Verificar que el archivo físico en project knowledge sigue llamándose FACT_SHEETS.md (sin renombrar).
## RISKS: Ninguno — corrección referencial sin impacto en datos canónicos.
## ROLLBACK PATH: Restaurar el naming FACTS_SHEET.md en los 7 ficheros si en el futuro se decide renombrar el archivo físico en su lugar.

## MODULE COMPATIBILITY MATRIX (3.1.2)

| Module | Compatible | Action Required |
|---|---|---|
| INSTRUCCIONES_PERSONALIZADAS | PARTIAL | Corregir naming FACT_SHEETS.md |
| TOS_1_BPA | PARTIAL | Corregir naming FACT_SHEETS.md  |
| TOS_2_OME | PARTIAL | Corregir naming FACT_SHEETS.md  |
| TOS_MASTER | PARTIAL | Corregir naming FACT_SHEETS.md  |
| TARGET_POSITIONS_PROFILE | PARTIAL | Corregir naming FACT_SHEETS.md  |
| PORTFOLIO_CAPABILITIES | PARTIAL | Corregir naming FACT_SHEETS.md  |
| TOS_SHARED_CONTEXT | PARTIAL | Corregir naming FACT_SHEETS.md  |
| TOS_3_CPE | FULL | Sin cambios |
| TOS_4_IPE | FULL | Ya citaba el nombre correcto |
| CHANGELOG | FULL | Actualizado en esta entrada |

---

## VERSION: 3.2.0
## DATE: 2026-06-19
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: MAJOR
## AFFECTED MODULE(S): TOS_SHARED_CONTEXT
## SUMMARY: Reescritura lean de TOS_SHARED_CONTEXT (441→139 líneas), alineada al pipeline lineal de TOS_MASTER SIMPLE_3.0.
## REASON: El fichero declaraba versión v3.0 en cabecera pero su cuerpo seguía operando bajo la arquitectura v2.0 (máquina de 9 estados, handoff-contract ceremonial, drift detection y recovery framework automáticos) — derogada explícitamente por TOS_MASTER §4.
## OPERATIONAL IMPACT:
- Eliminado: motor de detección de drift automático, framework de recuperación de 6 pasos, handoff package ceremonial (§10 v3.0), modos operativos huérfanos (MODE A–D), campos de cabecera ligados a la FSM eliminada (NEXT_ALLOWED_STATE, CURRENT_PHASE).
- Conservado y saneado: jerarquía de autoridad de 4 capas, schema de contexto activo (recortado a 9 campos realmente consumidos por BPA/OME/CPE/IPE), formato de salida con Regla de Oro + directiva de inhibición de preámbulo (mismo patrón aplicado a BPA/OME/CPE/IPE).
- Condiciones de bloqueo recortadas a las que TOS_MASTER §6 autoriza; SHARED_CONTEXT deja de declarar bloqueos propios.
## BACKWARD COMPATIBILITY: PARTIAL
## REQUIRED USER ACTION: Ninguna adicional — ya aplicado y verificado en sesión.
## RISKS: Ninguno detectado; verificación cruzada confirmó cero referencias rotas a campos/secciones eliminados en el resto del sistema.
## ROLLBACK PATH: Versión previa SIMPLE_3.0 (441 líneas, arquitectura v2.0 embebida).
---
## ROLLBACK PATH: Versión previa SIMPLE_3.0 (441 líneas, arquitectura v2.0 embebida).

---

## VERSION: 3.3.0
## DATE: 2026-06-19
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: MAJOR
## AFFECTED MODULE(S): INSTRUCCIONES_PERSONALIZADAS, TARGET_POSITIONS_PROFILE
## SUMMARY: Sustitución de §0 (PRECEDENCIA SOBRE PREFERENCIAS GLOBALES) por §0 (INHIBICIÓN DE PREFERENCIAS GLOBALES — MODO TOS): de precedencia declarativa parcial a inhibición íntegra y binaria de las preferencias globales de usuario mientras el proyecto TOS_SIMPLE está activo.
## REASON: La §0 anterior declaraba que las instrucciones de proyecto "tienen prioridad absoluta" pero solo suspendía comportamiento generalista en "producción de datos", dejando sin definir la frontera entre modo TOS y "conversación de apoyo". Esa zona gris permitía que el protocolo de optimización de prompts, los perfiles expertos por dominio y los criterios de formato de las preferencias globales compitieran sin resolución determinista con el contrato anti-deslizamiento y los formatos canónicos de los motores TOS.
## OPERATIONAL IMPACT:
- Activación binaria: operar dentro del proyecto TOS_SIMPLE activa el modo TOS para toda la sesión, sin estados intermedios.
- Inhibición íntegra de `<userPreferences>`: protocolo de optimización de prompts, perfiles expertos genéricos (GOV/SDM/DLV de propósito general) y formato de respuesta abierto quedan suspendidos sin negociación caso a caso.
- Única excepción: el idioma de respuesta (español) persiste por ser atributo de comunicación, no de criterio de producción o comportamiento.
- Desambiguación de naming: los Roles Ancla SDM/GOV/DLV (`TARGET_POSITIONS_PROFILE.md`) se declaran como la única taxonomía válida en este proyecto, distinta de cualquier perfil homónimo de las preferencias globales. Nota de desambiguación añadida en cabecera de `TARGET_POSITIONS_PROFILE.md` referenciando esta sección.
## BACKWARD COMPATIBILITY: PARTIAL
## REQUIRED USER ACTION: Ninguna adicional — ya aplicado y verificado en sesión.
## RISKS: Ninguno detectado.
## ROLLBACK PATH: Restaurar §0 anterior ("PRECEDENCIA SOBRE PREFERENCIAS GLOBALES", suspensión parcial limitada a producción de datos) si se requiere convivencia activa con preferencias globales fuera de la producción de entregables.

## MODULE COMPATIBILITY MATRIX (3.3.0)

| Module | Compatible | Action Required |
|---|---|---|
| TOS_SHARED_CONTEXT | FULL | Reescritura lean aplicada (3.2.0) |
| INSTRUCCIONES_PERSONALIZADAS | FULL | §0 actualizada a inhibición íntegra |
| TARGET_POSITIONS_PROFILE | FULL | Nota de desambiguación añadida |
| TOS_MASTER | FULL | Sin cambios |
| TOS_1_BPA | FULL | Sin cambios |
| TOS_2_OME | FULL | Sin cambios |
| TOS_3_CPE | FULL | Sin cambios |
| TOS_4_IPE | FULL | Sin cambios |
| FACT_SHEETS / MASTER_CV_RAW / PORTFOLIO_CAPABILITIES | FULL | Sin cambios |
| CHANGELOG | FULL | Actualizado en esta entrada |


## VERSION: 4.0.0
## DATE: 2026-06-22
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: MAJOR
## AFFECTED MODULE(S): TODO EL SISTEMA — INSTRUCCIONES_PERSONALIZADAS, TOS_MASTER, TOS_1_BPA, TOS_2_OME, TOS_3_CPE, TOS_4_IPE, TOS_SHARED_CONTEXT, CHANGELOG (eje sistema → v4.0); FACT_SHEETS (eje dato → v3.1); CV_ANCLA_SDM/GOV/DLV_ESP (nuevos ficheros CAPA ENTREGABLE). CAPA DATO (MASTER_CV_RAW, TARGET_POSITIONS_PROFILE, PORTFOLIO_CAPABILITIES) sin cambio de versión de dato.
## SUMMARY: Consolidación a v4.0 — arquitectura de 4 capas. Incorpora la CAPA ENTREGABLE (cuarta capa subordinada) con dos niveles —Tier 1 CV ANCLA BASE (3 CV congelados y versionados) y Tier 2 CV ADAPTADO (salida efímera de CPE)—, el CONTRATO DE ADAPTACIÓN DE CV (allowlist de 5 operaciones + denylist + Test del MATIZ), el CV ASSEMBLY CONTRACT en CPE, y el re-estampado SYSTEM VERSION = SIMPLE_4.0 (4-LAYER ARCHITECTURE) en todos los módulos de sistema.
## REASON: (1) Los 3 CV Ancla, ya elaborados y revisados, no tenían lugar arquitectónico definido; colocarlos en CAPA DATO habría recreado el modo de fallo de v2.0 (fuente de verdad dual). Se necesitaba una capa de salida explícitamente subordinada que reutilice los anclas como base y permita adaptación por oferta basada en piezas (selección + adición desde PORTFOLIO + matiz) sin reescribir la trayectoria ni introducir deslizamiento. (2) El salto de 3 a 4 capas es estructural (MAJOR): se consolida en v4.0 en lugar de un 3.x incremental.
## OPERATIONAL IMPACT:
- TOS_MASTER §2: añadida CAPA ENTREGABLE a la jerarquía (DATO > TOS_MASTER > MÉTODO > SHARED_CONTEXT > ENTREGABLE) y REGLA DE ENTREGABLE (un ancla que contradice al MASTER se regenera; MASTER nuevo → ancla STALE).
- INSTRUCCIONES_PERSONALIZADAS: título y §1 a 4 capas; CAPA ENTREGABLE descrita (Tier 1 / Tier 2); §2 jerarquía + regla de resolución ancla↔MASTER; nueva §4A CONTRATO DE ADAPTACIÓN DE CV; §0/§10/footer actualizados.
- TOS_3_CPE: nueva §7A CV ASSEMBLY CONTRACT (input/assembly strategy/output CV adaptado vs ampliado); aclaración de alcance respecto a §12 (el documento CV es artefacto de CAPA ENTREGABLE, distinto del esquema de análisis de §12); §3 jerarquía local extendida.
- FACT_SHEETS §2: DECISIÓN DOCUMENTADA — el titular de cabecera de los CV Ancla se cita en inglés también en la versión ES (variante CV — EN) por convención TIC/ATS; la variante CV — ES queda como respaldo. Resuelve la discrepancia "CV_ANCLA_*_ESP con titular EN".
- CV Ancla (x3): formalizados como CAPA ENTREGABLE Tier 1. Tres coordenadas de versión sin conflación: (perfil/dato) Release_base_profile v.3.0, título (v.3.0), BASED_ON: MASTER_CV_RAW v3.0 — intactos; (era de sistema) comment tag TOS_SIMPLE v4.0 — añadido; (generación de entregable) FROZEN_REV: 1.0 — añadido. Cuerpo del CV sin cambios. FROZEN_REV es la coordenada que sube cuando CPE regenera el ancla.
- RE-ESTAMPADO DE VERSIÓN (dos ejes, nunca conflados — ver precedente entrada 2.0.0):
  · Eje SISTEMA/ARQUITECTURA → v4.0: SYSTEM VERSION = SIMPLE_4.0 (4-LAYER ARCHITECTURE) y VERSION = SIMPLE_4.0 en todos los módulos de gobierno y método; comment tag de era TOS_SIMPLE v4.0 en todos los ficheros del proyecto; footers de OME/SHARED_CONTEXT a SIMPLE 4.0; referencias internas "jerarquía/pipeline v3.0" → v4.0.
  · LINAJES PROPIOS PRESERVADOS: TOS_4_IPE mantiene VERSION = ANCHORED_OPTIMIZED_1.2 (solo su SYSTEM VERSION sube a 4.0).
  · Eje DATO/PERFIL → independiente: FACT_SHEETS sube a v3.1 (cambio de contenido en §2); MASTER_CV_RAW, TARGET_POSITIONS_PROFILE y PORTFOLIO_CAPABILITIES permanecen en v3.0 (perfil auditado sin cambios); Release_base_profile = v.3.0 intacto en toda la CAPA DATO; PROFILE: LOCKED · v3.0 intacto en TOS_MASTER. Los CV Ancla permanecen en Release_base_profile v.3.0 (cuerpo sin cambios).
## BACKWARD COMPATIBILITY: FULL (adición de capa subordinada + re-estampado de metadatos; no altera la lógica de las tres capas existentes ni el pipeline lineal).
## REQUIRED USER ACTION:
1. Reemplazar en el proyecto los 12 ficheros del sistema/dato re-estampados.
2. Cargar los 3 CV Ancla (con cabecera BASED_ON) como ficheros de la CAPA ENTREGABLE.
3. CERRADO (gate de auditoría — verificado 2026-06-22): KPIs DLV auditados contra MASTER_CV_RAW — Mapfre CFR −65% (8,6→3) ✓, productividad +20% ✓; Sabadell incidencias −80% (5→<1) ✓, rendimiento +14% ✓. CV_ANCLA_DLV_ESP opera como base congelada válida.
## RISKS: Si un ancla se edita a mano en lugar de regenerarse vía CPE, puede desincronizarse del MASTER sin que la marca STALE lo detecte (la marca solo cubre cambios de versión del MASTER). Mitigación: regla "no editar a mano" en cabecera de cada ancla.
## ROLLBACK PATH: 3.3.0 — revertir re-estampado a SIMPLE_3.0/3-LAYER; eliminar CAPA ENTREGABLE de TOS_MASTER §2 e INSTRUCCIONES §1/§2; retirar §4A y §7A (CPE); revertir nota §2 de FACT_SHEETS a v3.0; retirar cabeceras BASED_ON. Los 3 CV Ancla quedarían como ficheros sueltos sin lugar arquitectónico (estado previo).

## MODULE COMPATIBILITY MATRIX (4.0.0)

| Module | Compatible | Eje | Action Required |
|---|---|---|---|
| INSTRUCCIONES_PERSONALIZADAS | FULL | sistema → v4.0 | 4 capas + §4A Contrato de Adaptación |
| TOS_MASTER | FULL | sistema → v4.0 | §2 ampliada con CAPA ENTREGABLE (PROFILE LOCKED v3.0 intacto) |
| TOS_1_BPA / TOS_2_OME | FULL | sistema → v4.0 | Solo re-estampado SYSTEM/VERSION |
| TOS_3_CPE | FULL | sistema → v4.0 | §7A CV Assembly Contract añadida |
| TOS_4_IPE | FULL | sistema → v4.0 | SYSTEM VERSION → 4.0; VERSION ANCHORED_OPTIMIZED_1.2 preservado |
| TOS_SHARED_CONTEXT | FULL | sistema → v4.0 | Re-estampado SIMPLE_4.0 |
| CHANGELOG | FULL | sistema → v4.0 | Esta entrada |
| FACT_SHEETS | FULL | dato → v3.1 | §2 decisión titular EN; doc v3.0→v3.1 |
| MASTER_CV_RAW / TARGET_POSITIONS_PROFILE / PORTFOLIO_CAPABILITIES | FULL | dato → v3.0 | Sin cambio de dato; solo comment tag de era |
| CV_ANCLA_SDM/GOV/DLV_ESP | FULL | entregable · FROZEN_REV 1.0 | Era v4.0 + BASED_ON; perfil v3.0 intacto; gate de auditoría KPIs pendiente |


## VERSION: 4.0.1
## DATE: 2026-06-22
## AUTHOR: Propietario del Sistema / TOS_SIMPLE
## CHANGE TYPE: PATCH (TYPE C)
## AFFECTED MODULE(S): TOS_1_BPA
## SUMMARY: Corrección §1 DATA LAYER BINDING — primer bullet sustituido de
  `MASTER_CV_RAW.md` a `FACT_SHEETS.md`.
## REASON: Error de copia introducido en una iteración anterior: MASTER_CV_RAW
  aparecía duplicado; FACT_SHEETS (autoridad máxima de la CAPA DATO) quedaba
  omitida en la declaración de binding de §1. §3 lo compensaba implícitamente,
  pero la inconsistencia interna era trazable.
## OPERATIONAL IMPACT: Ninguno en producción (§3 ya declaraba la jerarquía
  correcta). Consistencia interna del módulo restaurada.
## BACKWARD COMPATIBILITY: FULL
## REQUIRED USER ACTION: Ninguna.
## RISKS: Ninguno.
## ROLLBACK PATH: Restaurar `MASTER_CV_RAW.md` en línea 21 de §1 (no recomendado).
---


CHANGELOG  
VERSION CONTROL & EVOLUTION GOVERNANCE  
SIMPLE ARCHITECTURE  
PRODUCTION VERSION  
