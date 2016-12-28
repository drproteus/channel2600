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

function addYoutubeEmbedLinks() {
  var youtubelinks = [].slice.call(document.querySelectorAll('a')).filter(function(el) {
    if (el.href.indexOf('youtu.be') !== -1 || el.href.indexOf('youtube') !== -1) {
      var id = el.href.split('/').slice(-1)[0];
      insertAfter(el, youtubeEmbedLink(id));
    }
  });
}

function youtubeEmbedLink(id) {
  var youtubeDiv = document.createElement('div');
  youtubeDiv.innerHTML = '<iframe width="560" height="315" src="https://www.youtube.com/embed/'+id+'" frameborder="0" allowfullscreen></iframe>';
  var embedlink = document.createElement('a');
  embedlink.classList.add('embed-link');
  embedlink.innerHTML = "[Embed]";
  embedlink.href = "#";
  embedlink.addEventListener('click', function(event) {
    event.preventDefault();
    insertAfter(embedlink, youtubeDiv);
    embedlink.remove();
  });
  return embedlink;
}


function insertAfter(element, after) {
  element.parentNode.insertBefore(after, element.nextSibling);
}

ready(initThumbnails);
ready(initReplyLinks);
ready(addYoutubeEmbedLinks);
