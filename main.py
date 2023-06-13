__author__ = 'Arnold C. Toppo'

# from dash import Dash, html, dcc
#
# app = Dash(__name__)
# # Geometry Options
# app.layout = html.Div([
#     dcc.Dropdown([
#         'Monolith',
#         'Spiral Sheet',
#         'Spiral Corrugation',
#         'Stacked Sheets',
#         'Stacked Corrugations',
#         'Folded Sheets',
#         'Folded Corrugations'
#     ],
#         'Monolith')
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)


import geometry_properties
import material_properties

geometry = 'Corrugated Monolith'

if geometry == 'Spiral':
    variable = SpiralGeom(inner_diam, outer_diam, sheet_width, sheet_thickness, sheet_gap)
    geometry_properties = geometry_properties.SpiralGeom(1,10,5,0.1,0.1)
    volume = a.spiral_volume()
elif geometry == 'Spiral Corrugation':
    # volume ==
elif geometry == 'Stacked Sheets':
# volume ==
elif geometry == 'Stacked Corrugation':
# volume ==
elif geometry == 'Folded Sheets':
volume == a.material_volume()
elif geometry == 'Folded Corrugation':
# volume ==
elif geometry == 'Monolith':
# volume ==
else:
    print('Invalid geometry.')