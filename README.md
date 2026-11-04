# Portfolio

Source of https://fitranurmayadi.github.io/portofolio

One hand-written page: `index.html` and `style.css`, with photos in `assets/images/` and videos in `assets/video/`. There is no JavaScript and no build step. GitHub Pages serves the `main` branch from the repository root.

Every project is a card with the same layout: a 16:10 cover, a short description, two key facts, and a `<details>` block that holds the extra pictures and tables until a visitor opens it. Selected work is a two-column grid, simulations sit in a dark band, and older builds are 4:3 tiles. Type is Manrope and JetBrains Mono from Google Fonts.

When `style.css` changes, bump the `?v=` number on its `<link>` in `index.html`, otherwise returning visitors can get the new page with the old stylesheet for up to ten minutes.

`assets/images/quadruped_times.svg` is drawn from the quadruped results table; there is no photo of that project.

`presentation.html` and `Fitra_Nurmayadi_Technical_Portfolio.pptx` are a separate slide deck, built by `build_presentation.py`.

Every number on the page should come from a measurement or a project README.
