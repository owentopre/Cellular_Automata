import math

from tracemalloc import start
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import random
#from Gravity1.0 import gravity

# Fixing random state for reproducibility
np.random.seed(19680801)



#make initial number of random cells
#give initial inertia
#pass these values through gravity1.0
#display results

#space size (mxmxm cube):
m = 10
#maximuminitial speed
maxspeed = 10
#number of starting particles:
startno = 10
particles = []
velocity = []

for a in range (startno):
    particles.append((random.randint(0, m),random.randint(0, m),random.randint(0, m)))
    
for b in range (startno):
    velocity.append((random.randint(0, maxspeed),random.randint(0, maxspeed),random.randint(0, maxspeed)))
    
#for k in range(3):
    #print(k)    

#show a point at 0,0,0

#print(particles)
#print(velocity[0])

#print(velocity[0])

def RoundU(number, div):
    return number//div + number%div>0

def ceildiv(a, b):
    return -(a // -b)

def Gravity(Data, InitialInertia):          # Data is a list like [[x1, y1, z1], [x2, y2, z2], ...] with each cells x,y,z coord?
    GridLength = [10, 10, 10]               # Grid x, y, z coordinates
    Cells = len(Data)
    radius = 5                              # radius of which the gravity will affect
    for i in range(3):                      # A quick fix to prevent the function breaking for Grid > gravity's influence
        if radius > GridLength[i]:
            radius = GridLength[i]
    apc = radius                            # Acceleration Per Cell mass
    NewGrid = []
    Grid = Data
    Vel = InitialInertia
    Vel2 = []

    d = RoundU(radius, 2)
    for i in range(Cells):                  # Finding the acceleration of each cell
        for k in range(Cells):
            if i != k:
                x = Grid[i][0] - Grid[k][0]
                y = Grid[i][1] - Grid[k][1]
                z = Grid[i][2] - Grid[k][2]
                r = math.sqrt((x**2)*(y**2)*(z**2))
                if r <= radius:
                    v1 = Vel[i][0]
                    v2 = Vel[i][1]
                    v3 = Vel[i][2]
                    #print(Vel)
                    #print(Vel[1][1])
                    #print(Vel[i][0])
                    #print(i,k)
                    if x != 0: 
                        v1 += (radius + 1 - abs(x)) * ceildiv(apc,radius) * (abs(x)/x)
                    if y != 0: 
                        v2 += (radius + 1 - abs(y)) * ceildiv(apc,radius) * (abs(y)/y)
                    if z != 0: 
                        v3 += (radius + 1 - abs(z)) * ceildiv(apc,radius) * (abs(z)/z)
                        
                    Vel2.append([int(v1),int(v2),int(v3)])
                    #print(Vel2)
                    Vel = Vel2
                    
    NextTo = []
    for i in range(Cells):
        Size = 0
        Direc = [0, 0]
        for k in range(3):
            #print(k)
            if abs(Vel[i][k]) > Size:      # Finding which direction the cell will move
                Size = Vel[i][k]
                #print(Direc)
                Direc[0] = k
                #print(Direc)
                if Vel[i][k] > 0: 
                    Direc[1] = 1
                else: 
                    Direc[1] = -1
        flag = False
        for k in range(Cells):             # Searches for possible collisions
            for l in range(Vel[i][Direc[0]]):
                if Grid[i][Direc[0]]+(Direc[1]*l) == Grid[k]:
                    NextTo.append([i, Direc])
                    flag = True
                    break
            if flag:
                NewGrid.append(Grid[i])
                break
                
        if not flag:    # Cells which don't collide are moved
                temp = []
                for a in range(3):
                    if Direc[0] == a:
                        temp.append(Grid[i][Direc[0]] + Vel[i][Direc[0]])
                    else:
                        temp.append(Grid[i][a])            
                NewGrid.append(temp)
                
                

    Grid = NewGrid
    for i in range(len(NextTo)):            # Moves cells which do collide. Collisions are elastic (like snooker balls)
        flag = [False, radius, 0]
        for k in range(Cells):             # Checks which previous collions no longer happen
            if flag[0]: break
            for l in range(Vel[NextTo[i][0]][NextTo[i][1][0]]):
                if Grid[NextTo[i][0]][NextTo[i][1][0]]+(NextTo[i][1][1]*iii) == Grid[k]:
                    if l < flag[1]:
                        flag[1] = l
                        flag[2] = k
                    if l==0: flag[0] = True
                    break
        if flag[1]==0:                      # Cells directly next to another in the direction of motion transfer all inertia
            Vel[flag[2]][NextTo[i][1][0]] += Vel[NextTo[i][0]][NextTo[i][1][0]]
            Vel[NextTo[i][0]][NextTo[i][1][0]] -= Vel[NextTo[i][0]][NextTo[i][1][0]]
        else:                               # Otherwise they move to where the collions occurs then transfers all remaining inertia
            NewGrid[NextTo[i][0]][NextTo[i][1][0]] = Grid[NextTo[i][0]][NextTo[i][1][0]] + (flag[1]-1)*NextTo[i][1][1]
            Vel[NextTo[i][0]][NextTo[i][1][0]] -= (flag[1]-1)*NextTo[i][1][1]
            Vel[flag[2]][NextTo[i][1][0]] += (flag[1]-1)*NextTo[i][1][1]
    ReturnGrid = []
    for i in range(3*len(NewGrid))
        ReturnGrid.append(NewGrid[i%len(NewGrid)][i//len(NewGrid)]
    #return ReturnGrid                      
    return NewGrid, Vel

fig = plt.figure()
ax = p3.Axes3D(fig)

dataPoint = Gravity(particles, velocity)
print(dataPoint)
print(dataPoint[0][1][0])
points = [ax.plot((dataPoint[0][i][0]), (dataPoint[0][i][1]), (dataPoint[0][i][2]))[0] for [i] in range(dataPoint[0])]

#print(test)

def Gen_RandLine(length, dims=2):
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    lineData = np.empty((dims, length))
    lineData[:, 0] = np.random.rand(dims)
    for index in range(1, length):
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = ((np.random.rand(dims) - 0.5) * 0.1)
        lineData[:, index] = lineData[:, index - 1] + step

    return lineData


def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

# Attaching 3D axis to the figure


# Fifty lines of random 3-D lines
data = [Gen_RandLine(25, 3) for index in range(50)]


# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
print([(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data])
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
#print(lines)

# Setting the axes properties
ax.set_xlim3d([0.0, m])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, m])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, m])
ax.set_zlabel('Z')

ax.set_title('3D Test')
'''
# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
                                   interval=50, blit=False)
'''
line_ani = animation.FuncAnimation(fig, Gravity, 25, fargs=(dataPoint, points),
                                   interval=50, blit=False)

#print(data)

plt.show()
