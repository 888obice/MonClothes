// ✅ tailwind.config.js — Configuración para Tailwind v4+
export default {
  content: [
    "./templates/**/*.html",
    "./store/templates/**/*.html",
    "./**/*.html",
  ],

  theme: {
    extend: {
      colors: {
        rosaPalo: "#F2D0D9",
        azulOscuro: "#010D26",
      },
    },
  },

  // Tailwind v4 usa ahora las variables declaradas en @theme
  // en tu input.css, no necesitas definir fontFamily aquí.
  // Pero si quieres autocompletado en VS Code o mantener compatibilidad,
  // puedes dejarlas también:
  fontFamily: {
    sans: ["Inter", "sans-serif"],
    display: ["Bebas Neue", "sans-serif"],
  },

  plugins: [],
};

