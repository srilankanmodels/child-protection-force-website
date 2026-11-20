const donationForm = document.querySelector('#donation-form');

donationForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const fields = new FormData(donationForm);
  const details = Array.from(fields, ([label, value]) => value.trim() ? `${label}: ${value.trim()}` : '')
    .filter(Boolean);
  const subject = encodeURIComponent('Child Protection Force bank transfer confirmation');
  const body = encodeURIComponent(details.join('\r\n'));
  window.location.href = `${donationForm.getAttribute('action')}?subject=${subject}&body=${body}`;
});
