# 🚀 FastAPI Price Monitor: Sistema de Monitoreo de Precios Resiliente

Este proyecto es un sistema backend robusto diseñado para rastrear precios de productos en diversas plataformas de e-commerce (como Mercado Libre), permitiendo a los usuarios automatizar el ahorro mediante alertas inteligentes y análisis de datos históricos.

## 🎯 Objetivo del Proyecto
Desarrollar un servicio backend capaz de realizar web scraping asíncrono para monitorear variaciones de precios, almacenar el historial de cambios y notificar al usuario cuando un producto alcance un precio objetivo, garantizando la resiliencia ante cambios en la estructura del sitio web original.

---

## 🛠️ Refinamiento Técnico

### 1. Requerimientos Funcionales (RF)
- **Gestión de Productos (CRUD):** Registro de URLs, selectores CSS/XPath y precios objetivos.
- **Scraping Asíncrono:** Motor de extracción que no bloquea la ejecución del API.
- **Historial de Precios:** Registro cronológico de cada variación detectada.
- **Sistema de Alertas:** Disparo de notificaciones (Email/Webhook) al cumplirse el umbral de precio.
- **Monitor de Salud (Resiliencia):** Detección y notificación de fallos en los selectores de scraping.

### 2. Requerimientos No Funcionales (RNF)
- **Concurrencia:** Capacidad de procesar múltiples rastreos simultáneos usando `httpx` y `asyncio`.
- **Normalización de Datos:** Limpieza automática de strings monetarios a valores numéricos comparables.
- **Integridad de Datos:** Relación estricta entre productos, historial y logs de error.

---

### 🗄️ Modelo de Datos (Entidades)

| Entidad | Campos Clave | Descripción |
| :--- | :--- | :--- |
| **Producto** | `id`, `url`, `selector`, `target_price`, `status` | Define qué y cómo se rastrea. |
| **HistorialPrecio** | `id`, `producto_id`, `precio`, `timestamp` | Almacena la evolución del costo en el tiempo. |
| **LogErrores** | `id`, `producto_id`, `error_msg`, `created_at` | Registra fallos de red o de cambios en el DOM. |

---

### 🛡️ Estrategia de Resiliencia
Para asegurar que el sistema no "muera" si una tienda cambia su diseño, se implementa:
1. **Try/Catch de Extracción:** Captura de excepciones específicas de selectores.
2. **Sistema de Reintentos:** Tres intentos antes de marcar un producto en estado "Revisión Requerida".
3. **Estrategia Multi-Selector:** Soporte para Meta Tags de SEO (`itemprop="price"`) como respaldo al CSS tradicional.

---

## 🏗️ Stack Tecnológico
- **Lenguaje:** Python 3.12+
- **Framework:** FastAPI
- **Base de Datos:** PostgreSQL / SQLAlchemy
- **Scraping:** BeautifulSoup4 / Playwright
- **Tareas Programadas:** APScheduler