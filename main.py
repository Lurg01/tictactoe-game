

pos = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]



def board():

    print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\n"+
          pos[3]+" | "+pos[4]+" | "+pos[5]+"\n"+
          pos[6]+" | "+pos[7]+" | "+pos[8])





def player_Turn():

    board()

    def player_X():

        game_ongoing = True
        while game_ongoing:



            pos1 = pos[0]
            pos2 = pos[1]

            pos3 = pos[2]
            pos4 = pos[3]
            pos5 = pos[4]
            pos6 = pos[5]

            pos7 = pos[6]
            pos8 = pos[7]
            pos9 = pos[8]
            #--------------------------------------------------------------




            if pos[0] == "X" and pos[1] == "X" and pos[2] == "X" or pos[3] == "X" and pos[4] == "X" and pos[5] == "X" \
                or pos[6] == "X" and pos[7] == "X" and pos[8] == "X" or pos[2] == "X" and pos[5] == "X" and pos[8] == "X" \
                or pos[1] == "X" and pos[4] == "X" and pos[7] == "X" or pos[0] == "X" and pos[3] == "X" and pos[6] == "X" \
                or pos[2] == "X" and pos[4] == "X" and pos[6] == "X" or pos[0] == "X" and pos[4] == "X" and pos[8] == "X" \
                or pos[0] == "O" and pos[1] == "O" and pos[2] == "O" or pos[3] == "O" and pos[4] == "O" and pos[5] == "O" \
                or pos[6] == "O" and pos[7] == "O" and pos[8] == "O" or pos[2] == "O" and pos[5] == "O" and pos[8] == "O" \
                or pos[1] == "O" and pos[4] == "O" and pos[7] == "O" or pos[0] == "O" and pos[3] == "O" and pos[6] == "O" \
                or pos[2] == "O" and pos[4] == "O" and pos[6] == "O" or pos[0] == "O" and pos[4] == "O" and pos[8] == "O":


                break

            # -------------------------------------------------------------




            else:


                X = input("\n"+"Choose number 1 - 9 "+"\n"+
                          "X turn : ")


                if X != "1" and X != "2" and X != "3" and X != "4" and X != "5" \
                            and X != "6" and X != "7" and X != "8" and X != "9":


                    print("\n"+"numbers 1 - 9 only !, letters unallowed !"+"\n")


                    player_X()





                elif pos1 == "-" and X == "1" or pos2 == "-" and X == "2" or pos3 == "-" and X == "3" \
                        or pos4 == "-" and X == "4" or pos5 == "-" and X == "5" or pos6 == "-" and X == "6" \
                        or pos7 == "-" and X == "7" or pos8 == "-" and X == "8" or pos9 == "-" and X == "9":


                    X=int(X)
                    X-=1
                    pos[X]="X"
                    board()




                    if pos[0] == "X" and pos[1] == "X" and pos[2] == "X" or pos[3] == "X" and pos[4] == "X" and pos[5] == "X" \
                        or pos[6] == "X" and pos[7] == "X" and pos[8] == "X" or pos[2] == "X" and pos[5] == "X" and pos[8] == "X" \
                        or pos[1] == "X" and pos[4] == "X" and pos[7] == "X" or pos[0] == "X" and pos[3] == "X" and pos[6] == "X" \
                        or pos[2] == "X" and pos[4] == "X" and pos[6] == "X" or pos[0] == "X" and pos[4] == "X" and pos[8] == "X" \
                        or pos[0] == "O" and pos[1] == "O" and pos[2] == "O" or pos[3] == "O" and pos[4] == "O" and pos[5] == "O" \
                        or pos[6] == "O" and pos[7] == "O" and pos[8] == "O" or pos[2] == "O" and pos[5] == "O" and pos[8] == "O" \
                        or pos[1] == "O" and pos[4] == "O" and pos[7] == "O" or pos[0] == "O" and pos[3] == "O" and pos[6] == "O" \
                        or pos[2] == "O" and pos[4] == "O" and pos[6] == "O" or pos[0] == "O" and pos[4] == "O" and pos[8] == "O":

                        print("\n"+"X won, game over !")

                        break


                    else:
                        player_O()





                else:
                    print("Position already taken !")

                    player_X()

            #---------------------------------------------------------------


    def player_O():

        game_ongoing1 = True
        while game_ongoing1:



            pos1 = pos[0]
            pos2 = pos[1]

            pos3 = pos[2]
            pos4 = pos[3]
            pos5 = pos[4]
            pos6 = pos[5]

            pos7 = pos[6]
            pos8 = pos[7]

            pos9 = pos[8]





            if pos[0] == "X" and pos[1] == "X" and pos[2] == "X" or pos[3] == "X" and pos[4] == "X" and pos[5] == "X" \
                or pos[6] == "X" and pos[7] == "X" and pos[8] == "X" or pos[2] == "X" and pos[5] == "X" and pos[8] == "X" \
                or pos[1] == "X" and pos[4] == "X" and pos[7] == "X" or pos[0] == "X" and pos[3] == "X" and pos[6] == "X" \
                or pos[2] == "X" and pos[4] == "X" and pos[6] == "X" or pos[0] == "X" and pos[4] == "X" and pos[8] == "X" \
                or pos[0] == "O" and pos[1] == "O" and pos[2] == "O" or pos[3] == "O" and pos[4] == "O" and pos[5] == "O" \
                or pos[6] == "O" and pos[7] == "O" and pos[8] == "O" or pos[2] == "O" and pos[5] == "O" and pos[8] == "O" \
                or pos[1] == "O" and pos[4] == "O" and pos[7] == "O" or pos[0] == "O" and pos[3] == "O" and pos[6] == "O" \
                or pos[2] == "O" and pos[4] == "O" and pos[6] == "O" or pos[0] == "O" and pos[4] == "O" and pos[8] == "O":

                break




            else:

                O = input("\n"+"Choose number 1 - 9 " + "\n" +
                              "O turn : ")


                if O != "1" and O != "2" and O != "3" and O != "4" and O != "5" \
                        and O != "6" and O != "7" and O != "8" and O != "9":
                    print("\n" + "numbers 1 - 9 only !, letters unallowed !" + "\n")


                    player_O()




                elif pos1 == "-" and O == "1" or pos2 == "-" and O == "2" or pos3 == "-" and O == "3" \
                        or pos4 == "-" and O == "4" or pos5 == "-" and O == "5" or pos6 == "-" and O == "6" \
                        or pos7 == "-" and O == "7" or pos8 == "-" and O == "8" or pos9 == "-" and O == "9":


                    O = int(O)
                    O -= 1
                    pos[O] = "O"
                    board()




                    if pos[0] == "X" and pos[1] == "X" and pos[2] == "X" or pos[3] == "X" and pos[4] == "X" and pos[5] == "X" \
                        or pos[6] == "X" and pos[7] == "X" and pos[8] == "X" or pos[2] == "X" and pos[5] == "X" and pos[8] == "X" \
                        or pos[1] == "X" and pos[4] == "X" and pos[7] == "X" or pos[0] == "X" and pos[3] == "X" and pos[6] == "X" \
                        or pos[2] == "X" and pos[4] == "X" and pos[6] == "X" or pos[0] == "X" and pos[4] == "X" and pos[8] == "X" \
                        or pos[0] == "O" and pos[1] == "O" and pos[2] == "O" or pos[3] == "O" and pos[4] == "O" and pos[5] == "O" \
                        or pos[6] == "O" and pos[7] == "O" and pos[8] == "O" or pos[2] == "O" and pos[5] == "O" and pos[8] == "O" \
                        or pos[1] == "O" and pos[4] == "O" and pos[7] == "O" or pos[0] == "O" and pos[3] == "O" and pos[6] == "O" \
                        or pos[2] == "O" and pos[4] == "O" and pos[6] == "O" or pos[0] == "O" and pos[4] == "O" and pos[8] == "O":

                        print("\n"+"O won, game Over")
                        break



                    else:
                        player_X()







                else:

                    print("Position already taken !")

                    player_O()






    player_X()



player_Turn()