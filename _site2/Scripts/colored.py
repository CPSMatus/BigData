# colorspep8.py

class Alerta():


    # name made in constructor
    def __init__(self, error_code,jugador):
        self.error_code = error_code
        self.jugador = jugador

    def colors_16(color_):
        return("\033[2;{num}m {num} \033[0;0m".format(num=str(color_)))

    def colors_256(self,error,jugador):
        num1 = str(9) # 9: rojo
        message = str(error) + ".-" + str(jugador)
        num2 = str(message).ljust(3, ' ')


        if color_ % 16 == 0:
            return(f"\033[38;5;{num1}m {num2} \033[0;0m\n")
        else:
            return(f"\033[38;5;{num1}m {num2} \033[0;0m")

    def print_error_message(self):
        CRED = '\033[91m'
        CEND = '\033[0m'
        error =  "Error "
        error_1 = str(self.error_code)
        error_2 = str(self.jugador )
        final_error = error + error_1  +".- " +  error_2
        print(CRED + final_error  + CEND)
        #print("\n", self.colors_256(self.error_code,self.jugador) )
