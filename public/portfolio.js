const nav = document.querySelector('#sections');
const menu = document.querySelector('.menu');
menu.hidden = false;
function closeMenu() {
  menu.setAttribute('aria-expanded', 'false');
}
menu.addEventListener('click', () => {
  menu.setAttribute('aria-expanded', String(menu.getAttribute('aria-expanded') !== 'true'));
});
nav.addEventListener('click', closeMenu);
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menu.focus();
  }
});
const clock = document.querySelector('#clock');
const formatter = new Intl.DateTimeFormat('en-IN', {
  timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit', hour12: true
});
function updateTime() {
  clock.textContent = ' · ' + formatter.format(new Date()) + ' IST';
}
updateTime();
setInterval(updateTime, 15000);

const links = [...nav.querySelectorAll('a')];
const sections = [...document.querySelectorAll('main > section')];
function highlightSection() {
  const active = sections.filter(section => section.getBoundingClientRect().top < innerHeight * .45).pop();
  for (const link of links) {
    if (active && link.hash === '#' + active.id) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
}
addEventListener('scroll', highlightSection, { passive: true });
highlightSection();

const email = document.querySelector('.email-link').href.slice(7);
const copy = document.querySelector('#copy');
if (navigator.clipboard) {
  copy.hidden = false;
  copy.addEventListener('click', async () => {
    const status = document.querySelector('#copy-status');
    try {
      await navigator.clipboard.writeText(email);
      status.textContent = 'Email address copied.';
    } catch {
      status.textContent = 'Select the address above to copy it.';
    }
  });
}
const draft = document.querySelector('#draft');
draft.hidden = false;
const { sender, reply, message } = draft.elements;
message.addEventListener('input', () => {
  document.querySelector('#count').textContent = message.value.length + ' / 2000';
});
draft.addEventListener('submit', event => {
  event.preventDefault();
  const subject = encodeURIComponent('Portfolio enquiry from ' + sender.value);
  const body = encodeURIComponent(message.value + '\n\n' + sender.value + '\n' + reply.value);
  location.href = 'mailto:' + email + '?subject=' + subject + '&body=' + body;
});
