const contactForm = document.querySelector('#contact-form');

contactForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const fields = new FormData(contactForm);
  const subject = encodeURIComponent(contactForm.dataset.subject || 'Child Protection Force website enquiry');
  const details = [`Name: ${fields.get('name')}`, `Email: ${fields.get('email')}`];
  if (fields.has('interest')) details.push(`Area of interest: ${fields.get('interest')}`);
  const phone = fields.get('phone')?.trim();
  if (phone) details.push(`Mobile or WhatsApp: ${phone}`);
  if (fields.get('availability')) details.push(`Availability: ${fields.get('availability')}`);
  const body = encodeURIComponent(details.join('\r\n') + '\r\n\r\n' + fields.get('message'));
  window.location.href = `${contactForm.getAttribute('action')}?subject=${subject}&body=${body}`;
});
