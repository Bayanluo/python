#dictionary file
dic={'name':'Fateme','age':'twelve','gread':'sixth'}
dic2={'brother':'Ali'}
print('length:',len(dic),
      'equivalent:',str(dic),
      'variable type:',type(dic) ,
      'copy dic:' ,dic.copy() ,
      'new dic:' ,dic.fromkeys() ,
      'value:' ,dic.get('name') , 
      'items:' ,dic.items() ,
      'keys:' ,dic.keys() ,
      'setdefault:' ,dic.setdefault() ,
      'value:' ,dic.values(),
      'update:' ,dic.update(dic2))