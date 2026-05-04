# AI System

Sistema modular de agentes basados en IA con una arquitectura centralizada de comportamiento base y agentes especializados por dominio.

---

## 🧠 Arquitectura del sistema

El proyecto está organizado en tres capas principales:
ai-system/
├── core/
├── agents/
│ ├── finanzas/
│ ├── marketing/
│ ├── data/
│ └── codex/
├── docs/
└── shared/

---

## 📦 core/

Contiene el comportamiento base del sistema.

Incluye:
- Definición del “prompt base” del sistema
- Reglas generales de comportamiento
- Configuración global de estilo y tono
- Lógica común de enrutamiento o interpretación

👉 Todo agente depende conceptual o funcionalmente de esta capa.

---

## 🤖 agents/

Contiene los agentes especializados por dominio.

Cada agente es un módulo independiente con su propia lógica y objetivos.

### Ejemplos:

- **finanzas/** → análisis financiero, métricas, decisiones económicas
- **marketing/** → generación de estrategias, copywriting, campañas
- **data/** → análisis de datos, procesamiento, insights
- **codex/** → asistencia en programación y desarrollo técnico

Cada agente puede incluir:
- Configuración propia
- Prompts específicos
- Flujos de trabajo
- Integraciones particulares

---

## 🔁 shared/

Contiene componentes reutilizables entre agentes.

Incluye:
- Utilidades comunes
- Helpers de procesamiento
- Funciones de integración
- Estructuras de datos compartidas

👉 Esta capa evita duplicación de lógica entre agentes.

---

## ⚙️ Principios del sistema

Este proyecto se basa en los siguientes principios:

### 1. Modularidad
Cada agente es independiente y puede evolucionar sin afectar al resto.

### 2. Centralización de comportamiento base
El comportamiento global reside en `core/`, garantizando coherencia del sistema.

### 3. Reutilización
Lógica común abstraída en `shared/` para evitar duplicación.

### 4. Escalabilidad
La arquitectura permite añadir nuevos agentes sin refactorizaciones mayores.

---

## 🔄 Flujo conceptual

1. El sistema define el comportamiento base en `core/`
2. Un usuario o sistema invoca un agente específico
3. El agente aplica:
   - reglas de `core/`
   - lógica propia del dominio
   - utilidades de `shared/`
4. Se genera una respuesta o acción especializada

---

## 📌 Reglas de desarrollo

- Todo nuevo comportamiento global debe residir en `core/`
- Todo código reutilizable debe colocarse en `shared/`
- Los agentes deben ser autónomos y no acoplarse entre sí
- Evitar duplicación de lógica entre agentes
- Mantener separación estricta de responsabilidades

---

## 🚀 Objetivo del sistema

Construir un ecosistema de agentes de IA especializados que trabajen sobre una base común coherente, permitiendo:

- Especialización por dominio
- Escalabilidad horizontal
- Mantenimiento controlado
- Evolución independiente por módulo

---

## 🧩 Extensibilidad

Para añadir un nuevo agente:

1. Crear carpeta en `agents/`
2. Definir su configuración y lógica
3. Conectarlo conceptualmente con `core/`
4. Reutilizar `shared/` cuando sea posible

Ejemplo:
agents/talento_senior
agents/abogado_matrimonialista

---
## Versionado

Para actualizar y versionar:
``` bash
	git remote add origin git@github-desarrollobd:josegalindobigdata-devlpr/basic_ai_system.git
	git add .
	git commit -m "Comentario significativo para el versionado"
	git push -u origin main
```
---

## 🧠 Nota final

Este sistema está diseñado para evolucionar como una arquitectura de agentes independientes coordinados por un núcleo común, permitiendo crecimiento progresivo sin pérdida de control estructural.
