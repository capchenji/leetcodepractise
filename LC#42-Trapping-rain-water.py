class Solution:
    def trap(self, height: List[int]) -> int:

        output = 0
        init_num = 0
        left_array = []
        for i in range(0,len(height)):
            if height[i]>init_num:
                init_num = height[i]
            left_array.append(init_num)

        right_array = [0]*len(height)
        init_num = 0
        for i in range(1,len(height)+1):
            if height[-1*i]>init_num:
                init_num = height[-1*i]
            right_array[-1*i] = init_num

        final_array = []
        for i in range(0,len(height)):
            final_array.append(min(left_array[i], right_array[i]) - height[i])

        # final_array = min(left_array, right_array)

        # output = sum(final_array - height)

        output = sum(final_array)

        return output
