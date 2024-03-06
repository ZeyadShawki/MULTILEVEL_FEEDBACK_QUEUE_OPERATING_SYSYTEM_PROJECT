import queue
import random


class Process:
    def __init__(self, process_id, quantum_time):
        self.process_id = process_id
        self.quantum_time = quantum_time


def print_process_data(processes):
    for process in processes:
        print(
            f"Process {process.process_id}: Quantum Time = {process.quantum_time}")


def execute_processes(queue1, queue2, queue3):
    total_processes = 100
    time_quantum_q1 = 8
    time_quantum_q2 = 16

    processes = [Process(i, random.randint(1, 100))
                 for i in range(total_processes)]

    print("Processes data before enqueuing:")
    print_process_data(processes)
    print()

    for process in processes:
        queue1.put(process)

    while not queue1.empty():
        current_process = queue1.get()
        if current_process.quantum_time <= time_quantum_q1:
            print(
                f"Executing process {current_process.process_id} from Queue 1 RR with quantum time {current_process.quantum_time}")
            current_process.quantum_time = 0
        else:
            current_process.quantum_time -= time_quantum_q1
            print(
                f"""Transferring process {current_process.process_id} from Queue 1  RR to Queue 2 RR with quantum time before excution  = {current_process.quantum_time + time_quantum_q1} after excution ={  current_process.quantum_time}""")
            queue2.put(current_process)

    # Wait for Queue 2 to finish
    while not queue2.empty():
        current_process = queue2.get()
        if current_process.quantum_time <= time_quantum_q2:
            print(
                f"Executing process {current_process.process_id} from Queue 2 RR with quantum time {current_process.quantum_time}")
            current_process.quantum_time = 0
        else:
            print(
                f"Transferring process {current_process.process_id} from Queue 2 RR to Queue 3 FCFS with quantum time {time_quantum_q2}")
            current_process.quantum_time -= time_quantum_q2
            queue3.put(current_process)

    # Wait for Queue 3 to finish
    while not queue3.empty():
        current_process = queue3.get()
        print(
            f"Executing process {current_process.process_id} from Queue 3 (FCFS) with quantum time {current_process.quantum_time}")


# Create queues
queue1 = queue.Queue()
queue2 = queue.Queue()
queue3 = queue.Queue()

# Execute processes
execute_processes(queue1, queue2, queue3)
