#!/usr/bin/python3
""" My class module
"""
import cmd
from models.base_model import BaseModel
from models import storage


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
        """Create command to create an instance\n"""
        if args[0] == '':
            print("** class name missing **")
            return
        classname = args[0]
        obj = self.__mapping(classname)
        if obj == False:
            print("** class doesn't exist **")
        else:
            obj = obj()
            obj.save()
            print(obj.id)

    def do_show(self, *args):
        """Show command to show an instance\n"""
        args = args[0].split(' ')
        if args[0] == '':
            print("** class name missing **")
            return
        classname = self.__mapping(args[0])
        if classname == False:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id = args[1]
        obj = classname.find(id)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def __mapping(self, classname):
        """_summary_
        """
        if classname == 'BaseModel':
            return BaseModel
        else:
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
