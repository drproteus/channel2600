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
