import json
import matplotlib.pyplot as plt


class plotScatter:

    def __init__(self,filename):
        self.filename = filename 

    def read_json_file(self):
        with open(self.filename) as f:
            all_eq_data = json.load(f)
        all_eq_dicts = all_eq_data['features']             

        mags, plas, lons, lats = [], [], [], []
        for eq_dict in all_eq_dicts:  
            mag = eq_dict['properties']['mag']  
            pla = eq_dict['properties']['place']  
            lon = eq_dict['geometry']['coordinates'][0]   
            lat = eq_dict['geometry']['coordinates'][1]
            mags.append(mag)
            plas.append(pla)
            lons.append(lon)
            lats.append(lat)
        return mags,plas,lons,lats

    def plot_json(self,mags,plas,lons,lats):
        scaled_mags = [entry ** 2 * 10 for entry in mags]  # List comprehension

        fig, ax = plt.subplots()
        scatter = ax.scatter(lons, lats, marker="o", color="C3", s=scaled_mags,
                     label="eqs magnitude", edgecolors="w", linewidth=1,
                     alpha=0.75)
        fig.legend()
        fig.suptitle("suptitle", x = 0.5,y = 0.97)
        ax.grid()
        ax.set_xlabel("longitude")
        ax.set_ylabel("latitude")
        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.tick_params(axis="both", which="minor", labelsize=10)
        plt.show()


filename = 'eq_data_1_day_m1.json'
plotS = plotScatter(filename)
mags,plas,lons,lats = plotS.read_json_file()
plotS.plot_json(mags,plas,lons,lats)

