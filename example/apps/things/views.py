from django.http import Http404
from django.core.paginator import Paginator, InvalidPage
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _

from example.apps.things.models import Thing


def _pagination(request, object_list):
    paginator = Paginator(object_list, 2, orphans=3, allow_empty_first_page=True)

    try:
        page = paginator.page(request.GET.get('page', 1))
    except InvalidPage:
        raise Http404(_(u'Invalid page number.'))

    return [paginator, page]


def thing_index(request):
    """
    Index / list view of things.

    Templates:
        :template:`things/thing_index.html`
    Context:
        thing_list
            A list of all :model:`things.Thing` objects.
        new_things
            A list of 5 of the newest :model:`things.Thing` objects.
        paginator
            A ``django.core.paginator.Paginator`` object for the things.
        page
            A ``django.core.paginator.Page`` object for the current page.
        is_paginated
            Boolean. True if there is more than one page. False otherwise.

    """

    thing_list = Thing.objects.all()

    paginator, page = _pagination(request, thing_list)

    new_things = thing_list.order_by('-created')[:5]

    context = {
        'thing_list': page.object_list,
        'new_things': new_things,
        'paginator': paginator,
        'page': page,
        'is_paginated': page.has_other_pages(),
    }

    return render(request, 'things/thing_index.html', context)


def thing_detail(request, slug):
    """
    A detail view of a thing.

    Templates:
        :template:`things/thing_detail.html`
    Context:
        thing
            A :model:`things.Thing` object.
        next_thing
            The alphabetically-next :model:`things.Thing` object.
        prev_thing
            The alphabetically-preceding :model:`things.Thing` object.

    """

    thing = get_object_or_404(Thing, slug=slug)

    # TODO tech: make next|prev_thing work.
    next_thing = thing
    prev_thing = thing

    context = {
        'thing': thing,
        'next_thing': next_thing,
        'prev_thing': prev_thing,
    }

    return render(request, 'things/thing_detail.html', context)
