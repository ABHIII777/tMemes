import time
import sys

def loadingSpinner(text="Loading"):
    spinner = ['|', '/', '-', '\\']
    for i in range(10):
        for symbol in spinner:
            sys.stdout.write(f'\r{text}... {spinner[i % 4]}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(text) + 5) + '\r') 