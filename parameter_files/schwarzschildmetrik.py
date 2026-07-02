import io
import math

def buildSectors(filename,
                 lorentzTransform,
                 nSektorzeilenVonRing,
                 nSektorspaltenVonRing,
                 nSektorzeilenVonRingSchwarzschild,
                 nSektorzeilenVonRingEuklid,
                 schwarzschildradius,
                 dr,
                 startZoom,
                 startViewportTransform_4,
                 startViewportTransform_5,
                 fontSize,
                 lineColors,
                 lineStrokeWidthWhenNotSelected,
                 lineStrokeWidthWhenSelected,
                 markColors,
                 vectorColors):

    dphi = (2*math.pi/nSektorspaltenVonRing)
    dradius = dr * schwarzschildradius

    sector_y_dist = 10.0



    file = io.open(filename,'w')

    file.write( "/*" +"\n"
                "------Parameter-------" +"\n"
                "turnLorentzTransformOn = " + str(lorentzTransform) + "\n"
                "nSektorzeilenVonRing: " + str(nSektorzeilenVonRing) +"\n"
                "nSektorspaltenVonRing: " + str(nSektorspaltenVonRing) +"\n"
                "nSektorzeilenVonRingSchwarzschild: " + str(nSektorzeilenVonRingSchwarzschild) +"\n"
                "nSektorzeilenVonRingEuklid: " + str(nSektorzeilenVonRingEuklid) +"\n"
                "schwarzschildradius: " + str(schwarzschildradius) +"\n"
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
                            "sec_angle"]

    sectorDict = dict(zip(variablenamesSectors,range(len(variablenamesSectors))))

    anzahlDerSektoren = nSektorzeilenVonRing * nSektorspaltenVonRing

    sectorValues = [[[] for ii in range(anzahlDerSektoren)] for jj in range(len(variablenamesSectors))]



    for ringspalte in range(0, nSektorspaltenVonRing):
        for ringzeile in range(0, nSektorzeilenVonRing):

            rad1 = 1.25 * schwarzschildradius + (ringzeile) * dradius
            rad2 = 1.25 * schwarzschildradius + (ringzeile + 1) * dradius

            wichtungsfaktor = 0.0

            if(ringzeile < nSektorzeilenVonRingSchwarzschild):
                wichtungsfaktorBottom = 0.0
                wichtungsfaktorTop = 0.0
                wichtungsfaktorRadial = 0.0
            elif(ringzeile < nSektorzeilenVonRing - nSektorzeilenVonRingEuklid):
                if(ringzeile == nSektorzeilenVonRingSchwarzschild):
                    wichtungsfaktorBottom = 0.0
                else:
                    wichtungsfaktorBottom = (ringzeile - 1 - nSektorzeilenVonRingEuklid) * 1 / (nSektorzeilenVonRing - (nSektorzeilenVonRingSchwarzschild + nSektorzeilenVonRingEuklid))
                if(ringzeile == nSektorzeilenVonRing - nSektorzeilenVonRingEuklid - 1):
                    wichtungsfaktorTop = 1.0
                else:
                    wichtungsfaktorTop = (ringzeile - nSektorzeilenVonRingEuklid) * 1 / (nSektorzeilenVonRing - (nSektorzeilenVonRingSchwarzschild + nSektorzeilenVonRingEuklid))
                wichtungsfaktorRadial = (ringzeile - nSektorzeilenVonRingEuklid) * 1 / (nSektorzeilenVonRing - (nSektorzeilenVonRingSchwarzschild -1 + nSektorzeilenVonRingEuklid))
            elif(ringzeile >= nSektorzeilenVonRing - nSektorzeilenVonRingEuklid):
                #if (ringzeile == nSektorzeilenVonRing - nSektorzeilenVonRingEuklid):
                    #wichtungsfaktorBottom = (ringzeile - 1 - nSektorzeilenVonRingSchwarzschild) * 1 / (nSektorzeilenVonRing - (nSektorzeilenVonRingSchwarzschild + nSektorzeilenVonRingEuklid))
                #else:
                wichtungsfaktorBottom = 1.0
                wichtungsfaktorTop = 1.0
                wichtungsfaktorRadial = 1.0

            print("zzzzzzzzzzz")
            print("WB: " + str(wichtungsfaktorBottom))
            print("WT: " + str(wichtungsfaktorTop))
            print("WR: "+ str(wichtungsfaktorRadial))


            lengthSchwarzschildBottom = rad1 * dphi
            lengthSchwarzschildTop = rad2 * dphi
            lengthEuklidBottom = rad1 * 2 * math.sin(dphi / 2)
            lengthEuklidTop = rad2 * 2 * math.sin(dphi / 2)

            print("SB: "+ str(lengthSchwarzschildBottom))
            print("ST: "+ str(lengthSchwarzschildTop))
            print("EB: "+ str(lengthEuklidBottom))
            print("ET: "+ str(lengthEuklidTop))

            lengthBottomMid = (1 - wichtungsfaktorBottom) * lengthSchwarzschildBottom + wichtungsfaktorBottom * lengthEuklidBottom
            lengthTopMid = (1 - wichtungsfaktorTop) * lengthSchwarzschildTop + wichtungsfaktorTop * lengthEuklidTop

            print("MB: " + str(lengthBottomMid))
            print("MT: " + str(lengthTopMid))

            radialSchwarzschild = math.sqrt(rad2 * (rad2 - schwarzschildradius)) + schwarzschildradius * math.log(math.sqrt(rad2 - schwarzschildradius) + math.sqrt(rad2)) - (math.sqrt(rad1 * (rad1 - schwarzschildradius)) + schwarzschildradius * math.log(math.sqrt(rad1 - schwarzschildradius) + math.sqrt(rad1)))
            radialEuklidisch = dradius

            print("Ringzeile" + str(ringzeile))
            print(str(lengthSchwarzschildBottom - lengthEuklidBottom))
            print(str(1 - lengthEuklidBottom / lengthSchwarzschildBottom))
            print(str(lengthSchwarzschildTop - lengthEuklidTop))
            print(str(1 - lengthEuklidTop / lengthSchwarzschildTop))
            print("difference radialSchwarzschild radialEuklidisch " + str(radialSchwarzschild - radialEuklidisch))
            print("mistake " + str(1 - radialEuklidisch / radialSchwarzschild))

            if(ringzeile < nSektorzeilenVonRingSchwarzschild):
                radial = radialSchwarzschild
            elif(ringzeile < nSektorzeilenVonRing - nSektorzeilenVonRingEuklid):
                radial = (1 - wichtungsfaktorRadial) * radialSchwarzschild + wichtungsfaktorRadial * radialEuklidisch
            elif(ringzeile >= nSektorzeilenVonRing - nSektorzeilenVonRingEuklid):
                radial = radialEuklidisch
            #offset = dradius * dphi * 0.5
            offset = abs(lengthTopMid - lengthBottomMid) / 2
            sector_height = math.sqrt(math.pow(radial, 2) - math.pow(offset, 2))

            secIdx = ringzeile + ringspalte * nSektorzeilenVonRing

            if (ringzeile != 0):
                sector_y_dist = sector_height / 2 + sectorValues[sectorDict["sec_height"]][ringzeile-1] / 2 + sector_y_dist + 20
            else:
                sector_y_dist = dradius + sector_height/2 + 30

            if(ringzeile + 97 < (26 +97)):
                sectorValues[sectorDict["sec_name"]][secIdx] = "'%c%d'" % (chr(ringzeile + 97).upper(), (ringspalte + 1))
            else:
                sectorValues[sectorDict["sec_name"]][secIdx] = "'%c%c%d'" % (chr(ringzeile//26 - 1 + 97).upper(), chr(ringzeile%26 + 97).upper(), (ringspalte + 1))

            sectorValues[sectorDict["sec_ID"]][secIdx] = ringzeile + ringspalte * (nSektorzeilenVonRing)

            if (ringzeile >= nSektorzeilenVonRing - nSektorzeilenVonRingEuklid):
                sectorValues[sectorDict["sec_type"]][secIdx] = "'euklid'"
            else:
                sectorValues[sectorDict["sec_type"]][secIdx] = "'noneuklid'"

            sectorValues[sectorDict["sec_fill"]][secIdx] = "'white'"
            sectorValues[sectorDict["sec_fontSize"]][secIdx] = fontSize
            sectorTop = lengthTopMid #(dradius * (ringzeile + 2)) * dphi
            sectorBottom = lengthBottomMid #(dradius * (ringzeile + 1)) * dphi



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