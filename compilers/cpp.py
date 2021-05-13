import subprocess

def compile(id, files):
    source = []
    for file in files:
        source.append(f'temp/{id}/'+file)

    proc = subprocess.Popen(['g++', *source, '-std=c++14', '-o', f'temp/{id}/compiled'], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)
    
    return proc.stdout.readline(), proc.stderr.readline()