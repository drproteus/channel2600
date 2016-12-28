function ready(fn) {
  if (document.readyState != 'loading') {
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

function toggleThumbnail(event) {
  if (event.target.classList.contains('thumb-selected')) {
    event.target.classList.remove('thumb-selected');
    event.target.src = event.target.dataset['thumbUrl'];
  } else {
    event.target.classList.add('thumb-selected');
    event.target.src = event.target.dataset['fullUrl'];
  }
}

function initThumbnails() {
  document.querySelectorAll('.thumb').forEach(function(item) {
    item.addEventListener('click', toggleThumbnail);
  });
  console.log('foo');
}

function initReplyLinks() {
  document.querySelectorAll('.reply-to').forEach(function(item) {
    item.addEventListener('click', function(event) {
      console.log('kasdjlas');
      var replyId = event.target.dataset['postId'];
      document.querySelector('#id_body').value += ('\n>>' + replyId + '\n');
    });
  });
}

ready(initThumbnails);
ready(initReplyLinks);
