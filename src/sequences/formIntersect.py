from shapely.geometry import Polygon

figure1 = Polygon([(0,0),(0,1),(1,1),(1,0)])
figure2 = Polygon([(2,2),(2,3),(3,3)])

print(figure1.intersects(figure2))