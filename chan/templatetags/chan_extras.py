from django import template
import markdown

register = template.Library()

@register.filter
def markdownify(text):
    return markdown.markdown(text, safe_mode='escape',
            extensions=['markdown.extensions.nl2br',
                        'markdown.extensions.fenced_code',
                        'urlize',
                    ])
