function ready(fn) {
  if (document.readyState != 'loading') {
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

function toggleThumbnail(event) {
  event.target.classList.toggle('thumb-selected');
}

function initThumbnails() {
  document.querySelectorAll('.thumb').forEach(function(item) {
    item.addEventListener('click', toggleThumbnail);
  });
  console.log('foo');
}

ready(initThumbnails)
