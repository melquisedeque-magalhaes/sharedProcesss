import multiprocessing


def ping_pipe(connection):
    connection.send('Vamos tomar')


def pong_pipe(connection):
    msg = connection.recv()
    print(f'{msg} Cerveja')


def function_used_pipe():
    connection1, connection2 = multiprocessing.Pipe()

    process1 = multiprocessing.Process(target=ping_pipe, args=(connection1,))
    process2 = multiprocessing.Process(target=pong_pipe, args=(connection2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()


def ping_queue(queue):
    queue.put('Vamos tomar')


def pong_queue(queue):
    msg = queue.get()
    print(f'{msg} Cerveja')


def function_used_queue():
    queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=ping_queue, args=(queue,))
    process2 = multiprocessing.Process(target=pong_queue, args=(queue,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()


if __name__ == '__main__':
    function_used_queue()
    function_used_pipe()
