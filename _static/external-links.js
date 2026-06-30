// Mark external links in the main content so they open in a new tab and show
// the external-link indicator (↗, see quadriga.css). This covers links that we
// cannot annotate by hand in the source, in particular the bibliography entries
// generated from references.bib, as well as plain Markdown links that don't
// carry the explicit `class="external-link" target="_blank"` markup.
// See https://github.com/quadriga-dk/Text-Fallstudie-3/issues/57

(function () {
    function markExternalLinks() {
        var content =
            document.querySelector('article.bd-article') ||
            document.querySelector('article') ||
            document.querySelector('main') ||
            document.body;
        if (!content) return;

        content.querySelectorAll('a[href]').forEach(function (link) {
            var url;
            try {
                url = new URL(link.href, window.location.href);
            } catch (e) {
                return;
            }

            // Only decorate web links that point to a different host.
            if (url.protocol !== 'http:' && url.protocol !== 'https:') return;
            if (url.hostname === window.location.hostname) return;

            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
            link.classList.add('external-link');
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', markExternalLinks);
    } else {
        markExternalLinks();
    }
})();
