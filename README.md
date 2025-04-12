# 📚 Proyecto Académico - Grupo A NRC 23729
**Evaluación Parcial: Gestión de Código con Git y GitHub**

[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/GrupoA-NRC23729/proyecto/deploy.yml?label=Despliegue%20CI/CD)](https://github.com/GrupoA-NRC23729/proyecto/actions)
[![GitFlow](https://img.shields.io/badge/GitFlow-Implementado-success)](https://nvie.com/posts/a-successful-git-branching-model/)

## 🏗️ Estructura del Proyecto
├── .github/
│ └── workflows/
│ └── deploy.yml
├── css/
│ └── styles.css
├── img/
│ ├── bg.jpg
│ └── intro.jpg
├── js/
│ └── scripts.js
├── index.html
└── favicon.ico


## 🛠️ Tecnologías Implementadas
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Control de Versiones**: Git + GitHub
- **Metodología**: GitFlow
- **CI/CD**: GitHub Actions
- **Hosting**: GitHub Pages

## 🔄 Flujo de Trabajo GitFlow
Implementamos estrictamente el modelo GitFlow:

```bash
# Ejemplo de creación de feature
git checkout develop
git checkout -b feature/navbar-responsive
# Desarrollo... luego:
git push origin feature/navbar-responsive
# Crear Pull Request para revisión


Ramas principales:

main: Versiones estables (production)

develop: Integración continua

feature/*: Desarrollo de nuevas funcionalidades

hotfix/*: Correcciones urgentes

⚡ Automatización CI/CD
Configuración en .github/workflows/deploy.yml:

name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./


🧩 Resolución de Conflictos
Proceso documentado para manejo de conflictos:

Sincronizar ramas frecuentemente:

git pull origin develop


👥 Contribuciones
Miembro	Rol	Commits	PRs
Wilder Andrade	Frontend	15	3
Edgar Moya	GitFlow Manager	12	2
Anthony Quispe	QA Testing	10	2
Eyner Salvador	Documentación	8	1
Paulo Vásquez	CI/CD Specialist	9	2
📊 Métricas del Proyecto
Total de commits: 54

Pull requests mergeados: 10

Issues cerrados: 7

Despliegues automáticos: 5

📄 Licencia
MIT License © 2025 - Grupo A NRC 23729

License


