# Andre Driedger 1805536
# Generates a sphere obj file with radius 1

from math import *

n = 32 #vertices along equator
m = 16 #vertices pole to pole
vertices = []

def gen_vertices():

    vertices.append((0, 1, 0)) #north pole
    vertices.append((0, -1, 0)) #south pole
    ele_agl = (pi)/m #180 from top to bottom
    azm_agl = (2*pi)/n #360 clockwise from (1, 0, 0)
    for i in range(0, n):
        theta = azm_agl*i
        for j in range(1, m):
            phi = ele_agl*j
            #parametric coordinates
            x = cos(theta)*sin(phi)
            y = cos(phi) #cos of the discretized elevation angle
            z = sin(theta)*sin(phi)
            vertices.append((x, y, z))

gen_vertices()
faces = []

def gen_faces():

    #top and bottom triangles
    faces.append((1, (3+15*31), 3))
    faces.append((2, (17+15*31), 17))
    for i in range(0, n-1):
        a = 1 #north pole
        b = 3+(15*i)
        c = b+15
        faces.append((a, b, c))
        a = 2 #south pole
        b = 17+(15*i)
        c = b+15
        faces.append((a, b, c))
        
        #quads
        for j in range(0, m-2):
            a = 3+j+(15*i)
            b = a+1
            c = b+15
            d = a+15
            faces.append((a, b, c))
            faces.append((a, c, d))
    for j in range(0, m-2):
        a = 3+j+(15*31)
        b = a+1
        c = 3+j+1
        d = 3+j
        faces.append((a, b, c))
        faces.append((a, c, d))

gen_faces()

objFile = open("sphere.obj", "w")
for v in vertices:
    objFile.write("v ")
    for a in v:
        objFile.write(format(a, ".2f") + " ") #output to a precision of 2
    objFile.write("\n")

for f in faces:
    objFile.write("f ")
    for a in f:
        objFile.write(str(a) + " ")
    objFile.write("\n")

