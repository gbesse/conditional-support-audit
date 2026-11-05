import unittest,math
from conditional_support_audit.core import run
class DomainTests(unittest.TestCase):
 def test_joint_absence(self):
  x=run({'columns':['a','b'],'reference':[dict(a=1,b=1),dict(a=2,b=2)],'synthetic':[dict(a=1,b=2)]});self.assertEqual(x['checks'][0]['unseen_synthetic_rows'],[0])
 def test_type_preservation(self):
  x=run({'columns':['a'],'reference':[dict(a=True)],'synthetic':[dict(a=1)]});self.assertEqual(x['checks'][0]['unseen_synthetic_rows'],[0])
 def test_seen(self):self.assertEqual(run({'columns':['a'],'reference':[dict(a=None)],'synthetic':[dict(a=None)]})['checks'][0]['unseen_synthetic_rows'],[])
