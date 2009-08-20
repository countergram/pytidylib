if __name__ == '__main__':
    from tidylib import tidy_document
    import os
    import cProfile
    import pstats
    
    text = '''<p>foo <img src="bar.jpg"> & stuff'''
    def foo():
        tidy_document(text, keep_doc=True)
    def bar():
        for i in xrange(1000):
            foo()
    
    cProfile.run('bar()', 'tidylib_profile.tmp')    
    pstats.Stats('tidylib_profile.tmp').sort_stats('time').print_stats()
    os.unlink('tidylib_profile.tmp')
