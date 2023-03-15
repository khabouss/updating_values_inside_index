import sys

def update_ui(current_prog):
    sys.stdout.write("\r{0}>".format("="*2))
    sys.stdout.write("\033[92m CURRENT PROGRESS: \033[0m")
    sys.stdout.write(" "+str(current_prog)+"/316")
    sys.stdout.flush()
