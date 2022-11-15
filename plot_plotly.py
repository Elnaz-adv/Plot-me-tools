from plotly.graph_objs import Layout
from plotly import offline
import json

class Plotly_Plotter:
    def __init__(self,filename):
        self.filename = filename

    def read_json_file(self):
        with open(self.filename) as f:
            all_eq_data = json.load(f)
            all_eq_dicts = all_eq_data['features']

        mags, lons, lats, hover_texts = [], [], [], []
        for eq_dict in all_eq_dicts:
            mag = eq_dict['properties']['mag']
            lon = eq_dict['geometry']['coordinates'][0]
            lat = eq_dict['geometry']['coordinates'][1]
            title = eq_dict['properties']['title']
            mags.append(mag)
            lons.append(lon)
            lats.append(lat)
            hover_texts.append(title)

        # Map the earthquakes.
        data = [{
            'type': 'scattergeo',
            'lon': lons,
            'lat': lats,
            'text': hover_texts,
            'marker': {
                'size': [5 * mag for mag in mags],
                'color': mags,
                'colorscale': 'Viridis',
                'reversescale': True,
                'colorbar': {'title': 'Magnitude'},
            },
        }]
        return data

    def plot_json_plotly(self, data):
        my_layout = Layout(title='Global Earthquakes')
        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename='global_earthquakes.html')



if __name__ == "__main__":
        filename = 'eq_data_1_day_m1.json'
        plotly = Plotly_Plotter(filename)
        read_data = plotly.read_json_file()
        plot_data = plotly.plot_json_plotly(read_data)


