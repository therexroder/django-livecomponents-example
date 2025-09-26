from typing import Any

from django_components import component

from livecomponents import (
    CallContext,
    ExtraContextRequest,
    InitStateContext,
    LiveComponent,
    LiveComponentsModel,
    command,
)
from property.models import Property


class GridState(LiveComponentsModel):
    search_query: str = ""


@component.register("grid")
class GridComponent(LiveComponent[GridState]):
    template_name = "grid/grid.html"

    def init_state(self, context: InitStateContext) -> GridState:
        return GridState(**context.component_kwargs)

    def get_extra_context_data(
        self, extra_context_request: ExtraContextRequest[GridState]
    ) -> dict[str, Any]:
        state = extra_context_request.state
        if state.search_query:
            properties = Property.objects.filter(title__icontains=state.search_query)
        else:
            properties = Property.objects.all()
        return {
            "properties": properties,
        }

    @command
    def set_search_query(
        self, call_context: CallContext[GridState], search: str
    ) -> None:
        call_context.state.search_query = search
