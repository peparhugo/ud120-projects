def outlierCleaner(predictions, ages, net_worths):

    import numpy as np
    

    removal = (net_worths - predictions)**2
    
    zip_data=zip(ages, net_worths, removal)
    dtype = [('ages', int),  ('net_worths', float),('error', float)]
    np_data = np.array(zip_data,dtype=dtype)
    np_data.sort(order='error')
    print np_data
    for i in range(0,int(round(0.1*np_data.size))):
        x = int(np_data.size)-1
        np_data = np.delete(np_data, (x),axis=0)
    cleaned_data = tuple(map(tuple,np_data))
    print np_data
    return cleaned_data
    
