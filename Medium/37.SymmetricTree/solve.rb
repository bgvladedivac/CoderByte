class Node
	attr_accessor :value, :left_node, :right_node

	def initialize(value="" , left_node="", right_node="")
		@value = value
		@left_node = left_node
		@right_node = right_node
	end

	def to_s
		@value + " " + @left_node + " " + @right_node
	end
end






def isSymetric(left_node, right_node)
	if left_node == "" || right_node == "" 
		return left_node == "" && right_node == ""
	end

	return left_node == right_node && isSymetric(left_node.left, right_node.right) && isSymetric(left_node.right, right_node.left)

end

def SymmetricTree(tree)
   
tree_generated = false

index = 0
trees = []
root  = Node.new(tree[index], tree[index+1], tree[index+2])
visited = index + 2

trees << root

while not tree_generated
	index += 1
	n = Node.new(value=tree[index], left_node=tree[visited+1], rigth_node=tree[visited+2])

	trees << n
	visited += 2

	if index == tree.length - 1
		tree_generated = true
	end
end

isSymetric(trees[1], trees[2])
end
   
# keep this function call here    
puts SymmetricTree(STDIN.gets)