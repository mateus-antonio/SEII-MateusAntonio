import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds): #definição da função com argumento seconds
    print(f'Sleeping {seconds} second(s)...') 
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor: #usa o processpool executor para criar os multiprocess
    secs = [5, 4, 3, 2, 1] #argumentos de entrada da função
    results = executor.map(do_something, secs) #cria o multiprocess da função do_something com todos os valores de secs como argumentos

    for result in results: #passa pelo resultado dos multiprocess
        print(result) #printa o resultado dos multiprocess

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')