# 'Aioli' recipe-book-core

![Aioli](docs/aioli.png)

This is a simple(ish) python implementation of a static-site-generator designed solely to make a recipe-book out of Asciidoctor(ish) files.

The core concept is using a simple file with a title, set of ingredients, and steps, and turning that into a webpage that presents the same information in an easy to digest format. The built static site features pagination(ish), subpages, working links, etc.

## Usage

1. Download the source code from the repository or from the releases page.

2. Extract it into a folder of your choosing.

3. Add in recipes to the recipe folder in asciidoc format:

```asciidoc
= title

* ingredient 1
* ingredient 2
* ingredient 3

. step 1
. step 2
. step 3
```

4. Build using `build.py`, opening the build folder and opening `home1.html`.
