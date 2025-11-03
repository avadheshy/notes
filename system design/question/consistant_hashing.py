from collections import Counter
import bisect
import hashlib

class ConsistantHashing():
    def __init__(self,nodes,vnode):
        self.nodes=set()
        self.vnode=vnode
        self.ring={}
        self.hash_fun = int(lambda key : hashlib.md5(key).hexdigest(),16)
        self.arr=[]
        self.nodes_data={}
    def get_node_str(self,node,i):
        return f"node:{node} and vnode:{i}".encode('utf-8')
    def add_node(self,node):
        if node in self.nodes:
            return
        self.nodes.add(node)
        self.nodes_data[node]=set()
        for i in range(self.vnode):
            h=self.hash_fun(self.get_node_str(node,i))
            self.ring[h]=node
            