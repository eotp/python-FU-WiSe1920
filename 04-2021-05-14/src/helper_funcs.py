'''
Helper functions for data science workshop
'''

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
    
def cuteplot(gpd_df, crs="Mollweide", title=None, kdp=False, map_extend=(-27, 45, 33, 73.5), bw=0.2):
    '''
    Function to leverage the cartopy library to plot geographical data
    '''
    # map projections
    proj = {"PlateCarree": ("+proj=eqc +lat_ts=0 +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs",
                            ccrs.PlateCarree()),
            "Mollweide": ("+proj=moll +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs",
                          ccrs.Mollweide()),
            "Robinson": ("+proj=robin +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs",
                         ccrs.Robinson()),
            "UTM32N": ("+proj=utm +zone=32 +ellps=intl +units=m +no_defs",
                       ccrs.EuroPP()),
            "Orthographic": ("+proj=ortho", ccrs.Orthographic())
            }

    # plot figure
    fig = plt.figure()
    ax = plt.axes(projection=proj.get(crs)[1])
    # add features
    ax.coastlines(resolution='50m')
    ax.stock_img()
    countries = cfeature.NaturalEarthFeature(category='cultural',
                                             name='admin_0_boundary_lines_land',
                                             scale='50m',
                                             facecolor='none',
                                             edgecolor="black")
    ax.add_feature(countries)

    # extend
    ax.set_extent(map_extend)
    # plot geopandas data frame
    if crs != "PlateCarree":
        gpd_df = gpd_df.to_crs(proj.get(crs)[0])

    if kdp:
        kdp_germany = sns.kdeplot(gpd_df['Target Longitude'],
                                  gpd_df['Target Latitude'],  # y-axis
                                  cmap="viridis",
                                  shade=True,
                                  shade_lowest=False,
                                  bw=bw,
                                  transform = ccrs.PlateCarree()
                                  )
        kdp_germany.plot()
    else:
        gpd_df.plot(ax=ax, marker='o', color='red',
             markersize=5, alpha=0.01)
    # add gridlines
    ax.gridlines()

    if title is not None:
        ax.set_title(title, size=16)
    plt.tight_layout()

