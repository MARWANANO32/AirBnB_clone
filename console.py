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
        if not obj:
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
        if not classname:
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

    def do_destroy(self, *args):
        """Destroy command to destroy an instance\n"""
        args = args[0].split(' ')
        if args[0] == '':
            print("** class name missing **")
            return
        classname = self.__mapping(args[0])
        if not classname:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id = args[1]
        if classname.destroy(id):
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, *args):
        """All command to get all instances\n"""
        if args[0] != '':
            classname = self.__mapping(args[0])
            if not classname:
                print("** class doesn't exist **")
                return
        res = []
        objs = storage.all()
        for key in objs:
            res.append(str(objs[key]))
        print(res)

    def do_update(self, *args):
        """Update command to update instance by id\n"""
        args = args[0].split(' ')
        if args[0] == '':
            print("** class name missing **")
            return
        classname = self.__mapping(args[0])
        if not classname:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        id = args[1]
        key = args[2]
        val = args[3][1:-1]
        obj = classname.find(id)
        if obj:
            if hasattr(obj, key):
                attrType = type(obj.id)
                setattr(obj, key, attrType(val))
            else:
                setattr(obj, key, val)
            obj.save()
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
