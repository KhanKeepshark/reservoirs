
from .models import TextFile, ChemistryData
import plotly.io as pio
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_reservoirs(reservoirs):
    reserv_list = {}
    for reserv in reservoirs:
        try:
            # txt plot data
            reserv_info={}
            text_file = TextFile.objects.filter(reservoir=reserv).first()
            if text_file:
                with text_file.file.open(mode='r') as file:
                    data = np.loadtxt(file, delimiter=',')
                    x_size = int(np.max(data[:, 0]))
                    y_size = int(np.max(data[:, 1]))
                    depth = np.zeros((y_size, x_size))
                    for i in range(data.shape[0]):
                        x, y, z = data[i]
                        depth[int(y)-1, int(x)-1] = z
                    # 2D
                    fig2D = go.Figure(data=go.Heatmap(z=depth))
                    fig2D.update_layout(title='2D Plot')
                    plot2D1_div = fig2D.to_html(full_html=False)
                    # 3D
                    fig3D = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])
                    fig3D.add_trace(go.Surface(z=depth), row=1, col=1)
                    fig3D.update_layout(
                        title='3D Plot',
                        scene=dict(
                            camera=dict(
                                eye=dict(x=-4, y=-4, z=0.8),
                                projection=dict(type='orthographic')
                            ),
                            aspectmode='manual',
                            aspectratio=dict(x=1, y=1, z=0.6)
                        )
                    )
                    plot3D2_div = fig3D.to_html(full_html=False)
                    reserv_info["2Dplot"] = plot2D1_div
                    reserv_info["3Dplot"] = plot3D2_div
            # chemistry data
            chemistryData = ChemistryData.objects.filter(reservoir = reserv)
            chemistry_info = {}
            if len(chemistryData) != 0:
                chemistry_info["data"] = chemistryData

                keys_to_keep = [key for key in chemistryData.first().__dict__.keys() if key not in ['id', '_state', 'reservoir_id']]
                model_fields = ChemistryData._meta.get_fields()
                names_to_keep = [field.verbose_name for field in model_fields if field.name not in ['id', '_state', 'reservoir']]
                chemistry_info["keys"] = keys_to_keep
                chemistry_info["names"] = names_to_keep
                reserv_info["chemistry"] = chemistry_info
            if len(list(chemistryData)) != 0:
                plot_divs = {}
                df = pd.DataFrame(list(chemistryData.values())).drop(['id', 'reservoir_id'], axis=1)
                for column in df.columns:
                    fig = px.line(df, x='uploaded_at', y=column, title=f'График изменений для {column}')
                    plot_div = pio.to_html(fig, full_html=False)
                    plot_divs[column] = plot_div
                chemistry_info["plots"] = plot_divs
            

            # final
            reserv_list[reserv.title] = reserv_info
        except TextFile.DoesNotExist:
            print(f"No ExcelFile found for Reservoir ID: {reserv}")
    
    return reserv_list