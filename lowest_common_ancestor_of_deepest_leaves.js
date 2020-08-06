// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */





function deepth(node) {
    var d = []
    var de = node.deep
    if (node.left) {
        d.push(deepth(node.left))
    }
    if (node.right) {
        d.push(deepth(node.right))
    }
    if (d.length > 0) {
        de = Math.max(...d)
        node.deep = de
    }
    return de
}


function subtree(node) {
    if (node.left && node.right) {
        if (node.left.deep == maxDeepth && node.right.deep == maxDeepth) {
            return node
        }
    }
    if (node.left) {
        var nl = subtree(node.left)
        if (nl) {
            return nl
        }
    }
    if (node.right) {
        var nr = subtree(node.right)
        if (nr) {
            return nr
        }
    } 
    if (!node.left && !node.right && node.deep == maxDeepth) {
        return node
    }
}


var lcaDeepestLeaves = function(root) {
    root.deep = 0
    var nodes = [root]
    maxDeepth = 0
    while (nodes.length > 0) {
        node = nodes.pop()
        if (node.left) {
            node.left.deep = node.deep + 1
            nodes.push(node.left)
            maxDeepth = Math.max(maxDeepth, node.deep + 1)            
        }
        if (node.right) {
            node.right.deep = node.deep + 1
            nodes.push(node.right)
            maxDeepth = Math.max(maxDeepth, node.deep + 1)
        }
    }
    deepth(root)
    return subtree(root)
};




