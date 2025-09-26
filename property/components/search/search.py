from django_components import component

from livecomponents import CallContext, StatelessLiveComponent, command


@component.register("search")
class SearchComponent(StatelessLiveComponent):
    template_name = "search/search.html"

    @command
    def update_search(self, call_context: CallContext, search: str):
        call_context.parent.set_search_query(search=search)
