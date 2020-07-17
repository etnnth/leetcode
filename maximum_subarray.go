func maxSubArray(nums []int) int {
    m0,m1 := nums[0], nums[0]
    for i:=1 ; i<len(nums) ; i++ {
        if m0 + nums[i] > nums[i] {
            m0 += nums[i]
        } else {
            m0 = nums[i]
        }
        if m0 > m1 {
            m1 = m0
        }
    }
    return m1
}
