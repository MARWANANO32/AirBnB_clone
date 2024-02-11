#!/usr/bin/python3
""" My class module
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """_summary_
    """
    prompt = "(hbnb) "

    def do_quit(self, *args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """_summary_"""
        return False

    def do_create(self, *args):
        if len(args) == 0:
            print("** class name missing **")
            return
        classname = args[0]
        obj = self.__mapping(classname)
        if obj == False:
            print("** class doesn't exist **")
        else:
            obj.save()
            print(obj.id)

    def do_show(self, *args):
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

    def __mapping(self, classname):
        """_summary_
        """
        if classname == 'BaseModel':
            return BaseModel()
        else:
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
