import ursina

mitSpil = ursina.Ursina()

#minVæg1 = ursina.Entity(model = "quad", doublesided = True,scale_x = 20, scale_y = 20)
#minVæg1.x = 0
#minVæg1.y = 0
#minVæg1.z = 20
def væg():
    minVæg2 = ursina.Entity(model = "wireframe_cube",scale_x = 50, scale_y = 50, scale_z = 50)
    minVæg2.x = 0
    minVæg2.y = 0
    minVæg2.z = 100

mitSpil.run()

