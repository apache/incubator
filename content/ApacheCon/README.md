
# ApacheCon Slides

Slides for ApacheCon

## Technology Used

The slides are generated from [asciidoctor](https://asciidoctor.org) markup and displayed with [reveal.js](https://asciidoctor.org/docs/asciidoctor-revealjs/). This means the content can be kept under version control and exported to a number of formats other than HTML.

## How to Build with Maven (recommended)

To install the needed dependencies on OSX run:

`install-deps.sh`

Then run:

`mvn clean compile`


## How to Build with Ruby or Node (minimal support)

It possisble to genrate the slides with other technologies, please see instructions at https://asciidoctor.org/docs/asciidoctor-revealjs/.

For node install the dependacies:

`npm i --save asciidoctor@^2.0 @asciidoctor/reveal.js`

And generate the slides via:

`node convert-slides.js`

Some of the assets will need to be moved and the apachecon.css theme included in the HTML.

## How to View the Slides (Maven)

Once built, the generated slides can be found at:

`target/generated-slides/index_en.html`

Just open the `index_en.html` in a browser to view the slides.

Some features require the slides to be viewed via a http/https url you can do this by running:

`mvn jetty:run-exploded`

And goto `http://127.0.0.1:8080/index_en.html` in a browser to view.

If you add ?print-pdf at the end of the URL, you can then print the slide deck into a PDF document.

## Helpful Key Shortcuts

Some key shortcuts that may help you give a presentation:

- Cursor keys and space can navigate the slides.
- Press S will show speaker notes and a timer in a separate window.
- Press F for full screen.
- Press N for next slide or P for previous slide.
- Press O (for overview) will show a slide map / overview.
- Press B will black the screen.
