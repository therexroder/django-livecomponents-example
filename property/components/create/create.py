from typing import Any

from django_components import component

from livecomponents import (
    CallContext,
    InitStateContext,
    LiveComponent,
    LiveComponentsModel,
    command,
)
from livecomponents.manager.execution_results import ParentDirty

from property.components.forms import PropertyForm


class CreateState(LiveComponentsModel):
    is_open: bool = False
    form: PropertyForm


@component.register("create")
class CreateComponent(LiveComponent[CreateState]):
    template_name = "create/create.html"

    def init_state(self, context: InitStateContext) -> CreateState:
        return CreateState(is_open=False, form=PropertyForm())

    @command
    def toggle_form(self, call_context: CallContext[CreateState]) -> None:
        call_context.state.is_open = not call_context.state.is_open
        call_context.state.form = PropertyForm()

    @command
    def save_property(self, call_context: CallContext[CreateState], **form_data: Any):
        form = PropertyForm(data=form_data)
        if form.is_valid():
            form.save()
            call_context.state.form = PropertyForm()
            call_context.state.is_open = False
            return ParentDirty()

        call_context.state.form = form
