from django.utils.translation import ugettext_lazy as _

__all__ = (
    'SLIDER_TOOLTIP_SHOW',
    'SLIDER_TOOLTIP_HIDE',
    'SLIDER_TOOLTIP_ALWAYS',
    'SLIDER_DEFAULT_TOOLTIP',
    'SLIDER_TOOLTIP_CHOICES',

    'SLIDER_HANDLE_ROUND',
    'SLIDER_HANDLE_SQUARE',
    'SLIDER_HANDLE_TRIANGLE',
    'SLIDER_HANDLE_CUSTOM',
    'SLIDER_HANDLE_CHOICES',
)

SLIDER_TOOLTIP_SHOW = 'show'
SLIDER_TOOLTIP_HIDE = 'hide'
SLIDER_TOOLTIP_ALWAYS = 'always'
SLIDER_DEFAULT_TOOLTIP = SLIDER_TOOLTIP_HIDE

SLIDER_TOOLTIP_CHOICES = (
    (SLIDER_TOOLTIP_SHOW, _("Show")),
    (SLIDER_TOOLTIP_HIDE, _("Hide")),
    (SLIDER_TOOLTIP_ALWAYS, _("Always")),
)

SLIDER_HANDLE_ROUND = 'round'
SLIDER_HANDLE_SQUARE = 'square'
SLIDER_HANDLE_TRIANGLE = 'triangle'
SLIDER_HANDLE_CUSTOM = 'custom'
SLIDER_DEFAULT_HANDLE = SLIDER_HANDLE_ROUND
SLIDER_HANDLE_CHOICES = (
    (SLIDER_HANDLE_ROUND, _("Round")),
    (SLIDER_HANDLE_SQUARE, _("Square")),
    (SLIDER_HANDLE_TRIANGLE, _("Triangle")),
    (SLIDER_HANDLE_CUSTOM, _("Custom")),
)