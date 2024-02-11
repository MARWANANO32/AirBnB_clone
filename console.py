#!/usr/bin/python3

import cmd
import json
import models


class HBNBCommand(cmd.Cmd):
    custom_prompt = "hbnb"

    def Quit(self, args):
        return True

    def EOF(self, args):
        return True

    def Empty_line(self):
        return False

    def Create(self, args):
        if args == "":
            print("** class name missing **")
        elif args not in HBNBCommand:
            print("** class doesn't exist **")

    def Show(self, args):
        a = 0
        arg = args.split()

        if args == "":
            print("** class name missing **")
        elif arg[0] not in HBNBCommand:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
