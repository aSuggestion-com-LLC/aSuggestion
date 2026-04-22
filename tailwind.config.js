/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html"],
  theme: {
    extend: {
      colors: {
        brand: {
          navy: '#01384a',
          teal: '#00435d',
          orange: '#ef8110',
          blue: '#0099CC'
        }
      }
    }
  },
  plugins: []
}
