#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point for the code"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with Ctrl+D (EOF)"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if obj_key in all_objs:
            print(all_objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name.
        Usage: all [class name]
        """
        args = arg.split()
        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        objects = [str(obj) for key, obj in all_objs.items() if not args or key.split('.')[0] == args[0]]
        print(objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
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

        obj_key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if obj_key in all_objs:
            obj = all_objs[obj_key]
            attr_name = args[2]
            attr_value = args[3]

            # Update only "simple" attributes (string, integer, float)
            if attr_name not in ['id', 'created_at', 'updated_at']:
                # Convert attribute value to the correct data type
                try:
                    attr_value = eval(attr_value)
                except (NameError, SyntaxError):
                    pass

                setattr(obj, attr_name, attr_value)
                storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
