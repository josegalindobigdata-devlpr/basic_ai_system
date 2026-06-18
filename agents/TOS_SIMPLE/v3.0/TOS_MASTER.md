# TOS_MASTER — CONTROL FILE (LEAN)
<!-- TOS_SIMPLE v3.0 — Simplificación mono-usuario, perfil fijo. Sustituye a v2.0. -->
MODULE: TOS_MASTER
VERSION: SIMPLE_3.0
TYPE: GOVERNANCE

---

## 1. PROPÓSITO

Capa de control **mínima** de TOS_SIMPLE para un único titular con perfil fijo.
Garantiza tres cosas y nada más: precedencia de capas, secuencia del pipeline y disciplina
anti-deslizamiento. Se elimina toda flexibilidad multi-perfil (el sistema es de un solo
titular, ya decidido).

---

## 2. ARQUITECTURA Y AUTORIDAD (sin cambios)

- **CAPA DATO** (SSOT, se cita literal): `FACTS_SHEET > MASTER_CV_RAW > TARGET_POSITIONS_PROFILE`.
- **CAPA MÉTODO** (gobierna el cómo, no el qué; no contiene datos): `BPA, OME, CPE, IPE`.
- **CAPA GOBIERNO**: `TOS_MASTER, TOS_SHARED_CONTEXT, CHANGELOG`.

**Jerarquía (mayor → menor):** DATO > TOS_MASTER > MÉTODO > SHARED_CONTEXT.
**REGLA DE ORO:** el DATO manda sobre el MÉTODO. Dato de perfil ausente = BLOQUEO, nunca invención.

---

## 3. PERFIL: CONSTANTE FIJA (no es un estado)

- `PROFILE: LOCKED · v3.0` — validado por BPA **una sola vez**.
- `OBJETIVO` y `NO-NEGOCIABLES`: fijos, definidos por el titular.
- BPA solo se re-ejecuta si cambia el CV real, **no** en cada oportunidad.
- Se elimina STATE 0 (NO_PROFILE) y toda lógica multi-perfil de v2.0.

---

## 4. PIPELINE POR OPORTUNIDAD (estado ligero)

Flujo lineal, manual, con **una sola guardia**: no saltar pasos.

```
EVALUATE (OME) ──[si GO / GO-ADJ]──> POSITION (CPE) ──[si entrevista]──> INTERVIEW (IPE) ──> CLOSE
```

Reglas de secuencia (lo único que se gobierna):
- No CPE sin decisión OME = `GO` o `GO WITH ADJUSTMENT`.
- No IPE sin posicionamiento CPE.
- `NO GO` cierra la oportunidad sin avanzar.

Se elimina: la máquina de 9 estados, STATE_8 / recovery, el handoff-contract ceremonial y
las cabeceras universales obligatorias. No hay transiciones automáticas.

---

## 5. ENTRADA Y CABECERA (tolerante)

- Único input garantizado por oportunidad: **TÍTULO + DESCRIPCIÓN**.
- Ningún otro campo (Company, Comp, Status, Reporting…) es obligatorio; su ausencia no bloquea.
- La cabecera universal de v2.0 (SESSION_ID, OPPORTUNITY_ID, etc.) pasa a **OPCIONAL**: úsala
  solo si aporta y con lo que haya.
- Compensación ausente **nunca** bloquea.

---

## 6. BLOQUEO (mínimo)

Solo se bloquea si:
- Falta un dato de **PERFIL** en la CAPA DATO (no de la oferta).
- Hay contradicción entre capas que la jerarquía §2 no resuelve.

La falta de datos de la **OFERTA** no bloquea: degrada con `CONFIDENCE` y se avisa.

---

## 7. CONTINUIDAD

- `TOS_SHARED_CONTEXT` mantiene oportunidad activa y riesgos; no sobreescribe DATO ni MÉTODO.
- `CHANGELOG` registra cambios metodológicos e hitos.

---

# OUTPUT DESIGNATION
TOS_MASTER · LEAN CONTROL FILE · SIMPLE 3.0
