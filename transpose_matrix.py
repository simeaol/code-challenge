class Solution:
    def __init__(self):
        super().__init__()

    def transpose(self, A: List[List[int]], B: [List[List[int]]]):
        print(A, B)



if __name__ == "__main__":
    solution = Solution()
    solution.transpose([[1,2,3],[4,5,6],[7,8,9]])

    '''
    v1 = input("enter the value: ") # ask for input a catch the value in v1 variable
    v2 = eval(input("enter the expression")) #evalute the expression an input. e.g: 2+3*5

    ============Data Types================
    None, Numeric, List, Tuple, Set, String, Range, Dictionary
    
    Numeric: int, float, complex, bool, range

    complex(1,2) #result will be 1+2j

    String format:

    '{}, {}'.format(v1, v2) #using format method

    f'{v1}, {v2}' #using F-String


    for i in range(0, n): #in python we can use for-else condition. else will be exectuted only if "break" happen otherwise, it will not
        if(i == n*2)
        break
    else:
        pass



    =============Filter, Map reduce==================

    ==filter==
    def _even(n):
        return n%2==0
    evens = list(filter(_even, [1,2,3,4,5,6]))
    #or
    evens = list(filter(lambda n : n%2==0, [1,2,3,4,5,6]))

    ==map==
    sqrts = list(map(lambda n: n*n, evens))

    ==reduce==
    sum = reduce(lambda n1,n2: n1+n2, evens)





    ====================Pỳthon tips == List============
    lista = list() or lista=[] #create an empty list
    list = [1,2,3]
    matrix=[
            [1,2],
            [3,4]]

        list.append(5) #insert the element on the top of the list
        list.insert(pos, value) #where pos=position in the list where the "value" should be inserted
        
        list.extend([6,7,8]) #add multiply element(in flat) in the list

        list.remove(3) #remove the element 3 in the list
        list.pop(3) #remove the element located in position 3 of the list and return it
        list.pop() #remove the last inserted element in the list
        list.pop(-1)#remove the last index of the array
        del list[2:] #remove all the element of the list after index 2

        list.reverse() #reverse list element

        list.sort() #sort element in this list
        list.sort(reverse=True) #sort element in list and then reverse it

        sorted(list) #copy list element and sort it then return the new copy of the list

        sum(list) #sum elements of the list
        max(list) #return the max element in the list
        min(list) #return the min element in the list

        for index, el in enumerate(list) #enumerate return the INDEX and VALUE the list of element indexes
        for index, el in enumerate(list, start=1) #the first element index will be the start set value

        '-'.join(list) #join the list element according to format gived in ''


        from numpy import *
        arr = array[1,3,5,6,9]
        arr2 = arr + 5 #sum +5 for each element of the array

        arr3 = arr + arr2 #sum each specific element position-value in arr1 and arr2

        =================Python Tips - tuple ( tuple is unmutable)=============
        tp = tuple() #create an empty tuple
        tuple = (1, 2, 3, 4)


        =================Python Tips - Set (unorder and no duplicate element)============
        s = set() #create an empty set
        set1 = {1, 2, 3, 4, 5}
        set2 = {0,1,2}

        set1.intersection(set2) # return all common element between two sets

        set1.difference(set2) # return all different element of the set1 which is not in set2

        set.union(set2) #une two set. the result is set1 and set2 all in the same set


        ==============Python Tips - Dictionary =========================
        dict = {} #create an empty dictionary
        dict = {1:"sim", 2:"não", "name": "simeao", "age":28}
        
        dict['name'] #return the value of the key passed, if doesn't exist throw exception
        dict.get('name') #return the value of the key passed, if doesn't exist return "None"
        dict.get('phone', 'Not found') #return the default value if the key doesn't exist

        dict['phone'] = '999999-00' #add new pair(key, value) to the dictionary. if key already exist update the value

        dict.update({'name':'David', 'phone':'0000-000'}) #update single or multiple key and value elements of the dictionary

        del dict['name'] #delete a pair (key,value) in the dictionary
        dictionary.pop('age') #delete age key,pair element in the dictionary


        len(dict) #return the lenght of the dict
        dict.keys() #return all keys in the dict
        dict.values() #return all values of the dict
        dict.items() #return keys and values pair


        for key in dict: #loop in keys element
        for key, value in dict.items(): #loop for key,value elements in the dict



        ========Python Tips - slicing===========
        a = [1,2,3,4,5,6,7]
        a[:] #loop in array with step of 1 in incrising way
        a[1:] #lreturn the array of element starting in index 1
        a[1:-1]#return the array starting at element of index 1 until the last element of the array
        a[:-1] #return the reverse array
        a[::2] #return array list with step of two e.g:[2,4,6]
        a[::-2]#return reverse array list with step of 2


        =============Python Tips - Logical conditions ================
        a= True
        b= False

        a and b #similar to && in other language like java
        b or b #similiar to || in other language like java

        not a # similar to != in other language like java


        s1 = [1,2,3]
        s2 = [1,2,3]

        s1 == s2 #return true. compare values
        s1 is s2 #return false. compare objects. is the same doing "id(s1) == id(s2)"

        id(s1) #id return the memory identifier for the object in heap

        False evalutation:
        False,
        None
        Zero of any numeric type
        Any empty sequence. for example, '', (), []
        Any empty mapping. for example, {}

        element not in s1 #check if the element is not in the target
        element is in s1  #return True is element is in the target

        ==Bitwise==
        & #and
        | #or 
        ^ #xor
        ~ #complement of: e.g: 0001 is complement of 1110
        << #left-shift: gain bits beforne decimal
        >> #right-shift: loss bits before decimal




    ==============Python Tips - function _=================

    def function():

    def function(arg=1): #default params for function args

    def function(*args, **kwargs): #positioned elements




    import module
    import module as mod
    from module import func1, func2, variable1
    from module import func1 as fn1, function2
    from module import *




    ========Python tips = PIP==============
    pip install module_name
    pip uninstall module_name
    pip install -r configuration_file.txt #install all the modules defined in the configuration file
    pip list #list all the package/modules installed on the machine
    pip list --outdated #list all the outdated packages/modules
    pip install -U package/module name #update the given module




    virtualenv #handle multiple project version for diferent python version
    pip install virtualenv #install virtualenv 

    virtualenv myprojectname #create a new python project
    virtualenv -p /usr/bin/python2.6 myprojectname #create new project with specific python version dependence
    souce myprojectname/bin/activate #active the virtualenv for the current project

    which python #show the current python project path
    which pip

    pip freeze --local > requirement.txt #copy all env setup to file_name requirement.txt so you can use it in your other project
    diactivate #get out from the current virtual env and go back to the global config







   ==============Python tips - comprehensions ================

   ====List comprehension====
    arr = [n for n in range(0,10)] #create array list with elements from 0-10

    arr_copy = [n for n in el_list]#create array list with is copy of the arr array

    sqrt_el = [n*n for n in el_list] #multiply each element by it self an return the array of the correspondenting result

    sqrt_lambda = map(lamba n: n*n, arr) #using lambda (same with sqrt_el)

    even_arr = [n for n in arr if n%2 == 0] #return array of element wich is divisible to 2

    filter_arr = filter(lambda n: n%2==0, arr) #filter and returns elements mod of two

    #If I want a (letter, num) pair for each letter in 'abcd' and each number in 0123
    for letter in 'abcd':
        for num in range(0,4):
            mylist.append((letter, num))

    #using list comprehensions
    mylist = [(letter, num) for letter in 'abcd' for num in range(4)]


    ====Dictionary comprehension====
    names = ['Bruce', 'Clark', 'Tony Stark', 'thunder']
    heros = ['batman', 'superman', 'iron man','thor']
    my_dict = {}

    for name, hero in zip (names, heros): #loop int two array usin zip'and return each element of the arrays
        dict[name] = hero
    
    #using dictionary comprehensions
    dict = { name: hero for name, hero in zip(names, heros) }

    #dictionary comprehension using condition
    dict = { name: hero for name, hero in zip(names, heros) if name != 'thor" } #add elements which is diff to thor





    ==========Sorting==========
    arr = [a1, a2, a3]
    sorted(arr, key=myfunc, reverse=False) #sort arrays elements based on the first character

    def myfunc(el):
        return el[0]

        #or using lambda
    sorted(arr, key=lambda el: el[0])







    ===============Error Handling===============
    try:
        #do you task

    except FileNotFoundError as err: #multiple exception. general exception should be the last one
        #handler first exception
    except Exception as ex:
        #handler error
    else:
        #if no exception occurs, you can handle try bussiness code here
    finally:
        #finish your task


    =============== *ARGS x KWARGS

    def myfunc ( *args, **kwargs):
        print(args) #print a, 1, c
        print(kwargs) #print {"name":"Simeao", "email":"slamine@gmail.com"}

    myfunction('a', 1, 'c', name="simeao", email="slamine@gmail.com")






   =================== Duck Typing========================

    if isinstance(object, MyClass): #similar to java instanceof


    


    =================Decorator ==============================

    def decorator_function(myfunction):
        def wrapper(*args, **kwargs):
            myfunction()
        return wrapper
    
    @decorator_function
    def myfunction(*args, **kwargs):
        print(args, kwargs)

    f = decorator_function(myfunction)
    f() #execute wrapper function

    #using @
    myfunction() #execute wrapper inner function 







    ==============Python OOP===================
    +++++class variable, class attrs, classmethod, staticmethod and instance method
    class MyClass:
        count_instance = 0 #class variable
        def __init__(self, name, surname, pass): #constructor with class attributes
            self.name = name
            self.pass = pass
            self.surname = surname

        def full_name(self):
            return self.name + self.surname

        @classmethod
        def get_instance(cls): #cls is required in classmethod to diferentiate it with static method
            return cls.count_instance

        @classmethod
        def create_from_string(cls, input_string):
            name, surname, pass = input_string.split(',')
            return cls(name, surname, pass) #create a new instance of MyClass

        @staticmethod
        def mystaticmethod(value1):
            print(value1)

        instance1 = MyClass('sime','lamine', '123')

        instance2 = MyClass.create_from_string('sime,lamine,123')




        =====Inherentance====
        class Employee:
            def __init__(self, name, salary)
        
        class Developer(Employee):
            pass #just pass the scope
        
        class Manager(Employee): #something like Manager extends Employee
            def__init__(self, name, salary, nstaff=0): #set nstaff default value to 0
                super().__init__(name, salary) #constructor override
                #Employee.__init__(self, name, salary) #Do the same thing as the previous
                self.nstaff = nstaff
            
            def bonus(self):
                return self.salary * 1.5

        ====Abstract class====
        from abc import ABC, abstractmethod #abc=abstract base classes

        class Computer(ABC): #abstract class should have at least one abstract method

            @abstractmethod
            def process(self):
                pass
        
        class Laptop(Computer): #class extends abstract class
            def process(self):
                pass

        comp1 = Computer() #will throw error. Cannot instantiate abstract class with abstract method
    '''