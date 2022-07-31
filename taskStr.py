import logging

logging.basicConfig(filename='TaskStr.log',filemode='w',level=logging.DEBUG,format='%(asctime)s---%(name)s--%(levelname)s--%(message)s')


class TaskStr:

    def extract_data(self, s):
        """
        1 . Try to extract data from index one to index 300 with a jump of 3
        """
        try:
            logging.info("this is your input:  %s ", s)
            s1 = s[1:300:3]
            logging.info("The Str output is: %s", s1)
            return s1
        except Exception as e:
            logging.exception("The Error is:" ,e)

    def rev_str(self,s):
        '''
        2 . Try to reverse a string without using reverse function
        '''
        try:
            logging.info('your input is: %s',s)
            rs=s[::-1]
            logging.info('your reverse str: %s',rs)
            return rs
        except Exception as e:
            logging.exception('Error found',e)
        
    def splt_Upr_str(self,s):
        '''
         3. Try to split a string after conversion of entire string in uppercase
        '''
        try:
            logging.info('this is input str: %s',s)
            upr=s.upper()
            splt=upr.split()
            logging.info('this is your output:%s',splt)
            return splt
        except Exception as e:
            logging.exception(e)
    
    def Covt_StrInto_lower(self,s):
        '''
          4. try to convert the whole string into lower case
        '''
        try:
            logging.info('your input is : %s',s)
            s1=s
            s2=s.lower()
            logging.info('your output is %s',s2)
            return s2
        except Exception as e:
            logging.exception(e)

            
    def Covt_StrInto_captl(self,s):
        '''
         5 . Try to capitalize the whole string
        '''
        try:
            logging.info('the input is :%s',s)
            cptl=s
            c2=cptl.capitalize()
            logging.info('the out is: %s',c2)
            return c2
        except Exception as e:
            logging.exception(e)

cl=TaskStr()
cl.Covt_StrInto_captl('rohit khan\n')
cl.Covt_StrInto_lower('RoHiT KHAn\n')
cl.extract_data('rohit khan\n')
cl.splt_Upr_str('rohit khan\n')
cl.rev_str('rohit khan')
