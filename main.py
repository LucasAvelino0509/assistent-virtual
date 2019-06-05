# coding=utf-8
import cmds_module
import cognition_module
import util_module
from importlib import reload


# executeCmd(txt)


cmds_module.loadCmds()
while True:
    try:
        reload(cmds_module)
        reload(cognition_module)
        reload(util_module)
        print("Reload modules")
        if cognition_module.listen().lower() == "assistente":
            cognition_module.speak("Estou escutando")
            cognition_module.speak(cmds_module.executeCmd(cmds_module.evaluateCmd(cognition_module.listen())))
    except Exception as e:
        print(e)
        continue;
