# mining.py

def days_between(d1_, d2_): ## pass in date time objects, if string see commented code 
    # d1_ = datetime.strptime(d1_, "%Y-%m-%d")
    # d2_ = datetime.strptime(d2_, "%Y-%m-%d")
    return abs((d2_ - d1_).days)

# report.py

def Average(Mylist): 
    return sum(Mylist) / len(Mylist)
    
def Median(Mylist): 
    return statistics.median(Mylist)

# dataset.stats.py

def getFileLength(file_):
    return sum(1 for line in open(file_, encoding='latin-1'))
  
def days_between(d1_, d2_): ## pass in date time objects 
    return abs((d2_ - d1_).days)
