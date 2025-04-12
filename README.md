# Grupo A - NRC 23729: Construcción de Software

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/tu-usuario/tu-repo/deploy.yml?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/tu-usuario/tu-repo?style=flat-square)

Proyecto colaborativo que implementa GitFlow, CI/CD y buenas prácticas de desarrollo.

## 🌐 Demo
[Ver sitio en GitHub Pages](https://tu-usuario.github.io/tu-repo/)

## 🛠️ Tecnologías
- HTML5, CSS3, Bootstrap 5
- GitHub Actions (CI/CD)
- GitFlow

## 📂 Estructura del proyecto
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



## 🔀 Flujo de trabajo GitFlow
```bash
# Crear nueva feature
git checkout develop
git checkout -b feature/nueva-funcionalidad

# Subir cambios
git push origin feature/nueva-funcionalidad

# Crear Pull Request a develop

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


👥 Colaboradores
Integrante	Perfil GitHub	Portafolio
Wilder	@WilderAndr	Ver
Edgar	@moyacoasaca	Ver
Anthony	@Antonymq1097	Ver
Eyner	@EynerSalvador	Ver
Paulo	@pvasquezb	Ver

