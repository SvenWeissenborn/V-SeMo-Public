import io
import math

def buildSectors(filename,
                 lorentzTransform,
                 radius,
                 nRowsInModel,
                 nColumnsInModel,
                 sectorDistance_x,
                 sectorDistance_y,
                 startZoom,
                 startViewportTransform_4,
                 startViewportTransform_5,
                 fontSize,
                 lineColors,
                 lineStrokeWidthWhenNotSelected,
                 lineStrokeWidthWhenSelected,
                 markColors,
                 vectorColors):



    dtheta = (math.pi/9)
    dphi = (math.pi/9)



    file = io.open(filename,'w')

    file.write( "/*" +"\n"
                "------Parameter-------" + "\n"
                "turnLorentzTransformOn = " + str(lorentzTransform) + "\n"
                "radius: " + str(radius) + "\n"
                "nRowsInModel: " + str(nRowsInModel) + "\n"
                "nColumnsInModel: " + str(nColumnsInModel) + "\n"                                                        
                "sectorDistance_x: " + str(sectorDistance_x) + "\n"
                "sectorDistance_y: " + str(sectorDistance_y) + "\n"
                "startZoom =" + str(startZoom) + "\n"
                "startViewportTransform_4 =" + str(startViewportTransform_4) + "\n"
                "startViewportTransform_5 =" + str(startViewportTransform_5) + "\n"
                "fontSize: " + str(fontSize) + "\n"
                "----------------------"
                + "\n"
                  "*/"
                )

    file.write("\n")
    file.write("\n")

    file.write(
        "startZoom =" + str(startZoom) + "\n"
        "startViewportTransform_4 =" + str(startViewportTransform_4) + "\n"
        "startViewportTransform_5 =" + str(startViewportTransform_5) + "\n"
    )
    file.write("\n")

    file.write("let turnLorentzTransformOn =" + str(lorentzTransform) + "\n")

    file.write("\n")

    file.write(
        "let line_colors = " + str(lineColors)
    )
    file.write(
        "let mark_colors = " + str(markColors)
    )
    file.write("\n")
    file.write(
        "let vector_colors = " + str(vectorColors)
    )
    file.write("\n")
    file.write(
        "let lineStrokeWidthWhenNotSelected = " + str(lineStrokeWidthWhenNotSelected)
    )
    file.write("\n")
    file.write(
        "let lineStrokeWidthWhenSelected =" + str(lineStrokeWidthWhenSelected)
    )
    file.write("\n")
    variablenamesSectors = ["sec_name",
                            "sec_fill",
                            "sec_ID",
                            "sec_type",
                            "sec_fontSize",
                            "sec_height",
                            "sec_width",
                            "sec_coords",
                            "sec_neighbour_top",
                            "sec_neighbour_right",
                            "sec_neighbour_bottom",
                            "sec_neighbour_left",
                            "sec_posx",
                            "sec_posy",
                            "sec_angle"]

    sectorDict = dict(zip(variablenamesSectors,range(len(variablenamesSectors))))

    anzahlDerSektoren = nRowsInModel * nColumnsInModel


    sectorValues = [[[] for ii in range(anzahlDerSektoren)] for jj in range(len(variablenamesSectors))]

    maxsectorwidth = radius * math.cosh(math.pi/6) * math.pi/9

    maxsectorheight = radius * math.pi/9


    for id in range(0, anzahlDerSektoren):
        if (id == 5 or id == 8 ):
            sectorValues[sectorDict["sec_name"]][id] = "'" + str(id + 1)+"." "'"
        else:
            sectorValues[sectorDict["sec_name"]][id] = id + 1
        sectorValues[sectorDict["sec_ID"]][id] = id
        sectorValues[sectorDict["sec_fill"]][id] = "'white'"
        sectorValues[sectorDict["sec_fontSize"]][id] = fontSize

    jj = 0

    for zeile in range(0, nRowsInModel):

        for ii in range(0, nColumnsInModel):

            sectorTop = radius*math.cosh(-math.pi/6 + (zeile) * dtheta) * dphi

            sectorBottom = radius * math.cosh(-math.pi/6 + (zeile +1) * dtheta) * dphi

            offset = (sectorTop - sectorBottom)/2

            sector_width = max(sectorTop, sectorBottom)

            sector_height = math.sqrt(math.pow(radius, 2) * math.pow(dtheta, 2) - math.pow(offset, 2))

            secIdx = jj + ii * nRowsInModel

            sectorValues[sectorDict["sec_height"]][secIdx] = sector_height

            sectorValues[sectorDict["sec_width"]][secIdx] = sector_width

            sector_y_dist = sector_height + sectorDistance_y

            sectorValues[sectorDict["sec_coords"]][secIdx] = ([-min(0, offset),
                                                               0,
                                                               sectorTop - min(0, offset),
                                                               0,
                                                               sectorBottom + max(0, offset),
                                                               sector_height,
                                                               max(0, offset),
                                                               sector_height])


            sectorValues[sectorDict["sec_posx"]][secIdx] = (ii * maxsectorwidth +((ii-1) * sectorDistance_y)) - maxsectorwidth

            sectorValues[sectorDict["sec_posy"]][secIdx] = (jj * maxsectorheight +((jj-1) * sectorDistance_y)) - maxsectorheight

            sectorValues[sectorDict["sec_angle"]][secIdx] = 0

            if (zeile == 0):
               sectorValues[sectorDict["sec_neighbour_top"]][secIdx] = - 1
            else:
               sectorValues[sectorDict["sec_neighbour_top"]][secIdx] = (jj + ii * nRowsInModel)- 1

            if (ii == 2):
               sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = -1
            else:
               sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = jj + ii * nRowsInModel + nColumnsInModel

            if (zeile == 2):
               sectorValues[sectorDict["sec_neighbour_bottom"]][secIdx] = - 1
            else:
               sectorValues[sectorDict["sec_neighbour_bottom"]][secIdx] = (jj + ii * nRowsInModel) + 1

            if (ii == 0):
               sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = -1
            else:
               sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = (jj + ii * nRowsInModel) - 3



        jj=jj+1


    for ii in range(0,len(variablenamesSectors)):
        file.write(variablenamesSectors[ii]+"= [ ")
        for jj in range(0,anzahlDerSektoren):
            file.write(str( sectorValues[ii][jj])+', ')
        file.write("];\n")


    file.close()

    return sectorValues