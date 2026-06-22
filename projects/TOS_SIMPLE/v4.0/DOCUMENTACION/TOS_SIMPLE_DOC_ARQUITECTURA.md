# TOS_SIMPLE — ARQUITECTURA DE REFERENCIA
<!-- TOS_SIMPLE v4.0 — Arquitectura de 4 capas -->

VERSION_DOC: 2.0
SYSTEM VERSION: SIMPLE_4.0
PLATFORM: Claude Projects
PURPOSE: Referencia arquitectónica del sistema TOS_SIMPLE

---

## 1. PRINCIPIO CENTRAL

TOS_SIMPLE es un sistema experto de gestión de carrera gobernado por IA, implementado como **Claude Project**.

Flujo de valor (invariable):

```
VERDAD → EVALUACIÓN → POSICIONAMIENTO → EJECUCIÓN
```

Garantías del sistema:
- Sin invención de datos
- Sin escalado de métricas
- Sin deslizamiento narrativo

---

## 2. ARQUITECTURA DE 4 CAPAS

Cuatro capas con responsabilidades **disjuntas** y jerarquía de autoridad inequívoca.
La cuarta capa (ENTREGABLE) es subordinada: no tiene autoridad sobre las tres anteriores.

---

### CAPA 1 — DATO (SSOT)
Se cita literalmente. Nunca se infiere. Nunca se reformula.

| Fichero | Rol | Versión |
|---|---|---|
| `FACT_SHEETS.md` | Constantes invariables: titulares por rol ancla, cifras de cabecera, certificaciones, formación, reglas de citación. Última palabra. | v3.1 |
| `MASTER_CV_RAW.md` | Historial laboral completo. Métricas exactas por puesto. Autoridad máxima del sistema. | v3.0 LOCKED |
| `TARGET_POSITIONS_PROFILE.md` | Matriz de los 3 Roles Ancla (SDM / GOV / DLV): dolores de cliente, keywords ATS, estrategia de posicionamiento. | v3.0 |
| `PORTFOLIO_CAPABILITIES.md` | Inventario STAR/CAR de 23 bloques de experiencia. **Derivado** de MASTER_CV_RAW — si contradicen, gana MASTER. **Carga condicional:** solo cuando el módulo activo es CPE o IPE. | v3.0 |

---

### CAPA 2 — MÉTODO
Gobiernan el **CÓMO**. Nunca el QUÉ. No contienen datos.

| Módulo | Función | Principio |
|---|---|---|
| `TOS_1_BPA.md` | Validación de verdad profesional. Apunta a CAPA DATO; no es la fuente del dato. Se ejecuta **una sola vez** (salvo cambio real de CV). | *Truth before positioning* |
| `TOS_2_OME.md` | Evaluación estratégica de oportunidades. Anchor Resolution + FIT/GAP + GO·NO-GO + Positioning Strategy. | *Evaluation before commitment* |
| `TOS_3_CPE.md` | Posicionamiento, narrativa y ensamblaje de CV (Contrato de Adaptación §4A). Único motor que produce CAPA ENTREGABLE. | *Positioning without distortion* |
| `TOS_4_IPE.md` | Preparación y ejecución de entrevistas. Narrativa, simulación de presión, gestión de objeciones, defensa salarial. | *Execution without drift* |

---

### CAPA 3 — GOBIERNO
Control de estado, secuencia y continuidad.

| Fichero | Función |
|---|---|
| `TOS_MASTER.md` | Núcleo de gobierno: jerarquía de capas, secuencia del pipeline, reglas de transición y bloqueo. |
| `TOS_SHARED_CONTEXT.md` | Continuidad contextual entre módulos y sesiones. Schema de 9 campos (PROFILE_VERSION, CURRENT_STATE, ACTIVE_OPPORTUNITY, LAST_OME_DECISION, etc.). |
| `CHANGELOG.md` | Trazabilidad y control evolutivo. Registro de todos los cambios estructurales. |

---

### CAPA 4 — ENTREGABLE (subordinada)
Outputs validados. Sin autoridad sobre las tres capas superiores.

**Tier 1 — CV ANCLA BASE** (congelados)

| Fichero | Ancla | Estado |
|---|---|---|
| `CV_ANCLA_SDM_ESP.md` | SDM | FROZEN_REV: 1.0 · BASED_ON: MASTER_CV_RAW v3.0 |
| `CV_ANCLA_GOV_ESP.md` | GOV | FROZEN_REV: 1.0 · BASED_ON: MASTER_CV_RAW v3.0 |
| `CV_ANCLA_DLV_ESP.md` | DLV | FROZEN_REV: 1.0 · BASED_ON: MASTER_CV_RAW v3.0 |

- Solo se regeneran vía CPE. **No se editan a mano.**
- Si MASTER_CV_RAW avanza de versión → quedan **STALE** hasta re-validación por CPE.

**Tier 2 — CV ADAPTADO** (efímero)
- Salida de CPE por oportunidad: ancla base + adiciones de PORTFOLIO + matiz de alineación.
- No es fichero gobernado. No es SSOT. Ningún motor lo lee como verdad.
- Se produce, se usa y se descarta.

---

## 3. JERARQUÍA DE AUTORIDAD

```
DATO > TOS_MASTER > MÉTODO > SHARED_CONTEXT > ENTREGABLE
```

**REGLA DE ORO:** el DATO manda sobre el MÉTODO. Siempre.

**REGLA DE ENTREGABLE:** si un CV Ancla contradice a MASTER_CV_RAW, el ancla se **regenera** vía CPE. Nunca al revés.

