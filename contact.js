const contactForm = document.querySelector('#contact-form');

contactForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const fields = new FormData(contactForm);
  const subject = encodeURIComponent('Child Protection Force website enquiry');
  const body = encodeURIComponent(
    `Name: ${fields.get('name')}\r\nEmail: ${fields.get('email')}\r\n\r\n${fields.get('message')}`
  );
  window.location.href = `${contactForm.getAttribute('action')}?subject=${subject}&body=${body}`;
});
