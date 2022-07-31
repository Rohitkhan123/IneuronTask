import logging

logging.basicConfig(filename='ListTask.log',filemode='w',level=logging.DEBUG,format='%(asctime)s---%(name)s--%(levelname)s--%(message)s')


class List_Task:

    def extract_list(self,l):
        '''
            Try to extract all the list entity 
        '''
        try:
            l1=[]
            logging.info('This is input: %s',l)
            for i in l:
                if type(i)==list:
                    l1.extend(i)
            logging.info('this is your output: %s',l1)
            return l1

        except Exception as e:
            logging.exception(e)



    
    def extract_ineuron_fromList(self,l):
        '''
            Try to extract "ineruon" out of this data
        '''
        try:
            l2=[]
            logging.info('your input: %s',l)
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j=='ineuron':
                            l2.append(j)
            logging.info('your output:%s',l2)
            return l2
            if type(i)==dict:
                    for k in i.items():
                        for g in k:
                            if g=='ineuron':
                                l2.append(g)
            logging.info('your output:%s',l2)
            return l2 
        except Exception as e:
            logging.exception(e)


    def flat_list(self,l):



        '''
            Try to unwrape all the collection inside collection and create a flat list
        '''
        logging.info('your input is:%s ',l)
        try:
            l3=[]
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j)==int or type(j)==str or type(j)==float:
                            l3.append(j)

                if type(i)==dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int  or type(g) == str:
                                l3.append(g)
            logging.info('the output is: %s',l3)
            return l3
        except Exception as e:
            logging.exception(e)



    def reverse_list(self, l):
        """
            Returns the given list in reverse order
        """
        try:
            logging.info("your input is: %s", l)
            l.reverse()
            logging.info('your Reversed List: %s', l)
            return l
        except Exception as e:
            logging.exception(e)


    

    def Ext_keys_FromList(self,l):
        '''
            Try to list all the key in dict element avaible in list
        '''
        try:
            l1=[]
            logging.info('the input is: %s',l)
            for i in l:
                if type(i)==dict:
                    l1.append(i.keys())
            logging.info('your output:%s',l1)
            return l
        except Exception as e:
            logging.exception(e)




    def Ext_values_FromList(self,l):
        '''
            Try to extract all the value element form dict available in list
        '''
        try:
            l1=[]
            logging.info('your input is: %s',l)
            for i in l:
                if type(i)==dict:
                    l1.append(i.value())
                return l1
            logging.info('your output is :%s',l1)
        except Exception as e:
            logging.exception(e)




    def find_vovel(self,s):
        '''
        Try to filter out all the vowels form below text by using while loop
        '''
        try:
                l1=[]
    
                i = 0 
                v = 'aeiouAEIOU'
                logging.info('your input is: %s',s)
                while i < len(s):
                    if s[i] in v :
                        l1.append(s[i])
                    i = i+1
                logging.info('you output is: %s',l1)
                return l1
        except Exception as e:
            logging.exception(e)


    

    def  Ext_Only_tuple(self,l):
        '''
        To extract tuples from a collection
        '''
        try:
            l1=[]
            logging.info('your input is: %s',l)
            for i in l:
                if type(i)==tuple:
                    l1.append(i)
                    logging.info('your output is %s',i)
            return l1
        except Exception as e:
            Exception(e)

####---------------------------------------------------------------------------------------------------------------


    
    
l=[[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) ,
{'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]


cls_object=List_Task()
cls_object.Ext_Only_tuple(l)
cls_object.Ext_keys_FromList(l)
cls_object.reverse_list(l)
cls_object.flat_list(l)


