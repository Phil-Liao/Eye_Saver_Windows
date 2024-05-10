import playsound
def psound(*Args):
    file_name = ''
    for i in Args:
        file_name += str(i)
    playsound.playsound(file_name)