document.querySelectorAll('figure.code button').forEach(function (b) {
  b.addEventListener('click', function () {
    var t = b.closest('figure').querySelector('pre code').innerText;
    function done() { var o = b.textContent; b.textContent = 'คัดลอกแล้ว'; setTimeout(function () { b.textContent = o; }, 1500); }
    function fb() {
      var a = document.createElement('textarea'); a.value = t; document.body.appendChild(a); a.select();
      try { document.execCommand('copy'); done(); } catch (e) {}
      document.body.removeChild(a);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(t).then(done, fb); } else { fb(); }
  });
});
