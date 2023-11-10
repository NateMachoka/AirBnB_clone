#!/usr/bin/python3
"""
console module

Implements the command interpreter for the AirBnB clone project.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class

    Implements the command interpreter for the AirBnB clone project.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line (pressing ENTER)"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        if class_name not in storage.classes().keys():
            print("** class doesn't exist **")
            return

        obj_dict = storage.all().get(key)

        if obj_dict is None:
            print("** no instance found **")
        else:
            print(obj_dict)


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj_dict = storage.all().get(key)
        if obj_dict is None:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        objs = storage.all()

        if not arg:
            print([str(objs[key]) for key in objs])
        else:
            args = arg.split()
            class_name = args[0]

            if class_name not in storage.classes().keys():
                print("** class doesn't exist **")
            else:
                print([str(objs[key]) for key in objs if key.startswith(class_name)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj_dict = storage.all().get(key)
        if obj_dict is None:
            print("** no instance found **")
        else:
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj_dict, attr_name, type(getattr(obj_dict, attr_name))(attr_value))
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
