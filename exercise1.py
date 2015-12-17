#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Rachel Lee'
__email__ = "siuming.lee@mail.utoronto.ca"


#####################
# HELPER FUNCTIONS ##
#####################

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def selection(t, f):
    """
    Perform select operation on table t that satisfy condition f.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]

    """

# :param t: table that function is to be performed on
# :param f: function that will operate on the table
# :return: a table that is the result of applying f to t

    # for each row in a table, return the row values when the function is satisfied
    # need to return as a table (list of lists)!
    table = []
    for i in t:
        if f(i) is True:
            table.append(i)
    return table


def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """
# :param t: original table
# :param r: an attribute (column) to sort the table by; can accept multiple
# :return: the columns of the original table that match the attributes parameter

    index_list = []
    final_table = []

# get a list of index numbers from attributes (r)
    for row in t:
        for item in row:
            if item in r:
                index_list.append(row.index(item))

# compile table of rows (list of lists),
# each row should include items found at each index gotten above
    for row in t:
        for x in index_list:
            final_table.append(row[x])

    return final_table
# returns a list of the right items, but not in table format


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]


    """

# :param t1: original table 1
# :param t2: original table 2
# :return: table including all combinations of rows from table 1 and table 2

# create a table including headings composed of the first rows of given tables
    combined_table = [t1[0] + t2[0]]

    # mix and match all values except for headings and add to created table
    for x in t1:
        for y in t2:
            if x != t1[0] and y != t2[0]:
                combined_table.append(x + y)

    return combined_table
