// Make the inline 🚀 / ↓ icons in the "Hinweise zur Ausführung" box actually
// clickable. Readers kept trying to click the rocket in the sentence instead of
// the launch button in the top-right toolbar (see issues #135, #146, #152, #157).
// The markdown wraps those icons in <span class="launch-colab-inline">🚀</span>
// and <span class="launch-ipynb-inline">↓</span>; here we point them at the same
// targets the toolbar buttons use. If a target can't be found we leave the icon
// as inert text rather than create a dead link.
//
// Toolbar DOM (sphinx-book-theme), verified against the live build:
//   .dropdown-launch-buttons   a[href*="colab.research.google.com"]  (Colab)
//   .dropdown-download-buttons a.btn-download-source-button[href$=".ipynb"]
(function () {
    // First matching element for any of the given selectors (most precise first).
    function pick(selectors) {
        for (var i = 0; i < selectors.length; i++) {
            var el = document.querySelector(selectors[i]);
            if (el) return el;
        }
        return null;
    }

    // Turn a marker <span> into an <a>, preserving its content and classes.
    function linkify(span, href, opts) {
        opts = opts || {};
        var a = document.createElement('a');
        a.href = href;
        a.className = span.className;
        a.innerHTML = span.innerHTML;
        if (opts.ariaLabel) a.setAttribute('aria-label', opts.ariaLabel);
        if (opts.newTab) {
            a.target = '_blank';
            a.rel = 'noopener';
        }
        if (opts.download) a.setAttribute('download', opts.download);
        span.replaceWith(a);
    }

    function wireInlineRunLinks() {
        // --- Cloud Mode: link the rocket to the toolbar's Colab entry ---
        var colab = pick([
            '.dropdown-launch-buttons a[href*="colab.research.google.com"]',
            'a[href*="colab.research.google.com"]'
        ]);
        if (colab) {
            document.querySelectorAll('span.launch-colab-inline').forEach(function (span) {
                linkify(span, colab.href, {
                    newTab: true,
                    ariaLabel: 'Dieses Notebook in Colab öffnen'
                });
            });
        }

        // --- Local Mode: link the download arrow to the .ipynb source ---
        // Same link force-ipynb-download.js targets; that script adds the
        // download attribute too, so same-origin clicks save the file.
        var source = pick([
            '.dropdown-download-buttons a.btn-download-source-button[href$=".ipynb"]',
            'a.btn-download-source-button[href$=".ipynb"]',
            'a[href$=".ipynb"]'
        ]);
        if (source) {
            var name = '';
            try {
                name = new URL(source.href, window.location.href).pathname.split('/').pop();
            } catch (e) { /* leave name empty */ }
            document.querySelectorAll('span.launch-ipynb-inline').forEach(function (span) {
                linkify(span, source.href, {
                    download: name,
                    ariaLabel: 'Notebook als .ipynb herunterladen'
                });
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', wireInlineRunLinks);
    } else {
        wireInlineRunLinks();
    }
})();