**DATO AUSENTE = BLOQUEO:** si un dato necesario no existe en CAPA DATO, el sistema se detiene. No se inventa, no se infiere.

---

## 4. ESTRUCTURA DE FICHEROS DEL PROYECTO

```
/TOS_SIMPLE/ (Claude Project — knowledge base)
│
├── ── CAPA DATO (SSOT) ───────────────────────────
│   ├── FACT_SHEETS.md                  ← v3.1
│   ├── MASTER_CV_RAW.md                ← v3.0 LOCKED
│   ├── TARGET_POSITIONS_PROFILE.md     ← v3.0
│   └── PORTFOLIO_CAPABILITIES.md       ← v3.0 (condicional CPE/IPE)
│
├── ── CAPA MÉTODO ────────────────────────────────
│   ├── TOS_1_BPA.md
│   ├── TOS_2_OME.md
│   ├── TOS_3_CPE.md
│   └── TOS_4_IPE.md
│
├── ── CAPA GOBIERNO ──────────────────────────────
│   ├── TOS_MASTER.md
│   ├── TOS_SHARED_CONTEXT.md
│   └── CHANGELOG.md
│
├── ── CAPA ENTREGABLE (Tier 1 — congelados) ──────
│   ├── CV_ANCLA_SDM_ESP.md             ← FROZEN_REV 1.0
│   ├── CV_ANCLA_GOV_ESP.md             ← FROZEN_REV 1.0
│   └── CV_ANCLA_DLV_ESP.md             ← FROZEN_REV 1.0
│
└── ── DOCUMENTACIÓN (externa al sistema) ─────────
    ├── TOS_SIMPLE_DOC_ARQUITECTURA.md  ← este fichero
    └── TOS_SIMPLE_DOC_OPERACION.md
```

---

## 5. ROLES ANCLA

Taxonomía de posicionamiento de carrera (no son perfiles de comportamiento del asistente).

| Ancla | Titular de mercado | Dolores de cliente |
|---|---|---|
| **SDM** | Senior IT Service Delivery Manager | OPEX, SLAs, gobierno de proveedores, eficiencia operativa, P&L |
| **GOV** | IT Governance & PMO Lead | Alineación estratégica, control de portafolio, PMO corporativa, SteerCo, reporting ejecutivo |
| **DLV** | Senior IT Delivery Manager | Plataformas de datos, SDLC, reporting regulatorio, predictibilidad de entrega |

---

## 6. PIPELINE LINEAL

```
EVALUATE (OME) ──[GO / GO-ADJ]──> POSITION (CPE) ──[entrevista]──> INTERVIEW (IPE) ──> CLOSE
```

Reglas de secuencia (no se saltan):
- No CPE sin OME = `GO` o `GO WITH ADJUSTMENT`.
- No IPE sin posicionamiento CPE completado.
- `NO GO` cierra la oportunidad. Sin avance.
- BPA se ejecuta **una sola vez** (perfil fijo). Solo se re-ejecuta si cambia el CV real.

---

## 7. CONTRATO DE ADAPTACIÓN DE CV (§4A — resumen)

Adaptar un CV = **recombinar proyecciones ya validadas del MASTER**. Nunca crear material nuevo.

**Operaciones PERMITIDAS (allowlist — todo lo no listado está prohibido):**

1. **Selección** — elegir ancla base (lo decide OME vía Anchor Resolution).
2. **Reordenación** — reordenar bloques/logros por relevancia a la oferta; sin cambiar contenido.
3. **Énfasis / Compresión** — destacar o comprimir bloques existentes; sin añadir hechos.
4. **Adición de piezas** — insertar bloques que ya existen en PORTFOLIO_CAPABILITIES.
5. **Matiz de alineación** — reformular keywords hacia el vocabulario de la oferta, sin tocar métricas, fechas ni hechos.

**Operaciones PROHIBIDAS:** inventar logros · elevar cifras o seniority · cambiar fechas · mezclar métricas entre clientes · fabricar narrativa de transición.

---

## 8. REGLAS HARDCODED (aplicables en todo entregable)

1. **200K vs 500K:** nunca mezclar. Toda mención a las 500K incluye la palabra **"acumulado"**.
2. **Redondeo:** porcentajes de impacto al entero más próximo en entregables de mercado. Decimales solo en MASTER_CV_RAW (auditoría interna).
3. **Anti-edadismo:** en CV, citar solo el **año de finalización** de la formación.
4. **Rol Advisor:** excluido de los CV Ancla. Solo se usa en estrategia paraguas LinkedIn.
5. **"Transformation":** no usar como titular principal en los roles ancla salvo exigencia explícita de la oferta.

---

## 9. VERSIONES ACTIVAS

| Eje | Elemento | Versión |
|---|---|---|
| Sistema / Arquitectura | Todos los módulos de gobierno y método | SIMPLE_4.0 |
| Dato / Perfil | MASTER_CV_RAW · TARGET_POSITIONS_PROFILE · PORTFOLIO_CAPABILITIES | v3.0 LOCKED |
| Dato / Perfil | FACT_SHEETS | v3.1 |
| Entregable | CV Ancla x3 | FROZEN_REV 1.0 · BASED_ON: MASTER v3.0 |
| Linaje propio IPE | TOS_4_IPE | ANCHORED_OPTIMIZED_1.2 |

---

TOS_SIMPLE · DOC_ARQUITECTURA · v2.0 · SIMPLE_4.0
