from shiny import App, render, ui

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_slider("n", "Number of observations", min=1, max=100, value=50),
    ),
    ui.card(
        ui.output_text("build"),
    ),
    ui.card(
        ui.output_text("txt"),
    ),
    title="Minimal Shiny App - Dev branch",
)


def server(input, output, session):
    @render.text
    def build():
        return f"Updated preview"
    @render.text
    def txt():
        return f"Number of observations: {input.n()}"


app = App(app_ui, server)
