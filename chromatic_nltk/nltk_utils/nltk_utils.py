'''Created on Jan 10, 2013 @author: wiljoh'''

from  __future__ import division
import nltk

'''--------------------------------------------------------------------------'''
class chromatic_nltk_distrib :
    
        def __init__( self , data_directory = None ) :
            
            self.data_directory = data_directory                
    
        def lexical_diversity( self , text_data ):
        
            return len( text_data ) / len( set( text_data ) )           
        
        def generate_model( self , cfdist , word , num=15 ) :
            
            for i in range( num ):
                print   word ,
                word = cfdist[word].max()
                
        def unusual_words( self , text , wordlist ):
          
                text_vocab = set( w.lower() for w in text if w.isalpha() )
                english_vocab = set( w.lower() for w in nltk.corpus.words.words() )
                unusual = text_vocab.difference( english_vocab )
                
                return sorted( unusual )
        
        def content_fraction( self , first_data , second_data ) :                
                      
                content = [w for w in first_data if w.lower() not in second_data]
                                
                return len( content ) / len( first_data )      
            
        '''--------------------------------------------------------------------------------------------------------'''
        #attributes 
        @property
        def data_dir(self ):
            return self.data_directory
        
        def __str__( self ):    
            
                return 'chromatic_nltk_distrib->natural language toolkit'

        __repr__ = __str__                   

if __name__ == '__main__':
        
            cnd = chromatic_nltk_distrib()            
    
            text = nltk.corpus.genesis.words( 'english-kjv.txt' )
            bigrams = nltk.bigrams( text )
            cfd = nltk.ConditionalFreqDist( bigrams )           
            
            
            uw = cnd.unusual_words( nltk.corpus.gutenberg.words( 'austen-sense.txt' ) ,
                                    nltk.corpus.words.words() )
            #for i , j in enumerate( uw[0:25] ):
            #    print i , j 
                
            print cnd.content_fraction( nltk.corpus.reuters.words() , 
                                        nltk.corpus.stopwords.words( 'english' ) )               
            

           
            
            
           
            

