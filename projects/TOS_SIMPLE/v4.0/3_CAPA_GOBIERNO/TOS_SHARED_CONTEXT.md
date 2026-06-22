# TOS_SHARED_CONTEXT — CONTINUITY LAYER (LEAN)
<!-- TOS_SIMPLE v4.0 — Arquitectura de 4 capas (+ CAPA ENTREGABLE). Sustituye a v3.x. -->

MODULE: TOS_SHARED_CONTEXT
VERSION: SIMPLE_4.0
TYPE: GOVERNANCE

---

## 1. PROPÓSITO

Capa de continuidad **mínima** para un único titular con perfil fijo y pipeline lineal.
Mantiene el snapshot de contexto activo (perfil, oportunidad, riesgos) entre módulos y
entre sesiones. No valida, no decide, no reconcilia automáticamente — solo conserva.

No sustituye a:
- CAPA DATO (`FACT_SHEETS` / `MASTER_CV_RAW` / `TARGET_POSITIONS_PROFILE`)
- `TOS_MASTER` (estado y secuencia)
- BPA / OME / CPE / IPE (validación y ejecución)

---

## 2. GOVERNANCE AUTHORITY

Jerarquía (mayor → menor), heredada de `INSTRUCCIONES_PERSONALIZADAS` §2:

1. **CAPA DATO** — `FACT_SHEETS > MASTER_CV_RAW > TARGET_POSITIONS_PROFILE > PORTFOLIO_CAPABILITIES` (SSOT)
2. **TOS_MASTER** — estado y secuencia del pipeline
3. **CAPA MÉTODO** — `BPA > OME > CPE > IPE`
4. **TOS_SHARED_CONTEXT** — continuidad (este fichero)
5. **CAPA ENTREGABLE** — CV ANCLA BASE (Tier 1, congelados) + CV ADAPTADO (Tier 2, efímero); sin autoridad sobre las capas superiores.

**REGLA DE ORO:** el DATO manda sobre el MÉTODO. Si SHARED_CONTEXT contradice un
dato validado o una decisión de módulo, **pierde SHARED_CONTEXT**.

---

## 3. REGLAS DE EJECUCIÓN

1. Solo outputs **validados** de un módulo (BPA/OME/CPE/IPE) pueden poblar el contexto.
2. SHARED_CONTEXT nunca sobreescribe CAPA DATO ni CAPA MÉTODO.
3. Tras cada ejecución de módulo con decisión (`GO`/`NO GO`/`READY`/etc.), refrescar
   los campos afectados del schema (§4).

---

## 4. SCHEMA DE CONTEXTO ACTIVO

Campos consumidos directamente por BPA/OME/CPE/IPE. Si falta alguno crítico, sube el
riesgo de ejecución (no bloquea por sí solo — ver `TOS_MASTER` §6 para condiciones
de bloqueo reales).

### IDENTIDAD Y PERFIL
- `PROFILE_VERSION` (debe coincidir con la última validación BPA)
- `TARGET_ROLE` / `TARGET_LEVEL`

### ESTADO ACTIVO
- `CURRENT_STATE` (fase del pipeline: EVALUATE / POSITION / INTERVIEW / CLOSE)
- `ACTIVE_MODULE`
- `CURRENT_OBJECTIVE`

### OPORTUNIDAD ACTIVA
- `ACTIVE_OPPORTUNITY` (título + empresa si hay)
- `LAST_OME_DECISION` (GO / GO WITH ADJUSTMENT / NO GO)
- `POSITIONING_MODE` (heredado de CPE si ya se ejecutó)
- `INTERVIEW_STAGE` (si aplica)

### RIESGOS
- `ACTIVE_RISKS` (lista corta, heredada del RISK MATRIX de OME o del OBJECTION MAP de CPE)

---

## 5. TRIGGERS DE REFRESCO

Refrescar el schema (§4) cuando:
- Cambia la decisión de OME (GO / NO GO / GO WITH ADJUSTMENT)
- Cambia el modo de posicionamiento (CPE)
- Cambia la etapa de entrevista (IPE)
- BPA se recalibra (cambio real de CV)
- Los riesgos activos cambian materialmente

---

## 6. FORMATO DE SALIDA CANÓNICO (si se solicita snapshot de contexto)

```
## ACTIVE CONTEXT SUMMARY
[snapshot operativo: estado + rol ancla + oportunidad]

## ACTIVE RISKS
[riesgos más críticos vigentes]

## NEXT REQUIRED ACTION
[paso obligatorio siguiente en el pipeline]

## VALIDATION STATUS
APROBADO / CONDICIONAL / BLOQUEADO
```

## REGLA DE ORO DE SALIDA (SINTAXIS INVARIABLE)
Si se solicita un snapshot de contexto, la única estructura válida es la de §6.
Prohibido añadir preámbulos, saludos o cierres meta-textuales fuera de ella.

DIRECTIVA DE INHIBICIÓN DE CHAT: prohibido generar cualquier texto antes del
primer carácter de salida. La respuesta debe comenzar directamente en
`## ACTIVE CONTEXT SUMMARY`.

---

## 7. CONDICIONES DE BLOQUEO

SHARED_CONTEXT no añade condiciones de bloqueo propias. Hereda exclusivamente las
de `TOS_MASTER` §6:
- Falta un dato de PERFIL en la CAPA DATO.
- Contradicción entre capas que la jerarquía §2 no resuelve.

La falta de campos de **contexto** (§4) no bloquea: degrada confianza y se avisa.

---

## 8. MODELO DE SIMPLICIDAD

Este módulo es markdown-first, manual y gobernado por prompt. No hay motor de
detección de drift automático, no hay reconciliación automática, no hay framework
de recuperación de estados: si el contexto se corrompe o queda obsoleto, se
regenera manualmente desde el último output validado de BPA/OME/CPE/IPE.

---

## 9. PRINCIPIO FINAL

SHARED_CONTEXT preserva coherencia entre ejecuciones modulares. Sin continuidad,
cada módulo opera a ciegas; con continuidad disciplinada, el pipeline se mantiene
trazable de punta a punta sin repetir trabajo.

---

# OUTPUT DESIGNATION
TOS_SHARED_CONTEXT · LEAN CONTINUITY LAYER · SIMPLE 4.0
