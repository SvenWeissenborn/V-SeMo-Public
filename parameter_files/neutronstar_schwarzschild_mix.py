import io
import math

def buildSectors(filename,
                 lorentzTransform,
                 nSektorzeilenVonRing,
                 nSektorspaltenVonRing,
                 schwarzschildradius,
                 dradius,
                 fontSizeStern,
                 fontSizeAussenraum,
                 startZoom,
                 startViewportTransform_4,
                 startViewportTransform_5,
                 lineColors,
                 lineStrokeWidthWhenNotSelected,
                 lineStrokeWidthWhenSelected,
                 markColors,
                 vectorColors):

    dphi = (2*math.pi/nSektorspaltenVonRing)






    file = io.open(filename,'w')

    file.write( "/*" +"\n"
            "------Parameter-------" +"\n"
            "turnLorentzTransformOn = " + str(lorentzTransform) + "\n"
            "nSektorzeilenVonRing: " + str(nSektorzeilenVonRing) +"\n"
            "nSektorspaltenVonRing: " + str(nSektorspaltenVonRing) +"\n"
            "schwarzschildradius: " + str(schwarzschildradius) +"\n"
            "dradius: " + str(dradius) + "\n"
            "startZoom =" + str(startZoom) + "\n"
            "startViewportTransform_4 =" + str(startViewportTransform_4) + "\n"
            "startViewportTransform_5 =" + str(startViewportTransform_5) + "\n"
            "fontSizeStern: " + str(fontSizeStern) + "\n"    
            "fontSizeStern: " + str(fontSizeAussenraum) + "\n" 
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
    ile.write("\n")

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

    anzahlDerSektoren = nSektorzeilenVonRing * nSektorspaltenVonRing

    sectorValues = [[[] for ii in range(anzahlDerSektoren)] for jj in range(len(variablenamesSectors))]



    for ringspalte in range(0, nSektorspaltenVonRing):
        for ringzeile in range(0, nSektorzeilenVonRing):

            rad1 = (ringzeile ) * dradius
            rad2 = (ringzeile + 1) * dradius
            radmid = (rad2 + rad1)/2
            if(ringzeile < 3):
                radial = math.sqrt(1 / (1 - 0.125 * math.pow((radmid / schwarzschildradius),2))) * dradius
                offset = dradius * math.sin(dphi * 0.5)
                sectorValues[sectorDict["sec_fill"]][ringzeile + ringspalte * nSektorzeilenVonRing] = "'#e2e2e2'"
                sectorValues[sectorDict["sec_fontSize"]][ringzeile + ringspalte * nSektorzeilenVonRing] = fontSizeStern
            else:
                radial = math.sqrt(math.pow((1 - (schwarzschildradius/radmid)), (-1))) * dradius
                offset = dradius * math.sin(dphi * 0.5)
                sectorValues[sectorDict["sec_fill"]][ringzeile + ringspalte * nSektorzeilenVonRing] = "'white'"
                sectorValues[sectorDict["sec_fontSize"]][ringzeile + ringspalte * nSektorzeilenVonRing] = fontSizeAussenraum


            # "Die integrale Form von Schwarzschild" radial = math.sqrt(rad2 * (rad2 - schwarzschildradius)) + schwarzschildradius * math.log(math.sqrt(rad2 - schwarzschildradius) + math.sqrt(rad2)) - (math.sqrt(rad1 * (rad1 - schwarzschildradius)) + schwarzschildradius * math.log(math.sqrt(rad1 - schwarzschildradius) + math.sqrt(rad1)))
            sector_height = math.sqrt(math.pow(radial, 2) - math.pow(offset, 2))


            if (ringzeile != 0):
                sector_y_dist = sector_height / 2 + sectorValues[sectorDict["sec_height"]][ringzeile-1] / 2 + sector_y_dist + 10
            else:
                sector_y_dist = 20 + sector_height/2

            secIdx = ringzeile + ringspalte * (nSektorzeilenVonRing)

            sectorValues[sectorDict["sec_name"]][secIdx] = "'%c%d'" % (chr(ringzeile + 97).upper(),(ringspalte+1))
            sectorValues[sectorDict["sec_ID"]][secIdx] = ringzeile + ringspalte * (nSektorzeilenVonRing)
            sectorTop = (dradius * (ringzeile + 1)) * 2 * math.sin(dphi * 0.5)
            sectorBottom = (dradius * (ringzeile )) * 2 * math.sin(dphi * 0.5)



            sector_width = sectorTop


            sectorValues[sectorDict["sec_height"]][secIdx] = sector_height
            sectorValues[sectorDict["sec_width"]][secIdx] = sector_width
            sectorValues[sectorDict["sec_coords"]][secIdx] = ([-min(0, offset),
                                                               0,
                                                               sectorTop - min(0, offset),
                                                               0,
                                                               sectorBottom + max(0, offset),
                                                               sector_height,
                                                               max(0, offset),
                                                               sector_height])


            sectorValues[sectorDict["sec_posx"]][secIdx] = math.sin(ringspalte * dphi) * ( sector_y_dist)
            sectorValues[sectorDict["sec_posy"]][secIdx] = - math.cos(ringspalte * dphi) * ( sector_y_dist)
            sectorValues[sectorDict["sec_angle"]][secIdx] = ringspalte * dphi *180/math.pi
            sectorValues[sectorDict["sec_neighbour_top"]][secIdx] = -1
            sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = -1
            sectorValues[sectorDict["sec_neighbour_bottom"]][secIdx] = -1
            sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = -1

            if (ringzeile == (nSektorzeilenVonRing - 1)):
                sectorValues[sectorDict["sec_neighbour_top"]][secIdx] = -1
            else:
                sectorValues[sectorDict["sec_neighbour_top"]][secIdx] = ringzeile + ringspalte * (nSektorzeilenVonRing) + 1

            if (ringspalte == (nSektorspaltenVonRing - 1)):
                sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = ringzeile
            else:
                sectorValues[sectorDict["sec_neighbour_right"]][secIdx] = ringzeile + ringspalte * (nSektorzeilenVonRing) + nSektorzeilenVonRing

            if (ringzeile == 0):
                sectorValues[sectorDict["sec_neighbour_bottom"]][secIdx] = -1
            else:
                sectorValues[sectorDict["sec_neighbour_bottom"]][secIdx] = ringzeile + ringspalte * (nSektorzeilenVonRing) -1

            if (ringspalte == 0):
                sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = nSektorspaltenVonRing * nSektorzeilenVonRing - nSektorzeilenVonRing + ringzeile
            else:
                sectorValues[sectorDict["sec_neighbour_left"]][secIdx] = ringzeile + ringspalte * (nSektorzeilenVonRing) - nSektorzeilenVonRing


    for ii in range(0,len(variablenamesSectors)):
        file.write(variablenamesSectors[ii]+"= [ ")
        for jj in range(0,anzahlDerSektoren):
            file.write(str( sectorValues[ii][jj])+', ')
        file.write("];\n")


    file.close()

    return sectorValues