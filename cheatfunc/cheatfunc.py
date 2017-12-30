  
import ConfigParser
import os

class CheatException(Exception):
    pass

def get_current_dir():
    cp = ConfigParser.SafeConfigParser()
    cp.read('cheat.ini')
    return cp.get("CHEAT_PATH", "cheatpath")

def list_all_cheats():
    path = get_current_dir()
    for elem in os.listdir(path):
        if os.path.isfile(path+'/'+ elem):
            print elem

def search_cheat_by_kw(kwrd):
    path = get_current_dir()
    find = False
    files = [path+'/' + elem for elem in os.listdir(path) if os.path.isfile(path+'/' + elem)]
    for file in files:
        with open(file, 'r') as fd:
            lines = fd.readlines()
            for line in lines:
                if kwrd in line:
                    find = True
                    print '['+ os.path.basename(file) + ']'+": "+ line

    if find == False:
        print "No key word find"

def print_certain_cheat(cheat):
    path = get_current_dir()
    files =  os.listdir(path)
    if cheat in files:
        if os.path.isfile(path+'/' + cheat):
            with open(path +'/' + cheat) as fd:
                print fd.read()
            exit(0)
    print "can not find cheat for "+cheat

def config_cheat_config():
    try:
        cfpath = get_current_dir() + '/' + 'cheat.ini'
    except:
        raise CheatException("cfg file error")
    else:
        vipath = os.environ.get('VIM_PATH')
        if vipath == None:
            raise CheatException("no VIM_PATH env var")
        else:
            os.system(vipath + " " + cfpath)

def edit_or_add_cheat(cheat):
    path = get_current_dir()
    files = os.listdir(path)
    vipath = os.environ.get('VIM_PATH')
    if vipath == None:
        raise CheatException("no VIM_PATH env var")
    if cheat in files:
        os.system(vipath + " " + path + '/' + cheat)
    else:
        filepath = path + '/' + cheat
        os.system("touch " + filepath)
        os.system(vipath + " " + filepath)
