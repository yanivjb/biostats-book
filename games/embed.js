// Size each chapter card embed to its contents; accept messages only from its iframe.
(() => {
 if (window.biostatsCardEmbedsReady) return;
 window.biostatsCardEmbedsReady = true;
 window.addEventListener('message', event => {
  if (event.origin !== window.location.origin || event.data?.type !== 'biostats-cards-height') return;
  const height = Number(event.data.height);
  if (!Number.isFinite(height) || height < 100 || height > 2000) return;
  for (const frame of document.querySelectorAll('iframe[data-chapter-games]')) {
   if (frame.contentWindow === event.source) frame.style.height = Math.ceil(height + 4) + 'px';
  }
 });
})();
