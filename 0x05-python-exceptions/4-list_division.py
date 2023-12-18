#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    fresh_empty_list = []
    for r in range(0, list_length):
        try:
            slash = my_list_1[r] / my_list_2[r]
        except TypeError:
            print("wrong type")
            slash = 0
        except ZeroDivisionError:
            print("division by 0")
            slash = 0
        except IndexError:
            print("out of range")
            slash = 0
        finally:
            fresh_empty_list.append(slash)
    return (fresh_empty_list)
