from django_components import component

from livecomponents import (
    CallContext,
    InitStateContext,
    LiveComponent,
    LiveComponentsModel,
    command,
)

from property.components.forms import PropertyForm


class EditState(LiveComponentsModel):
    form: PropertyForm


@component.register("edit")
class EditComponent(LiveComponent[EditState]):
    template_name = "edit/edit.html"

    def init_state(self, context: InitStateContext) -> EditState:
        return EditState(
            form=PropertyForm(instance=context.component_kwargs.get("property")),
        )

    @command
    def save_property(
        self, call_context: CallContext[EditState], **form_data: dict
    ) -> None:
        form = PropertyForm(data=form_data, instance=call_context.state.form.instance)
        if form.is_valid():
            updated_property = form.save()
            call_context.state.form = PropertyForm(instance=updated_property)
            call_context.parent.show_overview()
        else:
            call_context.state.form = form
