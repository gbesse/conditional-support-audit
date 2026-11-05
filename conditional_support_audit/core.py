import math,random,itertools
from .common import number,integer,identifier,unique_ids
def scalar(v):
 if v is None or type(v)in [str,int,bool]:return (type(v).__name__,v)
 if type(v)is float:number(v);return ('float',v)
 raise ValueError('scalar')
def run(d):
 cols=d['columns'];ref=d['reference'];syn=d['synthetic'];order=integer(d.get('order',2),1,3)
 if not 1<=len(cols)<=8 or len(set(cols))!=len(cols)or len(ref)+len(syn)>10000:raise ValueError('size')
 for c in cols:identifier(c)
 out=[]
 for subset in itertools.combinations(cols,min(order,len(cols))):
  seen={tuple(scalar(row[c])for c in subset)for row in ref};unexpected=[]
  for i,row in enumerate(syn):
   if tuple(scalar(row[c])for c in subset)not in seen:unexpected.append(i)
  out.append(dict(columns=list(subset),reference_combinations=len(seen),unseen_synthetic_rows=unexpected))
 return dict(checks=out,reference_rows=len(ref),synthetic_rows=len(syn),unseen_means_invalid=False)
