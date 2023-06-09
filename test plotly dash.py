import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Create a Dash app
app = dash.Dash(__name__)


# Define a class for the app layout
class MyAppLayout:
    def __init__(self):
        self.layout = html.Div(
            children=[
                html.H1("Shape Calculator"),
                html.Div(
                    children=[
                        html.Label("Number of Sides:"),
                        dcc.Input(
                            id="num-sides-input",
                            type="number",
                            value=3,
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Label("Side Length:"),
                        dcc.Input(
                            id="side-length-input",
                            type="number",
                            value=1,
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Button("Calculate", id="calculate-button"),
                    ],
                ),
                html.Div(id="output-div"),
            ],
        )


# Define a class for the app callbacks
class MyAppCallbacks:
    @staticmethod
    @app.callback(
        Output("output-div", "children"),
        [Input("calculate-button", "n_clicks")],
        [State("num-sides-input", "value"), State("side-length-input", "value")],
    )
    def calculate_area(n_clicks, num_sides, side_length):
        if n_clicks is None:
            return ""

        # Perform the area calculation based on the inputs
        # You can replace this with your own calculation logic
        area = 0.5 * num_sides * side_length ** 2

        # Return the output message
        return f"The area is: {area}"


# Create instances of the layout and callbacks classes
layout = MyAppLayout().layout
callbacks = MyAppCallbacks()

# Run the app
if __name__ == "__main__":
    app.layout = layout
    app.run_server(debug=True)
