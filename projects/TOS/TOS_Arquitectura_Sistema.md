# Arquitectura Final Recomendada: Sistema TOS

## 1. Jerarquía del Sistema

### Nivel 0: Orquestación
* **TOS_0_TCC — TOS_CONTROL_CENTER**: Orquestar el uso óptimo de GEM 1–4.

### Nivel 1: Ejecución (GEM 1–4 Visual)
El flujo lógico de ejecución sigue esta secuencia:
`TOS CONTROL` → `BASE PROFILE` → `MATCH ENGINE` → `CV POSITIONING` → `INTERVIEW POSITIONING`

---

## 2. Definición de las 4 Gemas + Orquestador

1.  **TOS_1_BPA — BASE_PROFILE_ARCHITECT** * *Misión:* Construyo la verdad (Perfil base).
2.  **TOS_2_OME — OPPORTUNITY_MATCH_ENGINE** * *Misión:* Decido dónde competir (Filtrado y matching).
3.  **TOS_3_CPE — CV_POSITIONING_ENGINE** * *Misión:* Maximizo competitividad (Adaptación de activos).
4.  **TOS_4_IPE — INTERVIEW_POSITIONING_ENGINE** * *Misión:* Convierto oportunidad (Cierre en entrevista).
5.  **TOS_0_TCC — TOS_CONTROL_CENTER** * *Misión:* Orquestar el uso óptimo de GEM 1-4.

---

## 3. Análisis de Límites Reales (LLM)

Para que el sistema funcione en un entorno de **Gemini** o cualquier LLM estándar, se deben considerar estas realidades técnicas:

* **Sin Memoria Estructural Nativa:** El sistema solo mantiene la estructura si se gestiona dentro del mismo contexto o mediante un orquestador externo.
* **Simulación de Estado:** El modelo no reconoce "módulos" de software; interpreta **contratos de comportamiento secuenciales**.
* **Traducción Técnica:** Los TOS son protocolos de entrada/salida que garantizan la coherencia en un pipeline de texto.

---

## 4. Pilares de Interoperabilidad Real

Para que las 5 gemas operen como un sistema cohesionado, deben cumplir los siguientes requisitos:

### A. Consistencia Semántica de Outputs
Cada gema debe producir campos estructurados y estables. Conceptos como *Seniority*, *Gaps* o *Score* deben ser idénticos en todo el flujo.

### B. Compatibilidad de Handoffs (Crítico)
El flujo de datos debe ser estricto para evitar reinterpretaciones libres:
* **TOS_1** → produce `PROFILE_CORE`
* **TOS_2** → consume `PROFILE_CORE` / produce `MATCH_CORE`
* **TOS_3** → consume `MATCH_CORE` / produce `POSITIONING_CORE`
* **TOS_4** → consume `POSITIONING_CORE`

### C. No Redundancia Funcional
Cada gema tiene una función única.
> **Error común:** Si TOS_2 y TOS_3 repiten el "análisis de riesgos", se rompe la lógica del sistema y se desperdicia contexto.

### D. Secuencialidad Obligatoria
Existe un único camino de éxito:
`TOS_1` → `TOS_2` → `TOS_3` → `TOS_4`

---

## 5. Resumen de Flujo de Datos

| Gema | Identificador | Input Principal | Output Principal |
| :--- | :--- | :--- | :--- |
| **Gema 1** | `TOS_1_BPA` | Datos Raw / Experiencia | `PROFILE_CORE` |
| **Gema 2** | `TOS_2_OME` | `PROFILE_CORE` + Job Desc | `MATCH_CORE` |
| **Gema 3** | `TOS_3_CPE` | `MATCH_CORE` | `POSITIONING_CORE` |
| **Gema 4** | `TOS_4_IPE` | `POSITIONING_CORE` | `CONVERSION` |