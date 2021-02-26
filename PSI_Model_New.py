#Script to obtain the axial and lateral soil resistance (Tu & Pu) for different parameter range.

from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *


import math

diameter = 0.06
height = [0.6]
unit_weight = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
phi = [34]
ko = 0.42
f = 0.60
nqh = [18]     # Bearing capacity factor can be obtained from a graph. So need to input it manually.
Tu = 0

res = [[i, j, k] for i in height
       for j in unit_weight
       for k in phi]

for item in res:
    print(item)
for i in height:
    print('H/D= ')
    print(i/diameter)
for item in res:
    print('[Depth, Unit weight, Friction angle] ')
    print(item)
    if (item[1] < 13):
        pu_temp = 1000 * diameter * item[1] * item[0]
        for i in nqh:
            Pu = 0.80431 * pu_temp * i
            print('Pu: ')
            print(Pu)                                     #Equation of Tu & Pu were modified based on the current study requirements.

    if (item[1] >= 13):
        pu_temp = 1000 * diameter * item[1] * item[0]
        for i in nqh:
            Pu = 1.17203 * pu_temp * i
            print('Pu: ')
            print(Pu)
    Tu = 7.78586 * math.pi * 1000 * diameter * item[1] * item[0] * (1 + ko) / 2 * math.tan(math.radians(f * item[2]))
    print('Tu: ')
    print(Tu)
    Tu_value=[Tu]
    Pu_value=[Pu]
    Tu_Pu=[[l,m] for l in Tu_value
           for m in Pu_value]

    start=1
    for value in Tu_Pu:
        Axial = value[0]
        Lateral = value[1]



       

           
        #start=1
        Max_iterations=3      #Need to select based on the parameters combination (3 means number of job will be 2)

        for q in range (start,Max_iterations):



            #Parts


            mdb.Model(modelType=STANDARD_EXPLICIT, name='Model-%d' %(q))

            mdb.models['Model-%d' %(q)].ConstrainedSketch(name='__profile__', sheetSize=1.8)    #Length of the pipe = 1.8m
            mdb.models['Model-%d' %(q)].sketches['__profile__'].Spot(point=(-0.9, 0.0))
            mdb.models['Model-%d' %(q)].sketches['__profile__'].Spot(point=(0.9, 0.0))
            mdb.models['Model-%d' %(q)].sketches['__profile__'].Line(point1=(-0.9, 0.0), point2=(
                0.9, 0.0))
            mdb.models['Model-%d' %(q)].sketches['__profile__'].HorizontalConstraint(
                addUndoState=False, entity=
                mdb.models['Model-%d' %(q)].sketches['__profile__'].geometry[2])
            mdb.models['Model-%d' %(q)].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
                DEFORMABLE_BODY)
            mdb.models['Model-%d' %(q)].parts['Part-1'].BaseWire(sketch=
                mdb.models['Model-%d' %(q)].sketches['__profile__'])
            del mdb.models['Model-%d' %(q)].sketches['__profile__']
            mdb.models['Model-%d' %(q)].PipeProfile(formulation=THICK_WALL, name='Profile-1', r=
                0.03015, t=0.0055)     # Radius and thickness of 60 mm MDPE pipe



            #Material Definition


            mdb.models['Model-%d' %(q)].Material(name='Material-1')
            mdb.models['Model-%d' %(q)].materials['Material-1'].Density(table=((940.0, ), ))  #Density of MDPE pipe = 940 kg/m3
            mdb.models['Model-%d' %(q)].materials['Material-1'].Elastic(table=((566278000.0,  #Elastic & Plastic property at strain rate 10^-4
                0.45), ))
            mdb.models['Model-%d' %(q)].materials['Material-1'].Plastic(table=((1700000.0, 0.0), 
                (3840000.0, 0.00221425), (4740000.0, 0.00363808), (5500000.0, 0.00528401), 
                (6170000.0, 0.00710818), (6750000.0, 0.00907757), (7270000.0, 0.0111668), (
                7730000.0, 0.0133562), (8140000.0, 0.0156301), (8510000.0, 0.0179759), (
                8840000.0, 0.0203834), (9150000.0, 0.0228443), (9430000.0, 0.0253516), (
                9680000.0, 0.0278998), (9920000.0, 0.0304837), (10100000.0, 0.0330995), (
                10300000.0, 0.0357435), (10500000.0, 0.0384128), (10700000.0, 0.0411047), (
                10900000.0, 0.043817), (11000000.0, 0.0465478), (11200000.0, 0.0492953), (
                11300000.0, 0.052058), (11400000.0, 0.0548346), (11500000.0, 0.0576239), (
                11700000.0, 0.0604248), (11800000.0, 0.0632364), (11900000.0, 0.0660579), (
                12000000.0, 0.0688885), (12000000.0, 0.0717276), (12100000.0, 0.0745744), (
                12200000.0, 0.0774285), (12300000.0, 0.0802894), (12400000.0, 0.0831565), (
                12400000.0, 0.0860296), (12500000.0, 0.0889081), (12600000.0, 0.0917918), (
                12600000.0, 0.0946803), (12700000.0, 0.0975734), (12800000.0, 0.100471), (
                12800000.0, 0.103372), (12900000.0, 0.106277), (13800000.0, 0.185621), (
                14300000.0, 0.265807), (14500000.0, 0.346323), (14700000.0, 0.427002), (
                14900000.0, 0.507773), (14900000.0, 0.588603), (15000000.0, 0.66947), (
                15100000.0, 0.750364), (15100000.0, 0.831278), (15200000.0, 0.912206), (
                15200000.0, 0.993145), (15200000.0, 1.07409), (15300000.0, 1.15505), (
                15300000.0, 1.23601), (15300000.0, 1.31697), (15300000.0, 1.39794), (
                15300000.0, 1.47891), (15400000.0, 1.55989), (15400000.0, 1.64087), (
                15400000.0, 1.72185), (15400000.0, 1.80283), (15400000.0, 1.88381), (
                15400000.0, 1.9648), (15400000.0, 2.04578), (15400000.0, 2.12677), (
                15400000.0, 2.20775), (15400000.0, 2.28874), (15400000.0, 2.36973), (
                15400000.0, 2.45072), (15500000.0, 2.53171), (15500000.0, 2.6127), (
                15500000.0, 2.6937), (15500000.0, 2.77469), (15500000.0, 2.85568), (
                15500000.0, 2.93667), (15500000.0, 3.01767), (15500000.0, 3.09866), (
                15500000.0, 3.17965), (15500000.0, 3.26065), (15500000.0, 3.34164), (
                15500000.0, 3.42264), (15500000.0, 3.50363), (15500000.0, 3.58463), (
                15500000.0, 3.66562), (15500000.0, 3.74662), (15500000.0, 3.82761), (
                15500000.0, 3.90861), (15500000.0, 3.98961), (15500000.0, 4.0706), (
                15500000.0, 4.1516), (15500000.0, 4.2326), (15500000.0, 4.31359), (
                15500000.0, 4.39459), (15500000.0, 4.47559), (15500000.0, 4.55658), (
                15500000.0, 4.63758), (15500000.0, 4.71858), (15500000.0, 4.79958), (
                15500000.0, 4.88057), (15500000.0, 4.96157), (15500000.0, 5.04257), (
                15500000.0, 5.12357), (15500000.0, 5.20456), (15500000.0, 5.28556), (
                15500000.0, 5.36656), (15500000.0, 5.44756), (15500000.0, 5.52855), (
                15500000.0, 5.60955), (15500000.0, 5.69055), (15500000.0, 5.77155), (
                15500000.0, 5.85255), (15500000.0, 5.93355), (15500000.0, 6.01454), (
                15500000.0, 6.09554), (15500000.0, 6.17654), (15600000.0, 6.25754), (
                15600000.0, 6.33854), (15600000.0, 6.41954), (15600000.0, 6.50053), (
                15600000.0, 6.58153), (15600000.0, 6.66253), (15600000.0, 6.74353), (
                15600000.0, 6.82453), (15600000.0, 6.90553), (15600000.0, 6.98653), (
                15600000.0, 7.06753), (15600000.0, 7.14852), (15600000.0, 7.22952), (
                15600000.0, 7.31052), (15600000.0, 7.39152), (15600000.0, 7.47252), (
                15600000.0, 7.55352), (15600000.0, 7.63452), (15600000.0, 7.71552), (
                15600000.0, 7.79652), (15600000.0, 7.87751), (15600000.0, 7.95851), (
                15600000.0, 8.03951), (15600000.0, 8.12051), (15600000.0, 8.20151), (
                15600000.0, 8.28251), (15600000.0, 8.36351), (15600000.0, 8.44451), (
                15600000.0, 8.52551), (15600000.0, 8.60651), (15600000.0, 8.68751), (
                15600000.0, 8.7685), (15600000.0, 8.8495), (15600000.0, 8.9305), (
                15600000.0, 9.0115), (15600000.0, 9.0925), (15600000.0, 9.1735), (
                15600000.0, 9.2545), (15600000.0, 9.3355), (15600000.0, 9.4165), (
                15600000.0, 9.4975), (15600000.0, 9.5785), (15600000.0, 9.6595), (
                15600000.0, 9.7405), (15600000.0, 9.8215), (15600000.0, 9.9025), (
                15600000.0, 9.98349), (15600000.0, 10.0645), (15600000.0, 10.1455), (
                15600000.0, 10.2265), (15600000.0, 10.3075), (15600000.0, 10.3885), (
                15600000.0, 10.4695), (15600000.0, 10.5505), (15600000.0, 10.6315), (
                15600000.0, 10.7125), (15600000.0, 10.7935), (15600000.0, 10.8745), (
                15600000.0, 10.9555), (15600000.0, 11.0365), (15600000.0, 11.1175), (
                15600000.0, 11.1985), (15600000.0, 11.2795), (15600000.0, 11.3605), (
                15600000.0, 11.4415), (15600000.0, 11.5225), (15600000.0, 11.6035), (
                15600000.0, 11.6845), (15600000.0, 11.7655), (15600000.0, 11.8465), (
                15600000.0, 11.9275), (15600000.0, 12.0085), (15600000.0, 12.0895), (
                15600000.0, 12.1705), (15600000.0, 12.2515), (15600000.0, 12.3325), (
                15600000.0, 12.4135), (15600000.0, 12.4945), (15600000.0, 12.5755), (
                15600000.0, 12.6565), (15600000.0, 12.7375), (15600000.0, 12.8185), (
                15600000.0, 12.8995), (15600000.0, 12.9805), (15600000.0, 13.0615), (
                15600000.0, 13.1425), (15600000.0, 13.2235), (15600000.0, 13.3045), (
                15600000.0, 13.3855), (15600000.0, 13.4665), (15600000.0, 13.5475), (
                15600000.0, 13.6285), (15600000.0, 13.7095), (15600000.0, 13.7905), (
                15600000.0, 13.8715), (15600000.0, 13.9525), (15600000.0, 14.0335), (
                15600000.0, 14.1145), (15600000.0, 14.1955), (15600000.0, 14.2765), (
                15600000.0, 14.3575), (15600000.0, 14.4385), (15600000.0, 14.5195), (
                15600000.0, 14.6005), (15600000.0, 14.6815)))



            #Section


            mdb.models['Model-%d' %(q)].BeamSection(consistentMassMatrix=False, integration=
                DURING_ANALYSIS, material='Material-1', name='Section-1', poissonRatio=0.0, 
                profile='Profile-1', temperatureVar=LINEAR)
            mdb.models['Model-%d' %(q)].parts['Part-1'].SectionAssignment(offset=0.0, 
                offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
                edges=mdb.models['Model-%d' %(q)].parts['Part-1'].edges.getSequenceFromMask(
                mask=('[#1 ]', ), )), sectionName='Section-1', thicknessAssignment=
                FROM_SECTION)
            mdb.models['Model-%d' %(q)].parts['Part-1'].assignBeamSectionOrientation(method=
                N1_COSINES, n1=(0.0, 0.0, -1.0), region=Region(
                edges=mdb.models['Model-%d' %(q)].parts['Part-1'].edges.getSequenceFromMask(
                mask=('[#1 ]', ), )))



            #Assembly


            mdb.models['Model-%d' %(q)].rootAssembly.DatumCsysByDefault(CARTESIAN)
            mdb.models['Model-%d' %(q)].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
                part=mdb.models['Model-%d' %(q)].parts['Part-1'])




            #Steps


            mdb.models['Model-%d' %(q)].StaticStep(initialInc=1e-05, maxNumInc=100000000, minInc=
                1e-08, name='Step-1', nlgeom=ON, previous='Initial')




            #Mesh


            mdb.models['Model-%d' %(q)].parts['Part-1'].seedPart(deviationFactor=0.1,    #Mesh size 5 mm chosen
                minSizeFactor=0.1, size=0.005)
            mdb.models['Model-%d' %(q)].parts['Part-1'].generateMesh()
            mdb.models['Model-%d' %(q)].parts['Part-1'].setElementType(elemTypes=(ElemType(
                elemCode=PIPE21, elemLibrary=STANDARD), ), regions=(                         # Element type: PIPE21
                mdb.models['Model-%d' %(q)].parts['Part-1'].edges.getSequenceFromMask(('[#1 ]', 
                ), ), ))



            #Displacement Point Node Creation


            mdb.models['Model-%d' %(q)].rootAssembly.regenerate()
            mdb.models['Model-%d' %(q)].rootAssembly.Set(name='Displacement', nodes=
                mdb.models['Model-%d' %(q)].rootAssembly.instances['Part-1-1'].nodes.getSequenceFromMask(
                mask=('[#0:5 #7c0000 ]', ), ))



            #Boundary


            mdb.models['Model-%d' %(q)].TabularAmplitude(data=((0.0, 0.0), (1.0, 1.0)), name=
                'Amp-1', smooth=SOLVER_DEFAULT, timeSpan=STEP)
            mdb.models['Model-%d' %(q)].DisplacementBC(amplitude='Amp-1', createStepName='Step-1'
                , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
                'BC-1', region=mdb.models['Model-%d' %(q)].rootAssembly.sets['Displacement'], u1=      # Displacement of 120 mm applied at center 
                UNSET, u2=-0.12, ur3=UNSET)



            #PSI Element Properties
    
            mdb.models['Model-%d' %(q)].keywordBlock.synchVersions(storeNodesAndElements=False)
            mdb.models['Model-%d' %(q)].keywordBlock.insert(1, 
                '\n*INCLUDE, input=psi_node_Set_Soil5.inp\n*INCLUDE, input=psi_element_Set_Soil5.inp')  #Called for PSI Nodes and Elements (From separate INP Files)
            mdb.models['Model-%d' %(q)].keywordBlock.insert(8, 
                # Need to change this part below based on the Tu and Pu value obtained from the different combination.
                '\n*PIPE-SOIL INTERACTION,ELSET=soil_psi_elset_Set_Soil\n*PIPE-SOIL STIFFNESS,TYPE=NONLINEAR,DIR=AXIAL\n '+ str(-Axial) +', -120e-3\n '+ str(-Axial) +', -35e-3\n 0, 0\n '+ str(Axial) +', 35e-3\n '+ str(Axial) +', 120e-3\n *PIPE-SOIL STIFFNESS,TYPE=NONLINEAR,DIR=VERTICAL\n '+ str(-Lateral) +', -120e-3\n '+ str(-Lateral) +', -30e-3\n 0, 0\n '+ str(Lateral) +', 30e-3\n '+str(Lateral)+', 120e-3')



            mdb.models['Model-%d' %(q)].keywordBlock.replace(29, 
                '\n*Boundary, amplitude=Amp-1\nDisplacement, 2, 2, -0.12\nPart-1-1.psi_far_end_Set_Soil,1,1\nPart-1-1.psi_far_end_Set_Soil,2,2\nPart-1-1.psi_far_end_Set_Soil,3,3')  # Boundary condition of PSI elements.



            #Job


            mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
                explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
                memory=90, memoryUnits=PERCENTAGE, model='Model-%d' %(q), modelPrint=OFF, 
                multiprocessingMode=DEFAULT, name='Job-%d' %(q), nodalOutputPrecision=SINGLE, 
                numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
                ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)



            #Job Submit

            mdb.jobs['Job-%d' %(q)].writeInput()     #Write the .INP file before Job submission
            mdb.jobs['Job-%d' %(q)].submit(consistencyChecking=OFF)   #Execute the job
            mdb.jobs['Job-%d' %(q)].waitForCompletion()     #Wait until the job is done before going to the next job







            o1 = session.openOdb(
                name='C:/Users/Tanmoy Sinha/Music/New folder/'+'Job-%d' %(q)+'.odb')  # (C:/Users/Tanmoy Sinha/Music/New folder) is the directory of .ODB file. Need to change if directory of ODB changes
            session.viewports['Viewport: 1'].setValues(displayedObject=o1)

            odb = session.odbs['C:/Users/Tanmoy Sinha/Music/New folder/'+'Job-%d' %(q)+'.odb'] #Need to change the directory if ODB location changes
            session.xyDataListFromField(odb=o1, outputPosition=NODAL, variable=(('RF', 
                NODAL, ((COMPONENT, 'RF2'), )), ), nodeLabels=(('PART-1-1', ('179:183', )),   #The physical distance between node 179 to 183 is 25 mm which is equal to the pulling grip width.
                ))
            xy1 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 179']
            xy2 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 180']
            xy3 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 181']
            xy4 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 182']
            xy5 = session.xyDataObjects['RF:RF2 PI: PART-1-1 N: 183']
            xy6 = sum((xy1, xy2, xy3, xy4, xy5))
            xy6.setValues(
                sourceDescription='sum ( ( "RF:RF2 PI: PART-1-1 N: 179", "RF:RF2 PI: PART-1-1 N: 180", "RF:RF2 PI: PART-1-1 N: 181", "RF:RF2 PI: PART-1-1 N: 182", "RF:RF2 PI: PART-1-1 N: 183" ) )')
            tmpName = xy6.name
            session.xyDataObjects.changeKey(tmpName, 'XYData-%d' %(q))
            x0 = session.xyDataObjects['XYData-%d' %(q)]
            session.xyReportOptions.setValues(totals=ON, minMax=ON)
            session.writeXYReport(fileName='Pullout-%d' %(q)+'.txt', xyData=(x0, )) #Generate a Pullout text file with maximum value of pullout resistance

            odb = session.odbs['C:/Users/Tanmoy Sinha/Music/New folder/'+'Job-%d' %(q)+'.odb']
            session.xyDataListFromField(odb=o1, outputPosition=NODAL, variable=(('LE', 
                INTEGRATION_POINT, ((COMPONENT, 'LE11'), )), ), nodeLabels=(('PART-1-1', (
                '175', )), ))
            x2 = session.xyDataObjects['LE:LE11 (Avg: 75%) SP:2 PI: PART-1-1 N: 175']
            x3 = session.xyDataObjects['LE:LE11 (Avg: 75%) SP:14 PI: PART-1-1 N: 175']
            session.writeXYReport(fileName='Strain-%d' %(q)+'.txt', appendMode=OFF, xyData=(x2, x3)) #Generate a Strain text file with maximum value of strain at 175 number node

            break

    start=start+1


        #End