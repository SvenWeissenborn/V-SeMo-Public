import io
import math

def buildSectors(filename,
                 lorentzTransform,
                 nRowsInModel,
                 nColumnsInModel,
                 radius,
                 delta_r,
                 delta_t,
                 sectorDistance_x,
                 sectorDistance_y,
                 start_x,
                 start_y,
                 startZoom,
                 startViewportTransform_4,
                 startViewportTransform_5,
                 fontSize,
                 lineColors,
                 lineStrokeWidthWhenNotSelected,
                 lineStrokeWidthWhenSelected,
                 markColors,
                 vectorColors):

    file = io.open(filename, 'w')

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
    file.write("\n")
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
                            "sec_angle",
                            "sec_timeEdgeLeft",
                            "sec_timeEdgeRight",
                            "spaceEdge"]

    sectorDict = dict(zip(variablenamesSectors,range(len(variablenamesSectors))))

    anzahlDerSektoren = nRowsInModel * nColumnsInModel

    sectorValues = [[[] for ii in range(anzahlDerSektoren)] for jj in range(len(variablenamesSectors))]



    for id in range(0, anzahlDerSektoren):
        sectorValues[sectorDict["sec_ID"]][id] = id
        sectorValues[sectorDict["sec_fontSize"]][id] = fontSize
    for zeile in range(0, nRowsInModel):

        for ii in range(0, nColumnsInModel):

            secIdx = zeile + ii * nRowsInModel
            secIdxBefore = zeile + (ii - 1) * nRowsInModel

            print("zeile", zeile)
            print("Sektor", secIdx)

            #Für die x-Position des Sektors wird die Sektorhöhe des alten Sektors verwendet.
            #Für die y-Position des Sektors wird die Hälfte der Differenz der zeitartigen Sektorkanten benötigt.
            # -> Diese Berechnung folgt weiter unten
            sectorValues[sectorDict["sec_name"]][secIdx] = "'%c%d'" % (chr(ii + 97).upper(),(nRowsInModel-zeile))
            if (ii == 0):
                sectorValues[sectorDict["sec_posx"]][secIdx] = start_x
            else:
                sectorValues[sectorDict["sec_posx"]][secIdx] = sectorValues[sectorDict["sec_posx"]][secIdxBefore] + sectorwidth + sectorDistance_x

            sectorValues[sectorDict["sec_angle"]][secIdx] = 0

            timeEdgeLeft = math.sqrt(1 - (1 / ((ii + 1) * delta_r))) * delta_t * radius

            timeEdgeRight = math.sqrt(1 - (1 / ((ii + 2) * delta_r))) * delta_t * radius

            spaceEdge =  math.sqrt(1 / ( 1 - (1 / (((( ii + 1 ) + ( ii + 2 )) / 2) * delta_r)))) * delta_r * radius

            sectorValues[sectorDict["sec_fill"]][secIdx] = "'white'"

            offset_y = (timeEdgeRight - timeEdgeLeft) / 2

            sectorwidth = math.sqrt( math.pow(spaceEdge, 2) + math.pow(offset_y, 2))

            sectorValues[sectorDict["sec_width"]][secIdx] = sectorwidth
            sectorValues[sectorDict["sec_height"]][secIdx] = max(timeEdgeLeft, timeEdgeRight)
            sectorValues[sectorDict["sec_timeEdgeLeft"]][secIdx] = timeEdgeLeft
            sectorValues[sectorDict["sec_timeEdgeRight"]][secIdx] = timeEdgeRight
            sectorValues[sectorDict["spaceEdge"]][secIdx] = spaceEdge

            sectorValues[sectorDict["sec_coords"]][secIdx] = ([0,
                                                               - timeEdgeLeft,
                                                               sectorwidth,
                                                               - timeEdgeLeft - offset_y,
                                                               sectorwidth,
                                                               offset_y,
                                                               0,
                                                               0])



            if (zeile == 0):
               sectorValues[sectorDict["sec_neighbour_top"]][secIdx] = - 1
            else:
               sectorValues[sectorDict["sec_neighbour_top"]][secIdx] = secIdx - 1

            if (ii == nColumnsInModel - 1):
               sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = -1
            else:
               sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = zeile + (ii + 1) * nRowsInModel

            if (zeile == nRowsInModel - 1):
               sectorValues[sectorDict["sec_neighbour_bottom"]][secIdx] = - 1
            else:
               sectorValues[sectorDict["sec_neighbour_bottom"]][secIdx] = secIdx + 1

            if (ii == 0):
               sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = -1
            else:
               sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = secIdxBefore
            print("nachbar_links", sectorValues[sectorDict["sec_neighbour_left"]][secIdx])

            if (zeile == 0):
                if (ii == 0):
                    sectorValues[sectorDict["sec_posy"]][secIdx] = start_y
                else:
                    sectorValues[sectorDict["sec_posy"]][secIdx] = sectorValues[sectorDict["sec_posy"]][secIdxBefore] + offset_y
            else:
                if (ii == 0):
                    sectorValues[sectorDict["sec_posy"]][secIdx] = start_y + zeile * (timeEdgeRight + sectorDistance_y)
                else:
                    sectorValues[sectorDict["sec_posy"]][secIdx] = sectorValues[sectorDict["sec_posy"]][secIdxBefore] + offset_y


    for ii in range(0,len(variablenamesSectors)):
        file.write(variablenamesSectors[ii]+"= [ ")
        for jj in range(0,anzahlDerSektoren):
            file.write(str( sectorValues[ii][jj])+', ')
        file.write("];\n")

    file.close()

    return sectorValues