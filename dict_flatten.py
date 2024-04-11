# -*- coding: utf-8 -*-


def dict_flatten(to_be_flatten_dict, prefix_str = '',joint_str = '_'):
    """
    该函数用于将一个多层嵌套的字典转换成一个单层的字典。
    temp_dict = {'cascas':'c'
                 ,'ca':{'bgb':{'ujujuj':'vdsx'}}
                 ,'mkm':{'wewrwer':{'bnv':{'qwqs':{'cvbcvb':'xalx'}}}}}
    
    flatten_dict = {}
    for item in dict_flatten(temp_dict,joint_str = '_'):
        flatten_dict.update(item)
    print(flatten_dict)
        
    #将打印
    {'cascas': 'c', 'ca_bgb_ujujuj': 'vdsx', 'mkm_wewrwer_bnv_qwqs_cvbcvb': 'xalx'}
    
    """

    for key,value in to_be_flatten_dict.items():
        if isinstance(value,dict):
            if not prefix_str:
                yield from dict_flatten(value,key + joint_str)
            else:
                yield from dict_flatten(value,prefix_str + key + joint_str)
        else:
            if not prefix_str:
                yield {key:value}
            else:
                yield {prefix_str + key:value}




if __name__ == '__main__':
    temp_dict = {'cascas':'c'
                 ,'ca':{'bgb':{'ujujuj':'vdsx'}}
                 ,'mkm':{'wewrwer':{'bnv':{'qwqs':{'cvbcvb':'xalx'}}}}}
    
    flatten_dict = {}
    for item in dict_flatten(temp_dict,joint_str = '_'):
        flatten_dict.update(item)
    print(flatten_dict)





