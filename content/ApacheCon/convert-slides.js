// Load Asciidoctor.js and the reveal.js converter
var asciidoctor = require('@asciidoctor/core')()
var asciidoctorRevealjs = require('@asciidoctor/reveal.js')
asciidoctorRevealjs.register()

// Convert the document using the reveal.js converter
var options = { safe: 'safe', backend: 'revealjs' }
asciidoctor.convertFile('src/main/asciidoc/index_en.adoc', options) 
