/* 80386 手册中文版 — 阅读交互 */
(function () {
  "use strict";
  var doc = document.documentElement;
  var body = document.body;
  var root = body.getAttribute("data-root") || "";

  /* ---------------------------------------------------------- theme */
  function currentTheme() {
    var t = doc.dataset.theme || "auto";
    if (t !== "auto") return t;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function setTheme(t) {
    doc.dataset.theme = t;
    try { localStorage.setItem("i386-theme", t); } catch (e) {}
  }
  function cycleTheme() {
    var t = currentTheme();
    setTheme(t === "dark" ? "light" : "dark");
  }

  /* ---------------------------------------------------------- font size */
  var sizes = [0.94, 1, 1.08, 1.16];
  function currentScale() {
    var v = parseFloat(getComputedStyle(doc).getPropertyValue("--reader-font-scale")) || 1;
    var best = 0, diff = 9;
    sizes.forEach(function (s, i) { if (Math.abs(s - v) < diff) { diff = Math.abs(s - v); best = i; } });
    return best;
  }
  function cycleFont() {
    var i = (currentScale() + 1) % sizes.length;
    doc.style.setProperty("--reader-font-scale", sizes[i]);
    try { localStorage.setItem("i386-font", sizes[i]); } catch (e) {}
    toast("正文字号 " + Math.round(sizes[i] * 100) + "%");
  }

  var toastEl = null, toastTimer = null;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement("div");
      toastEl.className = "toast";
      toastEl.setAttribute("role", "status");
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = msg;
    toastEl.classList.add("is-visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove("is-visible"); }, 1600);
  }

  /* ---------------------------------------------------------- nav drawer */
  function closeNav() { body.classList.remove("nav-open"); }
  function toggleNav() { body.classList.toggle("nav-open"); }

  /* ---------------------------------------------------------- progress + spy */
  var bar = document.getElementById("progress-bar");
  var toTop = document.querySelector(".to-top");
  var sections = Array.prototype.slice.call(document.querySelectorAll(".sec[id]"));
  var railLinks = Array.prototype.slice.call(document.querySelectorAll(".rail-list a[data-spy]"));
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc-secs a"));
  var lastActive = null;

  function onScroll() {
    var h = document.documentElement;
    var max = h.scrollHeight - window.innerHeight;
    var p = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
    if (bar) bar.style.width = (p * 100).toFixed(2) + "%";
    if (toTop) toTop.classList.toggle("is-visible", window.scrollY > 700);

    if (!sections.length) return;
    var probe = window.scrollY + 120;
    var active = sections[0];
    for (var i = 0; i < sections.length; i++) {
      if (sections[i].offsetTop <= probe) active = sections[i];
      else break;
    }
    var id = active.id;
    if (id === lastActive) return;
    lastActive = id;
    railLinks.forEach(function (a) { a.classList.toggle("is-current", a.getAttribute("data-spy") === id); });
    tocLinks.forEach(function (a) { a.classList.toggle("is-current", a.getAttribute("href") === "#" + id); });
    var current = document.querySelector('.rail-list a[data-spy="' + id + '"]');
    if (current) {
      var box = current.parentElement.parentElement;
      var r = current.getBoundingClientRect(), b = box.getBoundingClientRect();
      if (r.top < b.top + 8 || r.bottom > b.bottom - 8) {
        current.scrollIntoView({ block: "nearest" });
      }
    }
  }

  var ticking = false;
  window.addEventListener("scroll", function () {
    if (!ticking) { requestAnimationFrame(function () { onScroll(); ticking = false; }); ticking = true; }
  }, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });

  /* ---------------------------------------------------------- search */
  var modal = document.getElementById("search-modal");
  var input = document.getElementById("search-input");
  var resultsBox = document.getElementById("search-results");
  var hint = document.getElementById("search-hint");
  var countEl = document.getElementById("search-count");
  var indexPromise = null;
  var results = [];
  var activeIndex = -1;

  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch(root + "assets/search.json")
        .then(function (r) { return r.json(); })
        .then(function (data) { return data.docs || []; })
        .catch(function () { return []; });
    }
    return indexPromise;
  }

  function openSearch() {
    modal.hidden = false;
    body.style.overflow = "hidden";
    loadIndex().then(function () { input.focus(); input.select(); });
  }
  function closeSearch() {
    modal.hidden = true;
    body.style.overflow = "";
    if (input) input.value = "";
    if (resultsBox) resultsBox.innerHTML = "";
    if (hint) hint.style.display = "";
    if (countEl) countEl.textContent = "";
    results = [];
    activeIndex = -1;
  }

  function isCJK(ch) { return /[\u3400-\u9fff]/.test(ch); }

  function queryTokens(q) {
    q = q.trim().toLowerCase();
    var tokens = [];
    var latin = q.match(/[a-z0-9_][a-z0-9_.\-]*/g) || [];
    latin.forEach(function (w) { if (w.length > 1) tokens.push(w); });
    var runs = q.match(/[\u3400-\u9fff]+/g) || [];
    runs.forEach(function (run) {
      if (run.length === 1) tokens.push(run);
      for (var i = 0; i < run.length - 1; i++) tokens.push(run.slice(i, i + 2));
    });
    var seen = {};
    return tokens.filter(function (t) { return t && !seen[t] && (seen[t] = 1); });
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"]/g, function (c) { return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]; });
  }

  function highlight(text, tokens) {
    var safe = escapeHtml(text);
    if (!tokens.length) return safe;
    var pattern = tokens.slice().sort(function (a, b) { return b.length - a.length; })
      .map(function (t) { return t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }).join("|");
    try {
      return safe.replace(new RegExp("(" + pattern + ")", "gi"), "<mark>$1</mark>");
    } catch (e) { return safe; }
  }

  function snippet(text, tokens) {
    var lower = text.toLowerCase();
    var pos = -1;
    for (var i = 0; i < tokens.length; i++) {
      var p = lower.indexOf(tokens[i]);
      if (p !== -1 && (pos === -1 || p < pos)) pos = p;
    }
    if (pos === -1) pos = 0;
    var start = Math.max(0, pos - 42);
    var end = Math.min(text.length, pos + 160);
    return (start > 0 ? "…" : "") + text.slice(start, end) + (end < text.length ? "…" : "");
  }

  function scoreDoc(d, tokens, phrase) {
    var text = d.x.toLowerCase();
    var title = (d.t + " " + d.c + " " + d.n).toLowerCase();
    var score = 0;
    var matched = 0;
    tokens.forEach(function (t) {
      var n = 0, p = text.indexOf(t);
      while (p !== -1 && n < 12) { n++; p = text.indexOf(t, p + t.length); }
      var tn = title.indexOf(t) !== -1 ? 1 : 0;
      if (n || tn) matched++;
      var norm = Math.sqrt(1 + text.length / 1500);
      score += (n / norm) * (1 + Math.min(t.length, 4) * 0.35) + tn * 16;
      if (/[㐀-鿿]/.test(t)) {
        Array.from(new Set(t)).forEach(function (ch) {
          if (title.indexOf(ch) !== -1) score += 4;
        });
      }
      if (/[㐀-鿿]/.test(t)) {
        Array.from(new Set(t)).forEach(function (ch) {
          if (title.indexOf(ch) !== -1) score += 4;
        });
      }
    });
    if (!matched) return 0;
    score += matched * 6;
    if (phrase && text.indexOf(phrase) !== -1) score += 24;
    if (title.indexOf(phrase) !== -1) score += 40;
    return score;
  }

  function renderResults(q) {
    var tokens = queryTokens(q);
    var phrase = q.trim().toLowerCase();
    if (!tokens.length) {
      results = [];
      resultsBox.innerHTML = "";
      hint.style.display = "";
      countEl.textContent = "";
      return;
    }
    hint.style.display = "none";
    loadIndex().then(function (docs) {
      if (input.value.trim() !== q.trim()) return;
      var scored = [];
      docs.forEach(function (d) {
        if (!d.x && !d.t) return;
        var s = scoreDoc(d, tokens, phrase);
        if (s > 0) scored.push({ d: d, s: s });
      });
      scored.sort(function (a, b) { return b.s - a.s; });
      results = scored.slice(0, 24);
      activeIndex = results.length ? 0 : -1;
      countEl.textContent = results.length ? results.length + " 条结果" : "";
      if (!results.length) {
        resultsBox.innerHTML = '<div class="search-empty">没有匹配「' + escapeHtml(q) + '」的内容。<br>试试更短的关键词，或用英文术语（如 paging、descriptor）。</div>';
        return;
      }
      resultsBox.innerHTML = results.map(function (r, i) {
        var d = r.d;
        return '<a class="search-result' + (i === 0 ? " is-active" : "") + '" href="' + root + d.u + '" data-i="' + i + '">' +
          '<span class="sr-top"><span>' + highlight(d.t, tokens) + '</span><span class="sr-ch">' + escapeHtml(d.c) + "</span></span>" +
          "<p>" + highlight(snippet(d.x, tokens), tokens) + "</p></a>";
      }).join("");
    });
  }

  function moveActive(delta) {
    if (!results.length) return;
    activeIndex = (activeIndex + delta + results.length) % results.length;
    Array.prototype.forEach.call(resultsBox.children, function (el, i) {
      el.classList.toggle("is-active", i === activeIndex);
    });
    var el = resultsBox.children[activeIndex];
    if (el) el.scrollIntoView({ block: "nearest" });
  }

  var debounce = null;
  input && input.addEventListener("input", function () {
    clearTimeout(debounce);
    var q = input.value;
    debounce = setTimeout(function () { renderResults(q); }, 90);
  });
  input && input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") { e.preventDefault(); moveActive(1); }
    else if (e.key === "ArrowUp") { e.preventDefault(); moveActive(-1); }
    else if (e.key === "Enter") {
      e.preventDefault();
      var el = resultsBox.children[activeIndex];
      if (el) window.location.href = el.getAttribute("href");
    }
  });
  resultsBox && resultsBox.addEventListener("mousemove", function (e) {
    var a = e.target.closest(".search-result");
    if (!a) return;
    activeIndex = parseInt(a.getAttribute("data-i"), 10);
    Array.prototype.forEach.call(resultsBox.children, function (el, i) { el.classList.toggle("is-active", i === activeIndex); });
  });

  /* ---------------------------------------------------------- figure zoom */
  var zoom = null;
  function openZoom(src, alt) {
    if (!zoom) {
      zoom = document.createElement("dialog");
      zoom.className = "zoom";
      zoom.innerHTML = '<button class="zoom-close" type="button" aria-label="关闭">×</button><img alt="">';
      zoom.addEventListener("click", function (e) {
        if (e.target === zoom || e.target.classList.contains("zoom-close")) zoom.close();
      });
      document.body.appendChild(zoom);
    }
    var img = zoom.querySelector("img");
    img.src = src;
    img.alt = alt || "";
    zoom.showModal();
  }

  /* ---------------------------------------------------------- events */
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-action]");
    if (!t) {
      var link = e.target.closest("a.fig-link");
      if (link) { e.preventDefault(); openZoom(link.getAttribute("href"), link.querySelector("img").alt); }
      return;
    }
    var action = t.getAttribute("data-action");
    if (action === "theme") cycleTheme();
    else if (action === "font") cycleFont();
    else if (action === "print") window.print();
    else if (action === "top") window.scrollTo({ top: 0, behavior: "smooth" });
    else if (action === "menu") { if (body.classList.contains("nav-open")) closeNav(); else toggleNav(); }
    else if (action === "search") openSearch();
    else if (action === "search-close") closeSearch();
  });

  document.addEventListener("keydown", function (e) {
    var meta = e.metaKey || e.ctrlKey;
    if (meta && e.key.toLowerCase() === "k") { e.preventDefault(); modal.hidden ? openSearch() : closeSearch(); return; }
    if (e.key === "Escape") {
      if (!modal.hidden) closeSearch();
      if (body.classList.contains("nav-open")) closeNav();
      return;
    }
    if (e.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA") {
      e.preventDefault(); openSearch();
    }
  });

  // close mobile nav after jumping to a section
  document.querySelectorAll(".toc a").forEach(function (a) {
    a.addEventListener("click", function () { if (window.innerWidth <= 860) closeNav(); });
  });

  // initial scroll target
  window.addEventListener("load", function () {
    if (location.hash) {
      var el = document.getElementById(location.hash.slice(1));
      if (el) setTimeout(function () { el.scrollIntoView(); }, 30);
    }
  });

  onScroll();
})();
