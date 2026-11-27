/* Applied Biostatistics games: aggregate engagement only; no answers or user IDs. */
(function () {
  'use strict';
  const ID = 'G-JB99Z9SHHJ';
  const live = location.hostname === 'yanivjb.github.io' && location.pathname.startsWith('/biostats-book/');
  const memory = Object.create(null);
  function send(name, data) {
    if (!live || window['ga-disable-' + ID]) return;
    try {
      let host = window;
      // Embedded games share the book's tag and its consent settings.
      if (window.parent !== window) {
        if (window.parent.location.origin !== location.origin) return;
        host = window.parent;
        if (host['ga-disable-' + ID] || typeof host.gtag !== 'function') return;
      }
      if (typeof host.gtag !== 'function') {
        host.dataLayer = host.dataLayer || [];
        host.gtag = function () { host.dataLayer.push(arguments); };
        host.gtag('js', new Date());
        host.gtag('config', ID, {send_page_view:false});
        const script = document.createElement('script');
        script.async = true;
        script.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID;
        document.head.append(script);
      }
      host.gtag('event', name, {...data, send_to:ID});
    } catch (_) { /* Analytics must never interrupt a puzzle. */ }
  }
  window.BiostatsEngagement = function (meta, action, help, terminal, token, priorHelp) {
    if (!live) return;
    try {
      const key = 'biostats-engagement-v1:' + meta.game_type + ':' + meta.puzzle_id;
      let r;
      try { r = JSON.parse(localStorage.getItem(key)); } catch (_) {}
      r = r || memory[key] || {started:false, ended:false, assisted:false};
      const save = () => { memory[key]=r; try {localStorage.setItem(key,JSON.stringify(r));} catch (_) {} };
      const emit = (event, extra={}) => send(event, {...meta, level_name:meta.game_type+':'+meta.puzzle_id, assisted:r.assisted?'yes':'no', ...extra});
      if (action === 'reset') { r={started:false,ended:false,assisted:false};save();return; }
      if (r.ended) return;
      if (action === 'end') {
        if (!r.started) return; // Do not backfill old completed boards on reload.
        r.ended=true;save();emit('level_end',{outcome:help,success:help==='solved'});return;
      }
      if (!r.started) {
        if (terminal) return;
        r.started=true;r.assisted=Boolean(priorHelp);save();emit('level_start');
      }
      if (action === 'requested') emit('game_help_requested',{help_type:help});
      if (action === 'earned') emit('game_help_earned',{help_type:help});
      if (action === 'used') {if(token!==undefined){r.tokens=r.tokens||{};if(r.tokens[help]===token)return;r.tokens[help]=token;}r.assisted=true;save();emit('game_help_used',{help_type:help});}
    } catch (_) {}
  };
})();
