from enum import Enum

from django_components import component

from livecomponents import (
    CallContext,
    InitStateContext,
    LiveComponent,
    LiveComponentsModel,
    command,
)
from livecomponents.manager.execution_results import ParentDirty
from property.models import Property


class CardView(str, Enum):
    OVERVIEW = "overview"
    DETAIL = "detail"
    EDIT = "edit"


class CardState(LiveComponentsModel):
    view: CardView = CardView.OVERVIEW
    property: Property


@component.register("card")
class CardComponent(LiveComponent[CardState]):
    template_name = "card/card.html"

    def init_state(self, context: InitStateContext) -> CardState:
        return CardState(**context.component_kwargs)

    @command
    def show_detail(self, call_context: CallContext[CardState]) -> None:
        call_context.state.view = CardView.DETAIL

    @command
    def show_overview(self, call_context: CallContext[CardState]) -> None:
        call_context.state.view = CardView.OVERVIEW

    @command
    def show_edit(self, call_context: CallContext[CardState]) -> None:
        call_context.state.view = CardView.EDIT

    @command
    def delete_property(self, call_context: CallContext[CardState]):
        call_context.state.property.delete()
        call_context.state.view = CardView.OVERVIEW
        return ParentDirty()
