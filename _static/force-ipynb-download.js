// Make the header "Download ↓ → .ipynb" button download the notebook file
// instead of opening the raw JSON inline in the browser. sphinx-book-theme
// renders the source link as a plain <a href="_sources/….ipynb"> without the
// HTML5 `download` attribute, so browsers navigate to it (and render the JSON)
// instead of saving it. We add `download` (same-origin only) and drop any
// target="_blank" so the click saves the file. See
// https://github.com/quadriga-dk/Text-Fallstudie-3/issues/155
(function () {
    function forceIpynbDownload() {
        document.querySelectorAll('a[href$=".ipynb"]').forEach(function (link) {
            var url;
            try {
                url = new URL(link.href, window.location.href);
            } catch (e) {
                return;
            }
            // download attribute only works for same-origin URLs.
            if (url.hostname !== window.location.hostname) return;

            link.setAttribute('download', url.pathname.split('/').pop());
            link.removeAttribute('target');
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', forceIpynbDownload);
    } else {
        forceIpynbDownload();
    }
})();
