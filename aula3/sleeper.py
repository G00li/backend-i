
#PROGRAMA QUE REALIZA A CONTAGEM DO TEMPO 

import time

def timer (func: callable):
    def weapper(*args,**kwargs):
        start_time = time.perf_counter() # Ativa o cronometro quando a funcao wrapper e chamada 
        print(f"Start time {start_time}")
        result = func(*args,**kwargs)
        end_time = time.perf_counter() # Desatia o cronometro quando a funcaçãoi execute() termina 
        print(f"End time {end_time}")
        total_time = end_time-start_time #Calcula a diferença entre o star_time e end_time 
        print (f'Function {func.__name__} {args} {kwargs} Took {total_time:.4f} seconds')
        if total_time > 4: #aborta a operação caso seja maior que 4s
            raise Exception ("Aborted. try again later")

        return result
    return weapper
        
@timer
def do_things():
    time.sleep(3)

@timer
def execute () -> None:
    do_things()
    time.sleep(1)


if __name__ == "__main__":
    execute()