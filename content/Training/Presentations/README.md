
# Apache Training - Contributing more than just code

How to make presentations with simple plain text markup that look nice. 

## Technology Used

The slides are generated from [asciidoctor](https://asciidoctor.org) markup and displayed with [reveal.js](https://asciidoctor.org/docs/asciidoctor-revealjs/). This means the content can be kept under version control and exported to a number of formats other than HTML.

## How to Build

To install the needed dependencies on OSX run:

`install-deps.sh`

Then run:

`mvn clean compile`

## How to View the Slides

Once built, the generated slides can be found at:

`target/generated-slides/index_en.html`

Just open the `index_en.html` in a browser to view the slides.

Some features require the slides to be viewed via a http/https url you can do this by running:

`mvn jetty:run-exploded`

And goto `http://127.0.0.1:8080/index_en.html` in a browser to view.

If you add ?print-pdf at the end of the URL, you can then print the slide deck into a PDF document.

Some key shortcuts that may help you give a presentation:

- Cursor keys and space can navigate the slides.
- Press S will show speaker notes and a timer in a separate window.
- Press F for full screen.
- Press N for next slide or P for previous slide.
- Press O (for overview) will show a slide map / overview.
- Press B will black the screen.
