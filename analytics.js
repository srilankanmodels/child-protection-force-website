(() => {
  if (!['www.childprotectionforce.org', 'childprotectionforce.org'].includes(location.hostname)) return;

  const measurementId = 'G-QN2M1574V7';
  const consentKey = 'cpf-analytics-consent';
  const disableKey = 'ga-disable-' + measurementId;
  const preference = document.getElementById('analytics-preference');
  const dialog = document.createElement('dialog');
  dialog.setAttribute('aria-labelledby', 'analytics-title');
  dialog.innerHTML = '<form method="dialog"><h2 id="analytics-title">Analytics preferences</h2>' +
    '<p>Allow optional Google Analytics cookies to help Child Protection Force understand which pages people visit and how they find the site.</p>' +
    '<p><button value="declined">Decline</button> <button value="allowed">Allow analytics</button></p></form>';
  document.body.append(dialog);

  function loadAnalytics() {
    if (document.getElementById('cpf-google-tag')) return;
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }

    gtag('js', new Date());
    gtag('config', measurementId, {
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
      page_location: location.origin + location.pathname,
      page_referrer: document.referrer ? new URL(document.referrer).origin : '',
    });

    const tag = document.createElement('script');
    tag.id = 'cpf-google-tag';
    tag.async = true;
    tag.src = 'https://www.googletagmanager.com/gtag/js?id=' + measurementId;
    document.head.append(tag);
  }

  function applyPreference(value) {
    window[disableKey] = value !== 'allowed';
    if (value === 'allowed') loadAnalytics();
  }

  let saved;
  try {
    saved = localStorage.getItem(consentKey);
  } catch {
    // A blocked storage setting does not grant consent.
  }
  applyPreference(saved);

  preference.hidden = false;
  preference.addEventListener('click', () => {
    dialog.returnValue = '';
    dialog.showModal();
  });
  dialog.addEventListener('close', () => {
    if (!['allowed', 'declined'].includes(dialog.returnValue)) return;
    try {
      localStorage.setItem(consentKey, dialog.returnValue);
    } catch {
      // The choice still applies to this page.
    }
    applyPreference(dialog.returnValue);
  });
  if (saved === null) dialog.showModal();
})();
