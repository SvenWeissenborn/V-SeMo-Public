import io
import math

def buildSectors(filename,
                 lorentzTransform,
                 nSectorRowsFromSphere,
                 nSectorColumnsFromSphere,
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



    dtheta = (math.pi/nSectorRowsFromSphere)
    dphi = (2*math.pi/nSectorColumnsFromSphere)

    maxSectorWidth = radius * dphi * math.sin(dtheta * math.floor(nSectorRowsFromSphere/2))

    if (nRowsInModel > nSectorRowsFromSphere):
        print("Achtung nRowsInModel ist größer als nSectorRowsFromSphere")
        return -1

    if (nColumnsInModel > nSectorColumnsFromSphere):
        print("Achtung nColumnsInModel ist größer als nSectorColumnsFromSphere")
        return -2

    if (nSectorRowsFromSphere % 2 != nRowsInModel % 2):
        print("Achtung nSectorRowsFromSphere und nRowsInModel müssen gerade oder ungerade sein")
        return -3


    zeilestart = math.floor((nSectorRowsFromSphere-nRowsInModel)/2)
    zeileende = nSectorRowsFromSphere-round((nSectorRowsFromSphere-nRowsInModel)/2)

    file = io.open(filename,'w')

    file.write( "/*" +"\n"
                "------Parameter-------" + "\n"
                "turnLorentzTransformOn = " + str(lorentzTransform) + "\n"                   
                "nSectorRowsFromSphere = " + str(nSectorRowsFromSphere) + "\n"
                "nSectorColumnsFromSphere = " + str(nSectorColumnsFromSphere) + "\n"
                "radius = " + str(radius) + "\n"
                "nRowsInModel = " + str(nRowsInModel) + "\n"
                "nColumnsInModel = " + str(nColumnsInModel) + "\n"                                                        
                "sectorDistance_x = " + str(sectorDistance_x) + "\n"
                "sectorDistance_y = " + str(sectorDistance_y) + "\n"
                "startZoom =" + str(startZoom) + "\n"
                "startViewportTransform_4 =" + str(startViewportTransform_4) + "\n"
                "startViewportTransform_5 =" + str(startViewportTransform_5) + "\n"
                "fontSize = " + str(fontSize) + "\n"
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
                            "sec_angle"]

    sectorDict = dict(zip(variablenamesSectors,range(len(variablenamesSectors))))

    anzahlDerSektoren = nRowsInModel * nColumnsInModel

    #sectorValues = np.zeros((len(variablenamesSectors),anzahlDerSektoren))
    sectorValues = [[[] for ii in range(anzahlDerSektoren)] for jj in range(len(variablenamesSectors))]

    jj =0

    for id in range(0, anzahlDerSektoren):
        #Um 6en un 9en unterscheiden zu koennen, werden sie um einen Punkt ergaenzt
        if (id == 5 or id == 8 ):
            sectorValues[sectorDict["sec_name"]][id] = "'" + str(id + 1)+"." "'"
        else:
            sectorValues[sectorDict["sec_name"]][id] = id + 1
        sectorValues[sectorDict["sec_ID"]][id] = id
        # Bei Bedarf muss die Fläche dazu genommen werden: Wichtig, "sec_fill" muss der Liste variablenamesSectors hinzugefügt werden!!!
        sectorValues[sectorDict["sec_fill"]][id] = "'white'"
        sectorValues[sectorDict["sec_fontSize"]][id] = fontSize

    for zeile in range(zeilestart, zeileende):
        for ii in range(0,nColumnsInModel):
            sectorTop = radius*math.sin((zeile) * dtheta) * dphi

            sectorBottom = radius * math.sin((zeile +1) * dtheta) * dphi

            offset = (sectorTop - sectorBottom)/2

            sector_width = max(sectorTop,sectorBottom)

            sector_height = math.sqrt(math.pow(radius, 2) * math.pow(dtheta, 2) - math.pow(offset, 2))

            secIdx = jj + ii * (zeileende - zeilestart)

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

            sectorValues[sectorDict["sec_posx"]][secIdx] = (ii - nColumnsInModel * 0.5 + 0.5) * (sectorDistance_x + maxSectorWidth) #+ (maxSectorWidth - sector_width) / 2

            sectorValues[sectorDict["sec_posy"]][secIdx] = (zeile - (nRowsInModel + 0.5)) * sector_y_dist - 100

            sectorValues[sectorDict["sec_angle"]][secIdx] = 0

            if (zeile == round((nSectorRowsFromSphere-nRowsInModel) / 2)):
                sectorValues[sectorDict["sec_neighbour_top"]][secIdx] = -1
            else:
                sectorValues[sectorDict["sec_neighbour_top"]][secIdx] = zeile + nRowsInModel * ii - round((nSectorRowsFromSphere-nRowsInModel) / 2) - 1

            if (ii == (nColumnsInModel-1)):
                if(nColumnsInModel == nSectorColumnsFromSphere):
                    sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = zeile
                else:
                    sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = -1
            else:
                sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = zeile + nRowsInModel * ii - round((nSectorRowsFromSphere-nRowsInModel) / 2) + nRowsInModel

            if (zeile == (nSectorRowsFromSphere-round((nSectorRowsFromSphere-nRowsInModel) / 2))-1):
                sectorValues[sectorDict["sec_neighbour_bottom"]][secIdx] = -1
            else:
                sectorValues[sectorDict["sec_neighbour_bottom"]][secIdx] = zeile + nRowsInModel * ii - round((nSectorRowsFromSphere-nRowsInModel) / 2) +1

            if (ii == 0):
                if (nColumnsInModel == nSectorColumnsFromSphere):
                    sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = zeile + nRowsInModel * nColumnsInModel - nRowsInModel
                else:
                    sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = -1
            else:
                sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = zeile + nRowsInModel * ii - round((nSectorRowsFromSphere-nRowsInModel) / 2) - nRowsInModel

        jj = jj + 1


    for ii in range(0,len(variablenamesSectors)):
        file.write(variablenamesSectors[ii]+"= [ ")
        for jj in range(0,anzahlDerSektoren):
            file.write(str( sectorValues[ii][jj])+', ')
        file.write("];\n")


    file.close()

    return sectorValues