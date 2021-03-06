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
}

function initReplyLinks() {
  document.querySelectorAll('.reply-to').forEach(function(item) {
    item.addEventListener('click', function(event) {
      document.querySelector('.reply-form').classList.remove('hidden');
      var replyId = event.target.dataset['postId'];
      if (replyId) {
        document.querySelector('#id_body').value += ('>>' + replyId + '\n');
        focusPost(replyId);
      }
    });
  });
}

function hideReplyForm() {
  document.querySelector('.reply-form').classList.add('hidden');
}

function addEmbedLinks() {
  addSoundcloudEmbedLinks();
  addYoutubeEmbedLinks();
}

function addSoundcloudEmbedLinks() {
  var soundcloudlinks = [].slice.call(document.querySelectorAll('a')).filter(function(el) {
    if (!el.classList.contains('embed-link') && !el.classList.contains('embedded')) {
      if (el.href.indexOf('soundcloud') !== -1) {
        var href = el.href;
        insertAfter(el, soundcloudEmbedLink(href));
        el.classList.add('embedded');
      }
    }
  });
}

function soundcloudEmbedLink(href) {
  var soundcloudDiv = document.createElement('div');
  soundcloudDiv.innerHTML = '<iframe width="560" height="460" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url='+href+'&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true"></iframe>';
  var embedlink = document.createElement('a');
  embedlink.classList.add('embed-link');
  embedlink.innerHTML = "[Embed]";
  embedlink.href = "#";
  embedlink.addEventListener('click', function(event) {
    event.preventDefault();
    insertAfter(embedlink, soundcloudDiv);
    embedlink.remove();
  });
  return embedlink;
}

function addYoutubeEmbedLinks() {
  var youtubelinks = [].slice.call(document.querySelectorAll('a')).filter(function(el) {
    if (!el.classList.contains('embed-link') && !el.classList.contains('embedded')) {
      var startAt = '';
      var link = '';
      var timeIndex = el.href.indexOf('?t=');
      if (timeIndex !== -1) {
        startAt = '?t='+el.href.split('?t=').slice(-1)[0];
        link = el.href.slice(0, timeIndex);
      } else {
        link = el.href;
      }
      if (link.indexOf('youtu.be') !== -1) {
        var id = link.split('/').slice(-1)[0]+startAt;
        insertAfter(el, youtubeEmbedLink(id));
        el.classList.add('embedded');
      } else if (link.indexOf('youtube') !== -1) {
        var id = el.href.split('=').slice(-1)[0]+startAt;
        insertAfter(el, youtubeEmbedLink(id));
        el.classList.add('embedded');
      }
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

function expandThread(id) {
  var embedThread = document.querySelector('#thread-embed-'+id);
  if (embedThread) {
    embedThread.classList.toggle('hidden');
  } else {
    var request = new XMLHttpRequest();
    request.open('GET', '/thread/'+id+'/posts/', true);
    request.onload = function() {
      if (request.status >= 200 && request.status < 400) {
        var embedDiv = document.createElement('div');
        embedDiv.classList.add('thread-embed');
        embedDiv.id = 'thread-embed-'+id;
        embedDiv.innerHTML = request.responseText;
        embedDiv.querySelectorAll('code').forEach(function(el) {
          hljs.highlightBlock(el);
        });
        var parent = document.querySelector('#thread-'+id+' .thread-op');
        insertAfter(parent, embedDiv);
        initThumbnails();
        addEmbedLinks();
      } else {
      }
    }
    request.send();
  }
  var expandLink = document.querySelector('#thread-'+id+' .expand-thread');
  if (expandLink.innerHTML === '+') {
    expandLink.innerHTML = '-';
  } else {
    expandLink.innerHTML = '+';
  }
}

function expandPost(id) {
  var bodyDiv = document.querySelector('#post-'+id+' .post-body');
  var request = new XMLHttpRequest();
  request.open('GET', '/post/'+id+'/', true);
  request.onload = function() {
    if (request.status >= 200 && request.status < 400) {
      bodyDiv.innerHTML = request.responseText;
      addEmbedLinks();
      bodyDiv.querySelectorAll('code').forEach(function(el) {
        hljs.highlightBlock(el);
      });
    } else {
    }
  }
  request.send();
}

function insertAfter(element, after) {
  element.parentNode.insertBefore(after, element.nextSibling);
}

function focusPostOnHash() {
  var postId = location.hash.slice(1);
  if (postId !== 'reply-form')
    focusPost(postId);
}

function focusPost(postId) {
  document.querySelectorAll('.post').forEach(function(el) {
    el.classList.remove('focused');
  });
  try {
    console.log(postId);
    document.querySelector('.post#post-'+postId).classList.add('focused');
  }
  catch (e) {
  }
}

ready(initThumbnails);
ready(initReplyLinks);
ready(addEmbedLinks);
ready(focusPostOnHash);
ready(hljs.initHighlighting);
window.addEventListener("hashchange", focusPostOnHash);
