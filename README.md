# 🧠 **DataEmployee – Análisis de Contrataciones**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📘 **Descripción general**

**DataEmployee** es un proyecto de análisis que integra **procesamiento de datos en Python**, **almacenamiento en SQLite** y **visualización en Power BI**.  
Su objetivo es entender el comportamiento de las **contrataciones por departamento, cargo y red de contactos**, generando información útil para la toma de decisiones.

El flujo parte desde la **limpieza y depuración de archivos CSV**, pasa por la **creación de una base de datos relacional**, y culmina con un **dashboard interactivo** en Power BI.

---

## 🧩 **Arquitectura general del proyecto**

```
DataEmployee/
│
├── dashboard/                # Dashboard Power BI (DataEmployee.pbix)
│
├── data/                     # Datos fuente y base de datos SQLite
│   ├── contacts.csv
│   ├── departments.csv
│   ├── jobs.csv
│   ├── hired_employees.csv
│   └── DataEmployee.db
│
├── logs/                     # Logs de ejecución y validaciones
│
├── src/                      # Código fuente del proyecto
│   ├── extract.py            # Extracción y limpieza
│   ├── load.py               # Creación y carga de tablas
│   └── main.py               # Script principal
│
├── test/                     # Scripts de prueba y validación
│
├── creacionEstandar.ps1      # Automatización en PowerShell
├── requirements.txt          # Dependencias del entorno
└── README.md
```

---

## ⚙️ **Ejecución del proyecto**

### 1️⃣ Crear entorno virtual
```bash
conda create -n DataEmployee python=3.11
conda activate DataEmployee
```

### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar flujo ETL
```bash
python src/main.py
```

El script genera la base `DataEmployee.db` con las tablas limpias y listas para análisis.

---

## 📊 **Dashboard Power BI**

El archivo `dashboard/DataEmployee.pbix` se conecta directamente a la base SQLite.  
El tablero responde a preguntas clave como:

- ¿Qué departamento concentra más contrataciones?  
- ¿Qué cargos tienen mayor impacto?  
- ¿Existe relación entre contactos y contrataciones?  

Incluye indicadores, comparativos por área, visuales temporales y mapa de distribución de contactos.

---

## 🧮 **Calidad de datos y perfilamiento**

Durante la limpieza se detectaron:
- **Duplicados y valores nulos** (eliminados).  
- **Inconsistencias** entre *country* y *region*.  
- **Conversiones de tipo**: el campo `datetime` fue transformado correctamente a tipo fecha.  

**Recomendaciones:**
- Normalizar ubicaciones geográficas.  
- Estandarizar claves y tipos de datos en origen.  
- Implementar validaciones automáticas en futuras integraciones.

---

## 🧠 **Hallazgos clave**

- Las áreas administrativas y financieras lideran las contrataciones.  
- Los departamentos con mayor red de contactos tienden a contratar más.  
- Los cargos técnicos y operativos presentan mayor concentración de nuevos ingresos.  

El dashboard permite explorar estos patrones por filtros de tiempo, área y país.

---

## 📦 **Entregables**

- ✅ Dashboard funcional en Power BI (`DataEmployee.pbix`)  
- ✅ Scripts Python para extracción, limpieza y carga (`src/`)  
- ✅ Base de datos SQLite (`DataEmployee.db`)  
- ✅ Presentación ejecutiva de hallazgos (`Presentación Prueba Técnica Analista de Datos.docx`)  

---

