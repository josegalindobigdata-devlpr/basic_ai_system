# TALENT OPERATING SYSTEM (TOS) — CHANGELOG
<!-- TOS_SIMPLE v2.0 — Reescritura anti-deslizamiento. Sustituye a v1.0. -->
MODULE: CHANGELOG
VERSION: SIMPLE_2.0
TYPE: GOVERNANCE
SYSTEM VERSION: SIMPLE_2.0 (3-LAYER ARCHITECTURE)
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
## AFFECTED MODULE(S): INSTRUCCIONES_PERSONALIZADAS (proyecto), TOS_MASTER, TOS_1_BPA, TOS_SHARED_CONTEXT, CHANGELOG; integración formal de la CAPA DATO (FACTS_SHEET, MASTER_CV_RAW, TARGET_POSITIONS_PROFILE)
## SUMMARY: Refactor a arquitectura de 3 capas con responsabilidades disjuntas — DATA (SSOT) / METHOD (motores) / GOVERNANCE (control) — y jerarquía de autoridad inequívoca con la Regla de Oro "el DATO manda sobre el MÉTODO".
## REASON: Eliminar el deslizamiento causado por doble fuente de verdad: el BPA se declaraba "single source of truth" pero estaba vacío, mientras los ficheros de datos reales (FACTS/MASTER_CV/TARGET) competían como verdad sin figurar en la jerarquía de gobierno.
## OPERATIONAL IMPACT:
- Los 3 ficheros DATO entran formalmente en la jerarquía de autoridad de TOS_MASTER (§1A, §12, §13, §15).
- El BPA se reconvierte de "capa de verdad" a "método de validación que apunta a la CAPA DATO".
- Las instrucciones de proyecto pasan a orquestar las 3 capas y suspenden el comportamiento generalista en la producción de datos.
- Corrección de naming: FACTS_SHEET.md (antes referenciado como FACTS_SHEETS.md).
- TOS_SHARED_CONTEXT desembebido de las instrucciones (eliminada duplicación de ~250 líneas); permanece como fichero de conocimiento.
- Sincronización de versión: SYSTEM VERSION = SIMPLE_2.0 (3-LAYER ARCHITECTURE) estampado en TODOS los módulos de sistema. VERSION de módulo subido a SIMPLE_2.0 en MASTER, BPA, OME, CPE, SHARED_CONTEXT y CHANGELOG. Se preservan los linajes propios: TOS_4_IPE (ANCHORED_OPTIMIZED_1.2) y la CAPA DATO (FACTS_SHEET v3.0, etc.) mantienen su versionado independiente.
## BACKWARD COMPATIBILITY: PARTIAL
## REQUIRED USER ACTION:
1. Reemplazar en el proyecto: INSTRUCCIONES_PERSONALIZADAS.md (v2.0), TOS_MASTER.md (SIMPLE_2.0), CHANGELOG.md.
2. (Recomendado) Reconvertir TOS_1_BPA a validador y alinear la jerarquía de TOS_SHARED_CONTEXT.md.
3. Verificar que FACTS_SHEET.md, MASTER_CV_RAW.md y TARGET_POSITIONS_PROFILE.md están cargados como conocimiento.
## RISKS: Entregables previos generados bajo v1.x pueden contener datos no trazables a la CAPA DATO; revalidar antes de reutilizar.
## ROLLBACK PATH: Versión estable previa 1.2.0 — restaurar INSTRUCCIONES_PERSONALIZADAS v1.0 y TOS_MASTER SIMPLE_1.0; readmitir el SHARED_CONTEXT embebido.

## MODULE COMPATIBILITY MATRIX (2.0.0)

| Module | Compatible | Action Required |
|---|---|---|
| INSTRUCCIONES_PERSONALIZADAS | BREAKING | Sustituir por v2.0 |
| TOS_MASTER | PARTIAL | Sustituir por SIMPLE_2.0 |
| TOS_1_BPA | FULL | Reconvertido a validador (hecho v2.0.1) |
| TOS_SHARED_CONTEXT | FULL | Jerarquía alineada y desembebido (hecho v2.0.1) |
| FACTS_SHEET / MASTER_CV_RAW / TARGET_POSITIONS | FULL | Confirmar carga como SSOT |
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
2.0.1 — Three-layer architecture (DATA / METHOD / GOVERNANCE) · migración 2.0.0 cerrada

## LAST STABLE VERSION
2.0.0.

## CURRENT ARCHITECTURE
TOS_SIMPLE

## ACTIVE MODULES

### DATA LAYER (SSOT)
- FACTS_SHEET
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

CHANGELOG  
VERSION CONTROL & EVOLUTION GOVERNANCE  
SIMPLE ARCHITECTURE  
PRODUCTION VERSION  
