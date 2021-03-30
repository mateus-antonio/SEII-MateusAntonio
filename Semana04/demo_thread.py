import concurrent.futures
import time
import threading

start = time.perf_counter()


def do_something(seconds): #definição da função com argumento seconds
    print(f'Sleeping {seconds} second(s)...') 
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'
    #printf(f'Done Sleeping...{seconds}')


with concurrent.futures.ThreadPoolExecutor() as executor: #usa o threadpool executor para criar as threads
    secs = [5, 4, 3, 2, 1] #argumentos de entrada da função
    results = executor.map(do_something, secs) #cria a thread da função do_something com todos os valores de secs como argumentos
    
    for result in results: #passa pelo resultado das threads
        print(result) #printa o resultado das threas

'''
threads = [] 

for _ in range(10): #loop para criar 10 threads
    t = threading.Thread(target=do_something, args=[1.5]) #cria a thread
    t.start() #inicializa a thread
    threads.append(t) #registra a thread em threads

for thread in threads: #passa pela lista de thread
    thread.join() #espera a thread e a fecha
'''

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')