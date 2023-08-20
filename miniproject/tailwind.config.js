module.exports = {
    darkMode: 'class',
    content: [
        './templates/**/*.html',
        'node_modules/preline/dist/*.js',
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('preline/plugin'),
        require('@tailwindcss/typography'),
    ],
}