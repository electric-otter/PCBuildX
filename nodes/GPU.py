import multiprocessing
import time
import asyncio
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
from numpy import int16
def task(n):
    time.sleep(1)
    return n * n

if __name__ == '__main__':
    start_time = time.time()
    
    # Serial processing
    serial_results = [task(i) for i in range(5)]
    print("Serial results:", serial_results)
    
    # Parallel processing
    with multiprocessing.Pool(processes=5) as pool:
        parallel_results = pool.map(task, range(5))
    print("Parallel results:", parallel_results)
    
    end_time = time.time()
    print("Total time:", end_time - start_time, "seconds")
async def tasks():
    print("Creating tasks...")
    asyncio.create_task()
  rasterized = features.rasterize(geom,
                                out_shape = raster.shape,
                                fill = 0,
                                out = None,
                                transform = raster.transform,
                                all_touched = False,
                                default_value = 1,
                                dtype = None)

# Plot raster
fig, ax = plt.subplots(1, figsize = (10, 10))
show(rasterized, ax = ax)
plt.gca().invert_yaxis()
