class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 1 << level
        # (level)2 -> (level 0)2
        # power(2,level)

        # find level first
        level = 0
        while ((1 << (level+1))-1 )< label:
            level += 1
        
        path = []
        while label >= 1:
            path.append(label)
            level_max = (1 << (level+1)) - 1
            level_min = (1 << (level))

            label = (level_max + level_min - label) // 2
            level -= 1

        return path[::-1]


        #                    1
        #              2            3
        #           4    5        6      7
        #          8 9 10 11    12 13 14  15
        #              ｜
        # original position

        # 在一个完全二叉树中，对于任何一个节点而言，它的子节点可以通过以下方式找到：
        # 左子节点 = 父节点 * 2
        # 右子节点 = 父节点 * 2 + 1
        # 反过来，如果你有一个子节点，你可以通过整除 2 的操作找到父节点的标签：
        # 父节点 = 子节点 // 2

        # 对于当层反序，我们需要找到他的镜像位置：
        #         4     5        6    7
        # ->    15 14 13 12    11 10 9 8
#                                 ｜
        # mirror position
        # (original position + mirror position) = (level_min + level_max)
        # mirror position = level_min + level_max - original postion
        # parent(mirror position) = (level_min + level_max - original postion) // 2

        # 对于当层顺序(上一层反序)：
        #                 ｜                             ｜
        #        3        2                              2       3
        # ->   4   5    6   7                          4   5   6   7
        #               ｜                                 ｜
        # 我们也可以先找当前层的镜像位置，在去上一层寻找parent node
